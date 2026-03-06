#!/usr/bin/env python3
from pwn import remote

HOST = "cyberchallenge.disi.unitn.it"
PORT = 10060

def signup(r, username_hex: str) -> int:
    r.recvuntil("What do you want to do?")
    r.sendline("1")
    r.recvuntil("hex)?")
    r.sendline(username_hex)
    line = r.recvline_contains("Here is your password:")
    pw_hex = line.strip().split(b":")[1].strip()
    return int(pw_hex, 16)

def login(r, username_hex: str, password_int: int):
    r.recvuntil("What do you want to do?")
    r.sendline("2")
    r.recvuntil("username (hex)")
    r.sendline(username_hex)
    r.recvuntil("password")
    r.sendline(hex(password_int)[2:])
    return r.recvuntil("}").decode()

def main():
    r = remote(HOST, PORT)

    # 1) firma di x = b"\x02"
    sx = signup(r, "02")

    # 2) firma di y = b"\x30\xb26\xb4\xb7"
    sy = signup(r, "30b236b4b7")

    # 3) password per admin
    pw_admin = sx * sy

    # 4) login e stampa flag
    resp = login(r, "61646d696e", pw_admin)
    print(resp)

if __name__ == "__main__":
    main()
