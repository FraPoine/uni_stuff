from Crypto.Util.number import long_to_bytes
from math import gcd

e = 65537

print("c_flag:")
c_flag = int(input("> "))

#!
print("c1:")
c1 = int(input("> "))

#"
print("c2:")
c2 = int(input("> "))

term1 = pow(33, e) - c1
term2 = pow(34, e) - c2



# N
N = gcd(term1, term2)

print("N = ", N)

# Ciphertext modificato
c_prime = (c_flag * pow(2, e, int(N))) % int(N)

print("\n Decrypt this:")
print(c_prime)

print("\nDecrypted message:")
decrypted = int(input("> "))

# Messaggio originale
original_m = decrypted // 2
#print("\nmessaggio numerico: ",original_m)
flag = long_to_bytes(original_m)
print("\nFLAG HEX:", flag.hex())
print("\n FLAG (raw bytes):", flag)
print("FLAG (as string):", flag.decode(errors="ignore"))
