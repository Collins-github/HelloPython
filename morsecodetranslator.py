"""
Source: https://en.m.wikipedia.org/wiki/Morse_code

"""

alphabet = {
	'A': '•–',
	'B': '–•••',
	'C': '–•–•',
	'D': '–••',
	'E': '•',
	'F': '••–•',
	'G': '––•',
	'H': '••••',
	'I': '••',
	'J': '•–––',
	'K': '–•–',
	'L': '•–••', 
	'M': '––',
	'N': '–•',
	'O': '–––',
	'P': '•––•',
	'Q': '––•–',
	'R': '•–•',
	'S': '•••',
	'T': '–',
	'U': '••–',
	'V': '•••–',
	'W': '•––',
	'X': '–••–',
	'Y': '–•––',
	'Z': '––••',
}
print("Print out the German phonetic spelling of the letters of any 	word! \nInput 'quit', without the quotation\nto end the program")
while True:
	word = input("> ").upper()
	output = ""
	if word == "QUIT":
		break
	try:
		for letters in word:
			code = alphabet.get(letters, letters)
			output += code + ' '
		print(output)
	except TypeError:
		print("Invalid input")