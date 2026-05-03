import input_module
import logic_module
import output_module

student_name, student_score = input_module.get_student_data()
final_grade = logic_module.calculate_grade(student_score)
output_module.display_result(student_name, student_score, final_grade)
