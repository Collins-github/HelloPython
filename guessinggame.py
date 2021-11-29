import random
while True:
	print('''
Try to guess a number between 0 and 9.
		
Hint: 
'Too hot!' means your guess was greater than the secret number. 
'Too cold!' means it was lesser than the secret number.
''')
		
	secret_number = random.randint(0,9)
	available_guesses = 3
		
	while available_guesses != 0:
			try:
				guess = int(input("Guess the secret number: "))
				available_guesses -= 1
				if guess == secret_number:
					print("You guessed the number. You win!")
					break
				elif guess < secret_number:
					print("Too cold!")
				elif guess > secret_number:
					print("Too hot!")
			except ValueError:
				print("Wrong Input!")
	else:
		print("You are out of guesses. You lose!")
		print(f"The secret number was {secret_number}")
	print("\nWould you like to play again?(yes/no)")
	if not input("> ").lower().startswith("y"):
		break
print("Thanks for playing!")
