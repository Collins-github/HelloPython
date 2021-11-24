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
print("""
Hi! My name is Mirabel.
I can translate words to Morse code

Input 'quit' without the quotation marks
to end the program

""")
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
