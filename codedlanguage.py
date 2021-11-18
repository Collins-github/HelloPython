alphabet = {
	'A': 'x',
	'B': 'x'*2,
	'C': 'x'*3,
	'D': 'x'*4,
	'E': 'x'*5,
	'F': 'x'*6,
	'G': 'x'*7,
	'H': 'x'*8,
	'I': 'x'*9,
	'J': 'x'*10,
	'K': 'x'*11,
	'L': 'x'*12, 
	'M': 'x'*13,
	'N': 'x'*14,
	'O': 'x'*15,
	'P': 'x'*16,
	'Q': 'x'*17,
	'R': 'x'*18,
	'S': 'x'*19,
	'T': 'x'*20,
	'U': 'x'*21,
	'V': 'x'*22,
	'W': 'x'*23,
	'X': 'x'*24,
	'Y': 'x'*25,
	'Z': 'x'*26,
	' ': ' - '
}
print("You get to print any word , in 'x codes'!\ninput 'quit', without the quotation\nto end the program")
while True:
	word = input("> ").upper()
	output = ""
	try:
		for letters in word:
			code = alphabet.get(letters)
			output += code + ' '
		print(output)
		if word == 'quit':
			break
	except TypeError:
		print("Invalid input")