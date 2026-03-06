
byte_string = b"61414b99be30cefb62a0e95a803760d27bfe4d5bd1d5bf6d2f08bf01ec07632c"

for i in range(256):
    xored = bytes([i ^ byte for byte in byte_string])
    if xored.startswith(b"UniTN{"):
        print(xored.decode())
        break