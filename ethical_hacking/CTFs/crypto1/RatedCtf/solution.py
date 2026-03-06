import pwn
#conn = pwn.remote('cyberchallenge.disi.unitn.it', 50100)
# modified_c1 = original_c1 XOR (original_plaintext XOR desired_plaintext)

conn = pwn.process("./codiceCtf.py")

#Perris
#bubberduck
full_ciphertext = bytes.fromhex("56a91837482ac819e5bb138197779af73687aa23472dbf2fa481336c20069e3e6125f742973cf783e43295a2dd7893e3")
print(f"Ciphertext originale: {full_ciphertext.hex()}")

iv = full_ciphertext[:16]
print("IV:", iv.hex())
c1 = full_ciphertext[16:32]
#print("c1:", c1.hex())
c2 = full_ciphertext[32:]
#print("c2:", c2.hex())

# Calcola la modifica
original = b"pet=Perris|pet=b"
desired = b"pet=Ferris|pet=r"
delta = pwn.xor(original, desired)
# Modifica il secondo blocco (secondi 16 byte)
iv_modified = pwn.xor(iv, delta)
print("Iv:", iv_modified.hex())

# Ricostruisci il ciphertext
modified_ciphertext = iv_modified + c1 + c2
print("Nuovo ciphertext:", modified_ciphertext.hex())