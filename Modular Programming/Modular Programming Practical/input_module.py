def get_student_data():
	running = True
	while running:
		try:
			name = input("Enter your name: ")
			score = float(input("Enter your score: "))
			return name, score
		except ValueError:
			print("Invalid input")
			running = True