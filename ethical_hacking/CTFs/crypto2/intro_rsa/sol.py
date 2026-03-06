from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 10500
e = 65537

r = remote(HOST, PORT)

r.recvuntil(b": ")
message = r.recvline(keepends = False)
print(message)
m = bytes_to_long(message)
print(m)
r.sendlineafter(b"? ", str(m).encode())

r.recvuntil(b"First prime: ")
p = int(r.recvline(keepends = False))

r.recvuntil(b"Second prime: ")
q = int(r.recvline(keepends = False))

n = p*q
#print(n)
r.sendlineafter(b"? ", str(n).encode())

phin = (p-1)*(q-1)
r.sendlineafter(b"? ", str(phin).encode())

d = pow(e, -1, phin)
r.sendlineafter(b"? ", str(d).encode())

c = pow(m, e, n)
r.sendlineafter(b"? ", str(c).encode())

r.recvuntil(b"for you: ")
flag_encrypted = int(r.recvline(keepends = False))
# c = m^e (mod n)
# m = c^d (mod n)
flag = pow(flag_encrypted, d, n)
flag = long_to_bytes(flag)
print(flag)
