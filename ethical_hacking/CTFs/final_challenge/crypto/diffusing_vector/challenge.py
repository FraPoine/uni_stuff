#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

if os.path.exists("./flag.txt"):
    with open("./flag.txt", "r") as f:
        FLAG = f.read().strip()
else:
    FLAG = "UniTN{placeholder_flag}"

BLOCK_SIZE = 16
KEY = os.urandom(BLOCK_SIZE)


def encrypt(plaintext: bytes) -> bytes:
    assert len(plaintext) % BLOCK_SIZE == 0
    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

def decrypt(ciphertext: bytes) -> bytes:
    assert len(ciphertext) % BLOCK_SIZE == 0
    cipher = AES.new(KEY, AES.MODE_CBC, KEY)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext


print("Hello")
print("Let me encrypt files for you!")
while True:
    print("What do you want to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Login as admin")
    option = input("> ")

    if option == "1":
        print("Insert the secret to encrypt (hex, multiple of 16 bytes)")
        plaintext = bytes.fromhex(input("> "))
        ciphertext = encrypt(plaintext).hex()
        print("Here you are, no need to worry about leaking data anymore: " + ciphertext)

    elif option == "2":
        print("Insert the data to decrypt (hex, multiple of 16 bytes)")
        ciphertext = bytes.fromhex(input("> "))
        plaintext = decrypt(ciphertext).hex()
        print("Here you are, keep it safe: " + plaintext)

    elif option == "3":
        print("Insert the admin password (hex)")
        key = bytes.fromhex(input("> "))
        if key == KEY:
            print("Welcome back!")
            print(FLAG)
        else:
            print("Hacker detected!")
            break

    else:
        print("Bye")
        break
