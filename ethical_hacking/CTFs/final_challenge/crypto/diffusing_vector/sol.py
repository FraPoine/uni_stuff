from pwn import *

HOST = 'cyberchallenge.disi.unitn.it'
PORT = 10030

r = remote(HOST, PORT)


# 1) Encrypt 16 zero byte per ottenere C0
r.recvuntil(b'> ')
r.sendline(b'1')                      # scelta Encrypt
r.recvuntil(b'> ')
r.sendline(b'00' * 16)                # 16 byte zero
r.recvuntil(b'anymore: ')
C0_hex = r.recvline().strip()         # ricevi il ciphertext esadecimale
C0 = bytes.fromhex(C0_hex.decode())

# 2) Decrypt C0||C0
r.recvuntil(b'> ')
r.sendline(b'2')                      # scelta Decrypt
r.recvuntil(b'> ')
r.sendline((C0 + C0).hex().encode())  # due volte C0
r.recvuntil(b'safe: ')
out = r.recvline().strip()            # plaintext esadecimale
plaintext = bytes.fromhex(out.decode())
P0, P1 = plaintext[:16], plaintext[16:32]

# 3) Recover KEY = (P0 ⊕ P1) ⊕ C0
KEY = xor(xor(P0, P1), C0)
print(f"[+] Recovered KEY: {KEY.hex()}")

# 4) Login as admin
r.recvuntil(b'> ')
r.sendline(b'3')              
r.recvuntil(b'> ')
r.sendline(KEY.hex().encode())

# 5) Stampa la flag
print(r.recvall().decode())
