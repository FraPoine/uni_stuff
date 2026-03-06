target = [
    0xaa, 0xf6, 0xb6, 0x75, 0xf1, 0xe7, 0xdd, 0x63, 0x0b, 0x65,
    0x1a, 0x56, 0x7c, 0xf7, 0x66, 0xf7, 0x8b, 0xe5, 0xec, 0xb7,
    0xe0, 0x63, 0xfb, 0x85, 0x3a, 0x17, 0x2f, 0x83, 0x5b, 0x46,
    0x6b, 0xe3, 0xcf, 0xf6, 0xa2
]

def reverse_transform(data):
    result = []
    for i in range(len(data)):
        # Invert Transform A: XOR with index << 4
        val = data[i] ^ (i << 4 & 0xFF)

        # Invert Transform B
        if i % 2 == 0:
            val = ~val & 0xFF  # bitwise NOT and mask to 8-bit
        else:
            # swap nibbles again (auto-inverse)
            val = ((val >> 4) | (val << 4)) & 0xFF

        result.append(val)
    return bytes(result)

original = reverse_transform(target)
print("Recovered input:", original)
print("As string (if printable):", original.decode('utf-8', errors='replace'))