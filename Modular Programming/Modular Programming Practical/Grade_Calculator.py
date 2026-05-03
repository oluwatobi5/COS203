
running = True
while running:
	try:
		name = input("Enter your name: ")
		score = float(input("Enter your score: "))
		if score >= 50:
			print("Pass")
			print()
		else:
			print("Fail")
			print()
	except ValueError:
		print("Error")