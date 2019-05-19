from prob2_fixed_xor import xor_2_bytes

import codecs

line = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

key = b'ICE'*len(line)
print("key = ")
print(key)
ciphertext = xor_2_bytes(line, key)
print(ciphertext)