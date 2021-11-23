"""
Source: https://www.expatrio.com/living-germany/learn-german/german-alphabet-and-grammar
"""

alphabet = {
	'A': 'ah',
	'B': 'bay',
	'C': 'tsay',
	'D': 'day',
	'E': 'ay',
	'F': 'eff',
	'G': 'gay',
	'H': 'hah',
	'I': 'eeh',
	'J': 'yot',
	'K': 'kah',
	'L': 'ell', 
	'M': 'em',
	'N': 'en',
	'O': 'oh',
	'P': 'pay',
	'Q': 'koo',
	'R': 'air',
	'S': 'es',
	'T': 'tay',
	'U': 'ooh',
	'V': 'fow',
	'W': 'vay',
	'X': 'iks',
	'Y': 'oopsilohn',
	'Z': 'tset',
}
print("Print out the German phonetic spelling of the letters of any 	word! \nInput 'quit', without the quotation\nto end the program")
while True:
	word = input("> ").upper()
	output = ""
	if word == 'QUIT':
			break
	try:
		for letters in word:
			code = alphabet.get(letters, letters)
			output += code + ' '
		print(output)
	except TypeError:
		print("Invalid input")
