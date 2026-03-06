from Crypto.Util.number import long_to_bytes
import math

n, e, c = open("message.txt").readlines()
n, e, c = int(n), int(e), int(c)

def integer_root(c: int, e: int) -> int:
    """Returns the integer e-th root of c, or None if the e-th root is not an integer"""
    if e == 1:
        return c
    elif e == 2:
        v = math.isqrt(c)
        if v*v == c:
            return v
        else:
            return None

    # binary search to find the root
    a = 0
    b = math.isqrt(c)
    while True:
        m = (a+b) // 2
        v = pow(m, e)
        if v == c:
            return m
        elif v > c:
            assert(b != m)
            b = m
        else:
            if a == m:
                assert(b - a <= 1)
                return None
            a = m

m = integer_root(c, e)
print(long_to_bytes(m))