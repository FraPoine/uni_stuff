from pwn import *

# 1) Carica il binario originario
orig = ELF('./bin_rated')

# 2) Leggi la sezione mysec
start = 0x001012a8
size  = 0x001015fe - start
blob  = orig.read(start, size)

# 3) Crea un ELF in memoria a partire dal blob
new = ELF.from_bytes(blob, vma=start)

# 4) Salva su disco
new.save('flag_section.elf')