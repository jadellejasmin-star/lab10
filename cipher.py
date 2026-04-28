import sys

shift = int(sys.argv[1])

text = sys.stdin.read().upper()

result = []

for char in text:
    if 'A' <= char <= 'Z':
        shifted = chr(((ord(char) - 65 + shift) % 26) + 65)
        result.append(shifted)

encoded = "".join(result)

# print in blocks of 5 letters, 10 blocks per line
for i in range(0, len(encoded), 50):
    chunk = encoded[i:i+50]
    print(" ".join(chunk[j:j+5] for j in range(0, len(chunk), 5)))
