import json


#61414b99be30cefb62a0e95a803760d27bfe4d5bd1d5bf6d2f08bf01ec07632c


MOD = 256 # allows generating bytes from 0 to 255

class LCG:
    def __init__(self, a: int, c: int, x0: int):    # Linear Congruential Generator
        self.a = a
        self.c = c
        self.x = x0

    def generate_byte(self) -> int: # generates a byte
        prev_x = self.x
        self.x = (self.a * self.x + self.c) % MOD
        return prev_x

with open("./data.json", "r") as f:     # load the data from the json file
    data = json.load(f)
lcg = LCG(data["a"], data["c"], data["x0"])
flag = data["flag"].encode()
assert flag.startswith(b"UniTN{")

enc_flag = bytes([c ^ lcg.generate_byte() for c in flag])
with open("message.txt", "w") as f:
    f.write(enc_flag.hex())
    
# create a script that tries for each byte to xor the encrypted flag and check if it starts with "UniTN{"
# if it does, then it will print the flag
# the script is in es4.py


    
