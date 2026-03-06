from pwn import *
import string

charset = string.ascii_letters + string.digits + '{}_'
host = 'cyberchallenge.disi.unitn.it'
port = 10000

prefix = ''
while True:
    max_time = 0
    next_char = ''
    for c in charset:
        guess = prefix + c
        conn = remote(host, port)
        conn.recvuntil(b'Insert flag:')
        conn.sendline(guess.encode())
        result = conn.recvline().decode()
        conn.close()

        try:
            cycles = int(result.strip().split()[-3])
            print(f"Trying {guess}: {cycles} cycles")
            if cycles > max_time:
                max_time = cycles
                next_char = c
        except:
            continue

    prefix += next_char
    print(f"[+] Current guess: {prefix}")