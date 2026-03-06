#!/usr/bin/env python3


"""
'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC77z0O+9EzA4x19edRBYuYftmApPoDLSjGLhHN3aCsyh41onmo\nx104YNjrl1qSSkTZpDduVTlLFET7/7G5ht2cWvWHNsUCuh/IJC93kCkNwYXiq17I\nEp/ikXITL9hSejMXlS4A2g9Lru5H8zDS8/jdolCesgXo/PoYGT6dDazAVwIDAQAB\nAoGANcMOuIaZJfrR57zc23S2pn1DQ2Xuj5IPpAHx3e6U1FlNoxJDs2C07jfmVh8K\nLedJIumzYcDHjw7RXTWcZfKK2n4fioJfwoJHG/fhyajAK7Re/t7Ampsj8m1t54YX\ngtbtHZv7x9WdHkxofW0f8sQMpdvhZuOqkg41Su7jf2RA+IECQQDSTirOwwVgTZMD\nMUA59KfQOMrg17Fcr+3g42HX7lLgYSotF9QztaNaESGsJW6gAQ65OTX63bOZ8e2l\nUMvPjMJRAkEA5MS8yG8pSp1qLYgNyqCzqIL1MX3y4k7O0d7cVCiUS6kemnsq8AS5\n1+lp7bkxCmdsesVVT6JCRC5UO+lAuUlGJwJAHnwuQGKMuPUFxoSxJrWMTeatogIi\nN6lY9ix/1mk5okTzdC3sGMLPtxKcqvOSIaeFltvwMzlH+5zSMhCQOrnQwQJBAJfM\nkDQzxuNzBsSFthkRf4U+uLKJj4RppMUQK4VQk+6MnvkE553ylNrXUGnk68yqigoB\nLTW1RmF1mIFUqpUIMRsCQAyNgT38zxTzqGJ3xPoCkUkShYQOKs8/kR9WJ4qfp+71\nRAvOne+kQOEThWlMfFMp6Cdh6giT6Yi9T7Peg/Q5v3E=\n-----END RSA PRIVATE KEY-----'

b'-----BEGIN RSA PRIVATE KEY-----\nMIICWwIBAAKBgQDIHsvorg3zVcNjpdACiiWFM27FJnCEYlhclsUPXQ60Xfm6s6Rw\nVhV9/smZ051ivH9mMZooFKFpdaij2hBBYS5FStdqVNOYX4BUX8nTrsUYH58Q3Pq5\n1kqNi7VUD2oNwNJx1moWEBeiRhAkf28IchIYLGrTX1AGE+Ek3zhop4L3DwIDAQAB\nAoGARxe5tNVwm0uSeCoFtYFCRwm4hk1bl4wge/QL2aNjf+wKtarv9gB+7h2/nOgy\nd0sjrzhb3XVGymJEIMFtGOzfNJlnvn2Y6AZszp/pjeT2IYKgRyR/ufvmkn0/X1C9\nM1xJhXAc86/XOra4omQ4qQXhRVd8fsUq90CuXztnaDjyN2ECQQDTNYZy1B9UcgPP\nbyuPGZlCH37lEfYA4o61tVO9EGwckiffFopLH5PvFwXj0xFGeksR5Myb2nzjo+2e\n5Pyd5TsXAkEA8o9DxZeGPsrKQWdTaGUHy90Z+cTZFM0E125TOjhV6M9jkWSGgTnT\nYbvn3LxYTLVjUULzSHFrPYEECUC2Kog+yQJAPopk62+gb1LrierzTQZZeVj2LEJr\nQ8vSUkAFMcDBIpysrcRw4tnQ5kU8+z8uqF3iCMRlSekifg22eQx5OQ/9tQJAQoQv\nHZxz3/xUgqMHKHWsMaesW+YzcZTXYwyKHkkcpf9ZWqGqkP1+jiqtZsbvn/mOBtbJ\nSHBx7CfZJ4BrdDZwoQJANdtG5e/ZAjGoMgC44UQxDtZNUnPADIh+lWiJiaS7lAXa\nTzZDbcWLxrvlPbUflNmzI3Y0TUqPPWM5jAUz+dtRYA==\n-----END RSA PRIVATE KEY-----'
"""

import os

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long


FLAG = os.getenv("FLAG")
if not FLAG:
    FLAG = "UniTN{placeholder_flag}"

rsa = RSA.generate(1024)

def encrypt(m):
    return pow(m, rsa.e, rsa.n)


def decrypt(c):
    return pow(c, rsa.d, rsa.n)


def protect():
    print("Enter your secret:")
    secret = input("> ")
    secret = bytes_to_long(secret.encode())
    print("Encrypting your secret...")
    encrypted = encrypt(secret)
    print("Here is your encrypted secret:", encrypted)


def show():
    print("Enter the encrypted secret:")
    encrypted = int(input("> "))
    print("Decrypting your secret...")
    decrypted = decrypt(encrypted)
    if decrypted == bytes_to_long(FLAG.encode()):
        print("Keep your hands off my secret!")
    else:
        print("Here is your secret:", decrypted)
        print("Due to budget cuts it is in numerical form.")

def main():
    print("Do you want to know my biggest secret?")
    print("Here it is:", encrypt(bytes_to_long(FLAG.encode())))
    print("I encrypted it using RSA so that you can see it, but you can't decrypt it.")
    print("Using my service you can do the same for your secrets.")
    print("Since I can't afford to store this data, take the public key with you.", rsa.export_key())

    print("What do you want to do?")
    while True:
        print("1. Protect a secret")
        print("2. Decrypt a secret")
        option = input("> ")

        if option == "1":
            protect()
        elif option == "2":
            show()
        else:
            print("Invalid option, try again.")
            import sys
            sys.exit(0)

if __name__ == "__main__":
    main()