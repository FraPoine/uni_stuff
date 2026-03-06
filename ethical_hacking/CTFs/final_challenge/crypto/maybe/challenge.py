#!/usr/bin/env python3
import os
from Crypto.Util.number import bytes_to_long, getPrime

if os.path.exists("./flag.txt"):
    with open("./flag.txt", "r") as f:
        FLAG = f.read().strip()
else:
    FLAG = "UniTN{placeholder_flag}"


registered_usernames = [b"admin"]

p = getPrime(1024)
q = getPrime(1024)
n = p*q
phi = (p-1)*(q-1)
e = 65537
d = pow(e, -1, phi)


def sign(username: bytes) -> int:
    pt = bytes_to_long(username) % n
    ct = pow(pt, d, n)
    return ct


def signup():
    print("What username do you want (hex)?")
    username = bytes.fromhex(input("> "))
    if username in registered_usernames:
        print("Username already taken")
        return
    password = sign(username) % n
    print("Here is your password: " + hex(password)[2:])
    registered_usernames.append(username)


def login():
    print("Insert your username (hex)")
    username = bytes.fromhex(input("> "))
    print("Insert your password")
    password = int(input("> "), 16)

    if username in registered_usernames and sign(username) % n == password % n:
        if username == b"admin":
            print(FLAG)
        else:
            print("Logged in successfully")
    else:
        print("Wrong user or password")


print("Welcome to the central Identity Manager, your ")
print("best friend in setting up a 2FA environment!")
while True:
    print("What do you want to do?")
    print("1. Signup")
    print("2. Login")
    option = input("> ")

    if option == "1":
        signup()

    elif option == "2":
        login()

    else:
        print("Bye")
        break
