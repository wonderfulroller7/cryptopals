import sys

def hamming_distance(string1, string2):
	difference = 0
	xor_bytes = b''
	for b1, b2 in zip(string1, string2):
		xor_bytes += (bytes([b1 ^ b2]))
	binary_val = bin(int.from_bytes(xor_bytes, byteorder=sys.byteorder))
	difference = binary_val.count("1")
	return difference
	

b1 = b"this is a test"
b2 = b"wokka wokka!!!"

val = hamming_distance(b1, b2)
print(val)