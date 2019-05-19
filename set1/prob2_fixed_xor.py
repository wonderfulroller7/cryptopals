def xor_2_bytes(input1,input2):
	xor_bytes = b''
	for b1, b2 in zip(input1, input2):
		xor_bytes += (bytes([b1 ^ b2])) 
	print(xor_bytes)
	return xor_bytes.hex()

if __name__ == "__main__":
	byte_string1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
	byte_string2 = bytes.fromhex('686974207468652062756c6c277320657965')
	print(byte_string1)
	print(byte_string2)
	print(xor_2_bytes(byte_string1,byte_string2))