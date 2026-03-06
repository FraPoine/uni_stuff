
import os
import pwn
from Crypto.Cipher import AES
from Crypto.Hash import MD5

conn = pwn.remote('cyberchallenge.disi.unitn.it', 10003)

conn.recvuntil(b"(hex): ")  #leggi fino a ": "
key =  bytes.fromhex(conn.recvline(keepends=False).decode()) #mi tengo la chiave in formato esadecimale come bytes
conn.recvuntil(b"(hex): ") #leggi fino a ": "
msg = bytes.fromhex(conn.recvline(keepends=False).decode()) #mi tengo il testo in formato esadecimale come bytes


aes = AES.new(key, AES.MODE_ECB)
encrypted = aes.encrypt(msg) #cifro il messaggio con la chiave
conn.sendlineafter(b"? ", encrypted.hex().encode()) #mando il messaggio cifrato in formato esadecimale

md5 = MD5.new(msg)  #calcolo l'md5 del messaggio (hash)
conn.sendlineafter(b"? ", md5.hexdigest().encode()) #mando l'md5 del messaggio in formato esadecimale

flag = conn.recvline() #dato che l'op è giusta ottengo il flag
print(flag)
conn.close()
