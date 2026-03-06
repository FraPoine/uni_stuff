import sqlite3
import subprocess

# Simulazione di una sessione utente
session = {'user_id': 1, 'username': 'testuser'}

# Simulazione di un database SQLite
DATABASE = 'test.db'

# Creazione di un database di esempio e di una tabella 'users'
def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT)')
    cursor.execute('INSERT OR IGNORE INTO users (id, username) VALUES (1, "testuser")')
    conn.commit()
    conn.close()

# Funzione per simulare la validazione degli input
def invalid(input_data):
    # Esempio di validazione: blocca input contenenti caratteri speciali
    if any(char in input_data for char in [';', '|', '&', '$', '`']):
        return True, "Input contains invalid characters"
    return False, None

# Funzione principale per inviare email
def send_mail(to, subject, message):
    # if 'user_id' in session:
    #     conn = sqlite3.connect(DATABASE)
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],))
    #     user = cursor.fetchone()
    #     if not user:
    #         # L'utente non esiste
    #         session.clear()
    #         print("User does not exist. Redirecting to login.")
    #         return
    #     conn.close()

    #     session['username'] = user[1]

        # Verifica che "to" sia un indirizzo email valido
        if '@' not in to:
            print(f'{to} is not a valid email address.')
            return

        # Validazione degli input
        invalid_message, reason = invalid(message)
        if invalid_message:
            print(f'Invalid message: {reason}')
            return {'error': 'Hacking attempt detected: invalid message.'}

        invalid_subject, reason = invalid(subject)
        if invalid_subject:
            print(f'Invalid subject: {reason}')
            return {'error': 'Hacking attempt detected: invalid subject.'}

        invalid_to, reason = invalid(to)
        if invalid_to:
            print(f'Invalid email address: {reason}')
            return {'error': 'Hacking attempt detected: invalid email address.'}

        # Comando per inviare l'email
        command = f'echo "{message}" | mail -s "{subject}" "{to}"'
        print(f'Executing command: {command}')

        try:
            returned = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, timeout=5)
        except subprocess.CalledProcessError as e:
            print(f'Failed to send email. Program exited with code {int(e.returncode)}')
            return {'error': f'Failed to send email. Program exited with code {int(e.returncode)}'}
        except subprocess.TimeoutExpired as e:
            print('Failed to send email. Timeout expired.')
            return {'error': 'Failed to send email. Timeout expired.'}
        except Exception as e:
            print('Failed to send email. Unknown error.')
            return {'error': 'Failed to send email. Unknown error.'}

        return_value = returned.returncode
        if return_value == 0:
            print('Email sent successfully.')
            return {'success': 'Email sent successfully.'}
        else:
            try:
                print(f'Failed to send email. Program exited with code {int(return_value)}')
                return {'error': f'Failed to send email. Program exited with code {int(return_value)}'}
            except Exception as e:
                print('Failed to send email and failed to flash the return code')
                return {'error': 'Failed to send email and failed to flash the return code'}
  #  else:
   #     print("User not logged in. Redirecting to login.")
    #    return

# Configura il database di esempio
#setup_database()

# Test della funzione send_mail
if __name__ == '__main__':
    # Input di esempio
    to = 'admin@admin'
    subject = 'Test Subject'
    message =  '" sleep 5 "'

    # Esegui la funzione send_mail
    result = send_mail(to, subject, message)
    print(result)