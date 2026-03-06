#!/usr/bin/env python3

# reverse_flag.py
# Script per estrarre la flag dai byte della funzione decriptata
# prerequisito: dump della memoria decriptata in decrypted.bin

from capstone import *
import sys

# modifica questi valori se cambiano
BASE_ADDR = 0x5555555552a8    # indirizzo di partenza della memoria decriptata
DUMP_FILE = "decrypted.bin"  # nome del file dumpato da GDB

# Carica il dump
with open(DUMP_FILE, "rb") as f:
    code = f.read()

# Inizializza Capstone per x86_64
md = Cs(CS_ARCH_X86, CS_MODE_64)
md.detail = True

# Dizionario offset -> byte di flag
flag_bytes = {}

# Disassembla il blocco decriptato
for ins in md.disasm(code, BASE_ADDR):
    # Cerchiamo istruzioni cmp BYTE PTR [rdi + disp], imm8
    if ins.mnemonic == "cmp" and len(ins.operands) == 2:
        op0, op1 = ins.operands
        if op0.type == X86_OP_MEM and op1.type == X86_OP_IMM:
            mem = op0.mem
            # controlla che il base register sia RDI
            if mem.base == X86_REG_RDI:
                offset = mem.disp
                imm = op1.imm & 0xFF
                flag_bytes[offset] = imm

# Ricostruisci la stringa della flag
if not flag_bytes:
    print("Nessuna istruzione cmp trovata. Controlla BASE_ADDR e il contenuto di decrypted.bin.")
    sys.exit(1)

max_off = max(flag_bytes.keys())
result = bytearray(max_off + 1)
for off, val in flag_bytes.items():
    result[off] = val

# Rimuove eventuali terminatori null e stampa
flag = result.rstrip(b'\x00').decode('ascii', errors='ignore')
print("Flag decifrata:", flag)
