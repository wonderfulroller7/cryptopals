from prob1_hex_to_base64 import convert_base64_to_hex
from base64 import b64decode
'''
cipher_text = "".join(list(open("7.txt", "r")))
cipher_text = convert_base64_to_hex(cipher_text)
print(cipher_text)
'''
with open("7.txt","r") as f:
	cipher=b64decode(f.read())

print(cipher)
