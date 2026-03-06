import sys

# 1) parametri
infile  = 'bin_rated'      # il tuo ELF originale
outbin  = 'raw_section.bin'
start   = 0x12a8           # file-offset di inizio
end     = 0x15fe           # file-offset di fine (esclusivo opzionale)

# 2) leggi e scrivi
with open(infile, 'rb') as f:
    f.seek(start)
    data = f.read(end - start)

with open(outbin, 'wb') as f:
    f.write(data)

print(f'Written {len(data)} bytes to {outbin}')