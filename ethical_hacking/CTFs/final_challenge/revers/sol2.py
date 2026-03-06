#!/usr/bin/env python3
from pwn import remote
import ctypes
import sys

# Carica la libc per accedere a srand() e rand()
libc = ctypes.CDLL("libc.so.6")

def rand_pass(seed: int, length: int = 16):
    """
    Genera due password (prima e seconda) esattamente come fa il tuo programma C:
      - usa srand(seed)
      - chiama rand()%0x5e + '!' per ogni carattere
      - continua il flusso di rand() tra la prima e la seconda pass
    """
    # Inizializza il generatore con il PID candidato
    libc.srand(ctypes.c_uint(seed))
    # genera la prima password
    p1 = ''.join(
        chr((libc.rand() % 0x5e) + ord('!'))
        for _ in range(length)
    )
    # genera la seconda password
    p2 = ''.join(
        chr((libc.rand() % 0x5e) + ord('!'))
        for _ in range(length)
    )
    return p1, p2

def main():
    fake = "U>o&D~I!f^hPz>o}"
    # Proviamo i PID più comuni (adatta il range se serve)
    for pid in range(1000, 65536):
        p1, p2 = rand_pass(pid)
        if p1 == fake:
            print(f"[+] Trovato seed (PID) = {pid}")
            print(f"[+] Password corretta da inserire prima che te la dica: {p2}")
            sys.exit(0)
    print("[-] Seed non trovato nel range dato. Prova a estenderlo.")

if __name__ == "__main__":
    main()
