from prob3_ingle_byte_xor import find_highest_score

with open('hex_encrypt.txt','r') as f:
    for line in f:
    	score, val = find_highest_score(bytes.fromhex(line))
    	#if score > 2:
    	if score > 2.0:
    		print(val)