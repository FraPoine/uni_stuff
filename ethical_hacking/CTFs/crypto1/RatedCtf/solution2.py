import pwn
#conn = pwn.remote('cyberchallenge.disi.unitn.it', 50101)
# modified_c1 = original_c1 XOR (original_plaintext XOR desired_plaintext)
"""
Iv
pet=BillTheRock|
pet=Ferris|pet=r
ubberduck|pet=te
rristheprillPAAD

Iv
pet=BillTheRock|
pet=rubberduck|p (et=Ferris|) 9 char
et=Ferris|pet=te
rristheprillPAAD

Iv
pet=BillTheRock|
pet=rubberduck|p 
et=Ferris|pet=te
rristheprillPAAD

delta1 = bytes([0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
c1_modified = xor(c1, delta1)

delta2 = bytes([0x00, 0x00, 0x00, 0x16, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
c2_modified = xor(c2, delta2)

73 dd 2f cb 60 b7 d8 ab f0 77 e3 eb 76 34 45 65     Iv
18 4b b3 8d 91 60 1b 40 e5 2c 17 75 43 da 94 86     pet=BillTheRock|
61 e2 80 50 05 62 e0 8b 0b 49 1b 1c c9 e0 e2 11     pet=Perris|pet=b
1a 9c 7d d2 ba 69 92 81 fe e8 89 60 34 21 56 76     ubberduck|pet=te
53 e9 a0 96 bc ac 17 9b e3 83 79 ba 11 b2 f8 4a     rristheprillPAAD

legal characters = abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .,;?!'"

AAAAAAAAAAAAwpet;PerriswAAAAAAAAAAAAAAAAAAAA
bubberduck


af45840d6e6f116a6e5136f0a9a5036a    IV                  
8f0b3e34fd1d476821f45818bddb15ad    pet=BillTheRock|    c1
79c18fb5766009657e5e6f9a7d286c23    pet=AAAAAAAAAAAA    c2
83beda8a297e388221027f085f238aac    wpet;PerriswAAAA    c3
3db87b3201679de8cd422b9de7d67881    AAAAAAAAAAAAAAAA    c4
595ab992599e91b77c3f5126b85ba8ec    |pet=bubberduck|    c5
b7cd8726a6da7300076f2ebcb17e7cf6    pet=terristhepri    c6
c718198c5080bcf4c591c8bd623214d3    llPAAAAAAAAAAAAD    c7


7698d4a85bd14b532b1bb72261b639bc    V       IV
7698d4a85bd14b532b1bb72261b639bc    V

bdf1310a0ab5609dfec1bcd2460fe145    V       c1
bdf1310a0ab5609dfec1bcd2460fe145    V


52 72 c0 d5 7f c5 a6 f8 74 72 f4 1a ed 63 06 d2            c2
55 67 d1 9c 02 f0 b1 f8 6f 68 fb 2c ed 63 06 e3

d30ec50c510cceea18402dcede5b9a55    V       c3
d30ec50c510cceea18402dcede5b9a55    V

0dd40a89ce174ea71f9bb011402c72fe    V       c4
0dd40a89ce174ea71f9bb011402c72fe    V

5c cd 2d bd 1f 93 a4 87 aa 6b 9a 57 f7 41 cd e5            c5
0d d4 0a 89 ce 07 4e a7 1f 9b b0 11 40 2c 72 fe

c18a5b8f57f4cb2841a4fef31a858907    V       c6
c18a5b8f57f4cb2841a4fef31a858907    V

7ccb6eccd28cf234fe881d948abd64c6    V       c7
7ccb6eccd28cf234fe881d948abd64c6    V
"""   

conn = pwn.process("./codiceCtf.py")

conn.sendline(b"1")
conn.sendline(b"Perris")
conn.sendline(b"bubberduck")
conn.recvuntil(b"it: ")
#
full_ciphertext = conn.recvall()

print("testo cifrato ricevuto: \n",full_ciphertext)


#full_ciphertext = bytes.fromhex("a3fbaf32121f83177c8ee8cef7ef2e1c9ba3c2e7847ad1af313f56987b17ef14a1af6c3b0365018d12c3c48a345789f3b4470be6fe3d5ab54f64130eddafdb5b475dbb9e102a3910fbada382c9c19ad0446d66d6d3914d3d5c2ce981ec995fd3e2d8616051475b8e3afef8f95c8dcb904bcd501d9ce73fef9ce69982b185c79a")

#print(f"Ciphertext originale: {full_ciphertext.hex()}")

iv = full_ciphertext[:16]
c1 = full_ciphertext[16:32]
c2 = full_ciphertext[32:48]
c3 = full_ciphertext[48:64]
c4 = full_ciphertext[64:80]
c5 = full_ciphertext[80:96]
c6 = full_ciphertext[96:112]
c7 = full_ciphertext[112:128]


# Calcola la modifica
original_c3 = b"wpet;PerriswAAAA"
desired_c3 = b"|pet=Ferris|AAAA"
delta_c3 = pwn.xor(original_c3, desired_c3)

original_c5 = b"|pet=bubberduck|"
desired_c5 = b"|pet=rubberduck|"
delta_c5 = pwn.xor(original_c5, desired_c5)

c2_modified = pwn.xor(c2, delta_c3)
c4_modified = pwn.xor(c4, delta_c5)

# Ricostruisci il ciphertext
modified_ciphertext = iv + c1 + c2_modified + c3 + c4_modified + c5 + c6 + c7
print("Nuovo ciphelast):\n'rtext:", modified_ciphertext.hex())

"""
conn.sendline(b"2")
conn.recvuntil(b"Insert your encrypted zoo (hex)\n")
conn.sendline(modified_ciphertext)

ress = conn.recvall()
print(ress)
"""