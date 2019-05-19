def find_highest_score(input1):
	character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
	score = 0
	key = ''
	decrypt = b''
	for val in range(128):
		xor_trail = b''
		for b1 in input1:
			xor_trail += (bytes([b1^val]))
		scoretemp = sum([character_frequencies.get(chr(byte), 0) for byte in xor_trail.lower()])
		if score < scoretemp:
			score = scoretemp
			key = str(val)
			decrypt = xor_trail
	#print(str(score) + ":" + key)
	return score, decrypt

if __name__ == "__main__":
	

	input1 = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
	print(input1)
	find_highest_score(input1)