
import string

"""
1d8e319d2be1ccd94580fec3754bbd64f8eb36853ee86f978da78ec9c98bbce7fa9b43ff07d30c3e82de82974f1edf6d4af26dcfdb4c13878b18f05946a13e11e4fcea6eb30014a8b87b65ec6fe5a0990e2b7b5157a09c4294851c68ad90dfd50d6bd55c85846714334fbf2699cb14dda44b1721b9884a819fc82441c075cd23505e62572e2087817d1d74c84191f57282f7674240b66d6fc8f00e2d93f182b92162d936db44a10e4c8451e8a8e0212abceb1921fafd0fb5449a9ebaa83770d6df65c2e64c37449eae8d1e445ecf7870c874a056122353d4e1b36ef9844a2d5ce33e8750cba259d0808413a8c056f247

BLOCK_SIZE = 16
key = os.urandom(BLOCK_SIZE)
cipher = AES.new(key, AES.MODE_ECB)

def encrypt(m: bytes) -> bytes:
    # a bit of encoding to make hackerz more confused
    for _ in range(3):
        m = m.hex().encode("utf-8")
    m = pad(m, BLOCK_SIZE)
    return cipher.encrypt(m)
    

the message is split in blocks of 16 bytes and encrypted with AES in ECB mode

we can brute force the flag by 
starting with the encripted text 

"""
