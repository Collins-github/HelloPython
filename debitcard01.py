class DebitCard:		

						
	def pin():
		pin = ""
		while pin != range(1000, 10000):
			pin = int(input("Input pin: "))
			if pin < 1000:
				print("Invalid pin. Too short!")
			elif pin > 9999:
				print("Invalid pin. Too long!")
			else:
				return pin
				break
				
			
			
	def amount():
		amount = int(input("Input amount: "))
		return amount
		
	def balance():
		import random
			
		balance = random.randint(1000, 100000)
		return balance
	
	def recipient_account_number():
		recipient_account_number = ""
		while recipient_account_number != range(1000000000, 10000000000):
			recipient_account_number = int(input("Input recipient account number: "))
			if recipient_account_number < 1000000000:
				print("Invalid account number. Too short!")
			elif recipient_account_number > 9999999999:
				print("Invalid account number. Too long!")
			else:
				return recipient_account_number
				break

		
	def withdraw():
		DebitCard.pin()
		amount = DebitCard.amount()
		balance = DebitCard.balance() 	
		if amount < balance:
			print(f"Collect your cash!")
		else:
			print("Withdrawal unsuccessful. Insufficient balance.")
		print(balance)
			
			
	def transfer():
		DebitCard.pin()
		recipient_account_number = DebitCard.recipient_account_number()
		amount = DebitCard.amount()
		balance = DebitCard.balance()
		if amount < balance:
			print(f"Successfully transfered ${amount} to {recipient_account_number}")
			balance -= amount
			print(f"Your balance is ${balance}")
		else:
			print("Transfer unsuccessful. Insufficient balance")
		print(balance)
	

		
	def check_balance():
		DebitCard.pin()
		balance = DebitCard.balance()
		print(f"Your balance is ${balance}")

		
				
						
card = DebitCard

#to withdraw
#card.withdraw()

#to transfer
card.transfer()

# to check balance
#card.check_balance()
