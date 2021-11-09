action = ""
is_started = False
ever_started = False

while True:
	action = input(">").lower()
	
	if ever_started == False:
		if action == "stop":
			print("car was never started")
		else:
			ever_started  = True
			
	if action == "help":
		print("""
start - to start the car
stop - to stop the car
quit - to end the game
	""")
	
	elif action == "start":
	   		if is_started:
	   			print("Car has already started!")
	   		else:
	   			is_started = True
	   			print("Car has started")
	   			
	elif action == "stop":
	   		if ever_started:
	   			if not is_started:
	   				print("Car has already stopped!")
	   			else:
	   				is_started = False
	   				print("Car has stopped")
	   				
	elif action == "quit":
		print("Game over")
		break
		
	else:
		print("Invalid input!")