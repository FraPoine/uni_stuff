#!/usr/bin/env python3

__author__ = 'golim'

from flask import Flask, render_template, send_file, request, redirect, url_for, session, flash
from datetime import datetime

import urllib.parse
import sqlite3
import logging
import random
import os

if os.path.exists('flag.txt'):
    with open('flag.txt', 'r') as f:
        FLAG = f.read().strip()
else:
    FLAG = 'UniTN{placeholder_flag}'

app = Flask(__name__)

app.secret_key = 'd03a2ab540e8aacf18bbafc12c4f1569'

DATABASE = 'database.db'

CARDS = [
    '1.png',
    '2.png',
    '3.png',
    '4.png',
    '5.png',
    '6.png',
    '7.png',
    '8.png',
    '9.png',
    '10.png',
    '11.png',
    '12.png',
    '13.png',
    '14.png',
    '15.png',
]

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            last_opened DATETIME DEFAULT (datetime('now', '-2 minutes'))
        )
    ''')
    conn.commit()
    conn.close()

def populate_database():  
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    # Add the admin user if it does not exist
    cursor.execute('''
        SELECT * FROM users WHERE username = 'admin'
    ''')
    admin = cursor.fetchone()

    if not admin:
        cursor.execute('''
            INSERT INTO users (username, password) VALUES (?, ?)
        ''', ('admin', os.environ['FLAG'] if 'FLAG' in os.environ else 'password'))
        conn.commit()
    conn.commit()
    conn.close()

# Create the database
create_database()

# Populate the database
populate_database()

@app.route('/robots.txt')
def robots():
    return "UUUhhh, I don't like robots. Please go away..\nBut first, get a free flag: " + FLAG                                                                                                     .replace(FLAG, 'UniTN{robots_are_not_welcome_here}')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = password

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

        if user and user[2] == password:
            # Login successful, set session variables
            session['user_id'] = user[0]
            session['username'] = user[1]
            session['last_card_creation'] = user[3]
            conn.close()

            if user[1] == 'admin':
                # Give the admin all the cards
                session['cards'] = CARDS

            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', category='error')

    return render_template('login.html')

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

        cards = session.get('cards', [])

        return render_template('index.html', username=session['username'], cards=cards, last_card_creation=session.get('last_card_creation', None))
    else:
        return redirect(url_for('login'))


@app.route('/newcard', methods=['GET', 'POST'])
def newcard():
    if 'user_id' not in session:
        flash('You must be logged in to create a new card.', category='error')
        return redirect(url_for('login'))
    
    # Refresh the session from the database
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
    session['last_card_creation'] = user[3]  # Update last opened time

    # Check if 2 minutes have passed since the last card creation
    remaining_seconds = 0
    if 'last_card_creation' in session:
        last_card_creation = session['last_card_creation']
        if isinstance(last_card_creation, str):
            try:
                last_card_creation = datetime.fromisoformat(last_card_creation)
            except ValueError:
                last_card_creation = datetime.strptime(last_card_creation, "%Y-%m-%d %H:%M:%S")
        
        time_diff = (datetime.now() - last_card_creation).total_seconds()
        remaining_seconds = max(0, 120 - time_diff)
        
        if time_diff < 120:
            # If less than 2 minutes have passed, do not allow creating a new card
            if request.method == 'GET':
                # If it's a GET request, redirect to the new card page
                return render_template('newcard.html', 
                                     last_card_creation=last_card_creation, 
                                     username=session.get('username', ''),
                                     remaining_seconds=int(remaining_seconds))
            else:
                # If it's a POST request, redirect to the index page
                flash('You can only create a new card every 2 minutes.', category='error')
                return redirect(url_for('index'))
    if request.method == 'POST':
        # Get the cards owned by the user
        cards = session.get('cards', [])

        # Pick a random card from the available cards that the user does not own
        available_cards = [card for card in CARDS if card not in cards]
        if not available_cards:
            flash('You have already collected all the cards!', category='error')
            return redirect(url_for('index'))

        # Save the new card in the session
        new_card = random.choice(available_cards)
        cards.append(new_card)
        session['cards'] = cards
        session['last_card_creation'] = datetime.now()

        # Update the user's last opened time in the database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET last_opened = ? WHERE id = ?', (session['last_card_creation'], session['user_id']))
        conn.commit()
        conn.close()

        # Flash a success message
        flash('New card created successfully!', category='success')
        return redirect(url_for('index'))

    return render_template('newcard.html', 
                         last_card_creation=session.get('last_card_creation', None), 
                         username=session.get('username', ''),
                         remaining_seconds=0)

@app.route('/card')
def card():
    '''
    Return the card image for the user, but only if they own it.
    '''
    if 'user_id' not in session:
        flash('You must be logged in to view your cards.', category='error')
        return redirect(url_for('login'))

    print(request.remote_addr, session, flush=True)

    # Refresh the session from the database
    cards = session.get('cards', [])

    card_name = request.args.get('name', '')
    if card_name not in cards:
        flash('You do not own this card.', category='error')
        return 'You do not own this card.', 403

    card_path = os.path.join('images', card_name)

    if not os.path.exists(card_path):
        flash('Card image not found.', category='error')
        return 'Card image not found', 404

    return send_file(card_path, mimetype='image/png')


if __name__ == '__main__':
    # Development
    app.run(host='0.0.0.0', port=5000, debug=True)
