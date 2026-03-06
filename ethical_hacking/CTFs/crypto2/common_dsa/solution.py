import pwn
from hashlib import sha256
from Crypto.Util.number import bytes_to_long

p = 13232376895198612407547930718267435757728527029623408872245156039757713029036368719146452186041204237350521785240337048752071462798273003935646236777459223
q = 857393771208094202104259627990318636601332086981
g = 5421644057436475141609648488325705128047428394380474376834667300766108262613900542681289080713724597310673074119355136085795982097390670890367185141189796

#chall = pwn.process(["python", "challenge.py"])
chall = pwn.remote("cyberchallenge.disi.unitn.it", 10503)

m1 = b"ciao"
m2 = b"boh"

chall.sendlineafter(b"> ", b'1')
chall.sendlineafter(b": ", m1.hex().encode())
r1 = int(chall.recvline().decode().split(": ")[1])
s1 = int(chall.recvline().decode().split(": ")[1])

chall.sendlineafter(b"> ", b'1')
chall.sendlineafter(b": ", m2.hex().encode())
r2 = int(chall.recvline().decode().split(": ")[1])
s2 = int(chall.recvline().decode().split(": ")[1])

h1 = bytes_to_long(sha256(m1).digest()) % q
h2 = bytes_to_long(sha256(m2).digest()) % q

assert r1 == r2
k = (h1 - h2) * pow(s1 - s2, -1, q) % q
d = (k * s1 - h1) * pow(r1, -1, q) % q

def dsa(m, k):
    h = bytes_to_long(sha256(m).digest()) % q
    r = pow(g, k, p) % q
    inverse_k = pow(k, -1, q)
    s = (h + d*r)*inverse_k % q
    return r, s

m = b"get_flag"
r, s = dsa(m, k)

chall.sendlineafter(b"> ", b'2')
chall.sendlineafter(b": ", m.hex().encode())
chall.sendlineafter(b": ", str(r).encode())
chall.sendlineafter(b": ", str(s).encode())
print(chall.recvline(keepends=False))

