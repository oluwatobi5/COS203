def get_student_data():
	name = input("Enter your name: ")
	score = float(input("Enter your score: "))
	return name, score

def calculate_grade(score):
	if score >= 50:
			grade = "Pass"
			return grade
	else:
			grade = "Fail"
			return grade
			
def display_result(name, score, grade):
	print()
	print("Name:" + name)
	print(f"Score: {score}")
	print(f"Grade: {grade}")
	
student_name, student_score = get_student_data()
final_grade = calculate_grade(student_score)
display_result(student_name, student_score, final_grade)

