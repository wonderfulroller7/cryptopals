import codecs

def convert_hex_to_base64(hex):
	return codecs.encode(codecs.decode(hex,'hex'),'base64').decode()

def convert_base64_to_hex(b64):
	return codecs.encode(codecs.decode(b64,'base64'),'hex').decode()

if __name__ == "__main__":
	b64 = convert_hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
	print(b64)