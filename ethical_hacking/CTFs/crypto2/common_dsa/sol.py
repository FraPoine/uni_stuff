from pwn import *
from hashlib import sha256
from Crypto.Util.number import bytes_to_long

HOST = "cyberchallenge.disi.unitn.it"
PORT = 10503

p = 13232376895198612407547930718267435757728527029623408872245156039757713029036368719146452186041204237350521785240337048752071462798273003935646236777459223
q = 857393771208094202104259627990318636601332086981
g = 5421644057436475141609648488325705128047428394380474376834667300766108262613900542681289080713724597310673074119355136085795982097390670890367185141189796

r = remote(HOST, PORT)

m1 = b"message" 
m2 = b"egassem"

r.sendlineafter(b"> ", b"1")
r.sendlineafter(b": ", m1.hex().encode())
r1 = int(r.recvline().decode().split(": ")[1])
s1 = int(r.recvline().decode().split(": ")[1])


r.sendlineafter(b"> ", b"1")
r.sendlineafter(b": ", m2.hex().encode())
r2 = int(r.recvline().decode().split(": ")[1])
s2 = int(r.recvline().decode().split(": ")[1])


#cosa serve sta cosa?
h1 = bytes_to_long(sha256(m1).digest()) % q
h2 = bytes_to_long(sha256(m2).digest()) % q

#non ho capito nulla di ste robe
assert r1 == r2
k = (h1 - h2) * pow(s1 - s2, -1, q) % q
d = (k * s1 - h1) * pow(r1, -1, q) % q

def dsa(m, k):
    h = bytes_to_long(sha256(m).digest()) % q
    r0 = pow(g, k, p) % q
    inverse_k = pow(k, -1, q)
    s = (h + d*r0)*inverse_k % q
    return r0, s

m = b"get_flag"
r0, s = dsa(m, k)

r.sendlineafter(b"> ", b'2')
r.sendlineafter(b": ", m.hex().encode())
r.sendlineafter(b": ", str(r0).encode())
r.sendlineafter(b": ", str(s).encode())
print(r.recvline(keepends=False))
