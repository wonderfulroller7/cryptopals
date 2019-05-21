from collections import defaultdict
from base64 import b64decode

def repetitions(cipher, block_length=16):
    reps = defaultdict(lambda: -1)
    for i in range(0, len(cipher), block_length):
        block = bytes(cipher[i:i + block_length])
        reps[block] += 1
    return sum(reps.values())

cipher_with_ecb = None
highest_repetitions = 0

# The ciphertext is provided in a file named 8.txt
with open("8.txt","r") as f:
    for line in f:
        no_of_reps = repetitions(bytearray(b64decode(line)))
        if no_of_reps >= highest_repetitions:
            highest_repetitions = no_of_reps
            cipher_with_ecb = line

print(cipher_with_ecb)