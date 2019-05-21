from base64 import b64decode
from Crypto.Cipher import AES

with open("7.txt","r") as f:
	cipher=b64decode(f.read())

key = "YELLOW SUBMARINE"
key_obj = AES.new(key, AES.MODE_ECB)
plaintext = key_obj.decrypt(cipher)
print(plaintext)
