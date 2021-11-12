import random

class DebitCard:
	

	def withdraw(balance = random.randint(1000, 1000000)):
		pin = int(input("Input your pin: "))
		amount = int(input("Input amount: $"))
		if amount < balance:
			print(f"Collect your cash!")
		else:
			print("Withdrawal unsuccessful. Insufficient balance.")


		
	def transfer(balance = random.randint(1000, 1000000)):
		pin = int(input("Input your pin: "))
		recipient_account_number = int(input("Input recipient account number: "))
		amount = int(input("Input amount: $"))
		if amount < balance:
			print(f"Successfully transfered ${amount} to {recipient_account_number}")
			balance -= amount
			print(f"Your balance is ${balance}")
		else:
			print("Transfer unsuccessful. Insufficient balance")
	
	
	def check_balance(balance = random.randint(1000, 1000000)):
		pin = int(input("Input your pin: "))
		print(f"Your balance is ${balance}")

		
				
						
card = DebitCard


# to withdraw
#card.withdraw()

# to tranfer 
#card.transfer()

# to check balance
#card.check_balance()