from Crypto.Util.number import long_to_bytes
import math

n, e, c = open("message.txt").readlines()
n, e, c = int(n), int(e), int(c)

p = q = math.isqrt(n)
while True:
    if p * q == n:
        break
    p -= 1 # decrease p gradually ...
    while p*q < n:
        q += 1 # ... while keeping p*q as close as possible to n

# no need to implement modular inverse, python stdlib takes care of it!
d = pow(e, -1, (p-1)*(q-1))
m = pow(c, d, n)
print(long_to_bytes(m))