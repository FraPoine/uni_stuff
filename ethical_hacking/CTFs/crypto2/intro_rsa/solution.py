#!/usr/bin/env python3
import pwn
from Crypto.Util.number import long_to_bytes, bytes_to_long


#r = pwn.process(["python", "challenge.py"])
r = pwn.remote("cyberchallenge.disi.unitn.it", 10500)

def read_bytes() -> str:
    r.recvuntil(b": ")
    return r.recvline(keepends=False)

def read_int() -> int:
    return int(read_bytes())

def send_int(v: int):
    r.sendlineafter(b"? ", str(v).encode())


message = read_bytes()
print(message)
m = bytes_to_long(message)
print(m)
send_int(m)


p = read_int()
q = read_int()
n = p*q
send_int(n)
phi = (p-1)*(q-1)
send_int(phi)

e = 65537
d = pow(e, -1, phi)
send_int(d)
c = pow(m, e, n)
send_int(c)

enc_flag = read_int()
dec_flag = pow(enc_flag, d, n)
flag = long_to_bytes(dec_flag)
print(flag)