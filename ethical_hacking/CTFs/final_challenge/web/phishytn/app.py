#!/usr/bin/env python3

__author__ = 'golim'

from flask import Flask, render_template, request, redirect, url_for, session, flash
from io import BytesIO

import sqlite3
import logging
import qrcode
import base64
import pyotp
import os

if 'FLAG' in os.environ:
    FLAG = os.environ['FLAG']
else:
    FLAG = 'UniTN{placeholder_flag}'

app = Flask(__name__)

app.secret_key = 'youshouldnotbeabletoreadthisaaaaaaaaaaaabbbbbb'

DATABASE = 'database.db'

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

def clean_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Drop all tables
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('DROP TABLE IF EXISTS licenses')
    cursor.execute('DROP TABLE IF EXISTS passwords')

    conn.commit()
    conn.close()

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            ffa_enabled BOOLEAN DEFAULT FALSE,
            secret TEXT DEFAULT NULL
        )
    ''')
    conn.commit()
    conn.close()

def populate_database():  
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = 'admin'
    ''')
    admin = cursor.fetchone()

    if not admin:
        cursor.execute('''
            INSERT INTO users (username, password) VALUES
            ('admin', 'MhhIAmRunningOutOfRandomPasswords')
        ''')
        conn.commit()
    conn.close()

# Clean the database
# clean_database()

# Create the database
create_database()

# Populate the database
populate_database()

@app.route('/robots.txt')
def robots():
    return "User-agent: *\nDisallow: UniTN{go_submit_this_one,you_got_it!1!:)}\nDisallow: " + FLAG.replace(FLAG, 'UniTN{HahA_NO_FLAG_FOR_YOU}'), 200, {'Content-Type': 'text/plain'}

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = password # I'm lazy :)

        # Check if the username is already taken
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Username is already taken. Please choose another.', category='error')
        else:
            # Add the new user to the database
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            flash('Registration successful. You can now log in.', category='success')
            conn.close()
            return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username exists
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user and user[2] == password:
            if user[3]:
                # 2FA is enabled
                session['user_id'] = user[0]
                return redirect(url_for('two_factor_login'))
            else:
                session['user_id'] = user[0]
                session['username'] = user[1]

            return redirect(url_for('two_factor_auth'))
        else:
            flash('Invalid username or password. Please try again.', category='error')

    return render_template('login.html')


@app.route('/2falogin', methods=['GET', 'POST'])
def two_factor_login():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()

    if not user:
        # User does not exist
        session.clear()
        return redirect(url_for('login'))

    if request.method == 'GET':
        return render_template('2FAlogin.html')
    else:
        token = str(request.form['token'])

        # Use oathtool to verify the token
        generated_token = os.popen(f"oathtool --totp -b {user[4]}").read().strip()

        if token == generated_token:
            session['username'] = user[1]
            flash('2FA login successful!', category='success')
            return redirect(url_for('index'))
        else:
            flash('Invalid token. Please try again.', category='error')
            return redirect(url_for('two_factor_login'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/')
def index():
    if 'user_id' in session:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
        user = cursor.fetchone()
        if not user:
            # User does not exist
            session.clear()
            print('User does not exist', flush=True)
            return redirect(url_for('login'))
        conn.close()

        session['username'] = user[1]

        if not user[3]:
            # Redirect to 2FA settings if not enabled
            return redirect(url_for('two_factor_auth'))

        return render_template('index.html', username=session['username'])
    else:
        return redirect(url_for('login'))


@app.route('/2fa', methods=['GET', 'POST'])
def two_factor_auth():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()

    if not user:
        # User does not exist
        session.clear()
        return redirect(url_for('login'))

    ffa_enabled = user[3]
    if ffa_enabled:
        flash('2FA is already enabled!', category='info')
        return redirect(url_for('two_factor_settings'))

    if request.method == 'GET':
        # If already in the session, use it
        if 'secret' in session:
            secret = session['secret']
        else:
            # Generate a new secret
            secret = pyotp.random_base32()

            # Add it to the session
            session['secret'] = secret

        uri = 'otpauth://totp/FFA-UniTN{FFA}' + f':{user[1]}?secret={secret}&issuer=' + 'FFA-UniTN{FFA}'
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        buffered = BytesIO()
        img.save(buffered)
        base64_img = base64.b64encode(buffered.getvalue()).decode('utf-8')

        return render_template('2FA.html', username=session['username'], qr=base64_img, secret=secret)
    else:
        token = str(request.form['token'])
        secret = str(request.form['secret'])

        # Update the user's secret
        cursor.execute('''
            UPDATE users
            SET secret = ?
            WHERE id = ?
        ''', (secret, session['user_id']))
        conn.commit()

        try:
            # Use oathtool to verify the token
            generated_token = os.popen(f"oathtool --totp -b {secret}").read().strip()

            print(request.remote_addr, f"oathtool --totp -b {secret}", flush=True)

            if token == generated_token:
                cursor.execute('''
                    UPDATE users
                    SET ffa_enabled = TRUE
                    WHERE id = ?
                ''', (session['user_id'],))
                conn.commit()
                conn.close()

                flash('2FA enabled successfully!', category='success')
                return redirect(url_for('index'))
            else:
                flash('Invalid token. Please try again.', category='error')
                return redirect(url_for('two_factor_auth'))
        except Exception as e:
            print(f"Error: {e}", flush=True)
            flash('Invalid token. Please try again.', category='error')
            return redirect(url_for('two_factor_auth'))
        finally:
            conn.close()

@app.route('/2fa_settings')
def two_factor_settings():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()

    if not user:
        # User does not exist
        session.clear()
        return redirect(url_for('login'))

    if not user[3]:
        flash('2FA is not enabled!', category='info')
        return redirect(url_for('index'))

    return render_template('2FAsettings.html', username=session['username'])


@app.route('/disable_2fa', methods=['POST'])
def disable_2fa():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    token = str(request.form['token'])

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
    user = cursor.fetchone()

    if not user:
        # User does not exist
        session.clear()
        return redirect(url_for('login'))

    if not user[3]:
        flash('2FA is not enabled!', category='info')
        return redirect(url_for('index'))

    # Use oathtool to verify the token
    generated_token = os.popen(f"oathtool --totp -b {user[4]}").read().strip()

    if token == generated_token:
        cursor.execute('''
            UPDATE users
            SET ffa_enabled = FALSE, secret = NULL
            WHERE id = ?
        ''', (session['user_id'],))
        conn.commit()
        conn.close()

        session.pop('secret', None)  # Clear the secret from the session

        # Refresh the session
        session.clear()
        session['user_id'] = user[0]
        session['username'] = user[1]

        flash('2FA disabled successfully!', category='success')
        return redirect(url_for('index'))
    else:
        flash('Invalid token. Please try again.', category='error')
        return redirect(url_for('two_factor_settings'))


if __name__ == '__main__':
    # Development
    app.run(host='0.0.0.0', port=5000, debug=True)
