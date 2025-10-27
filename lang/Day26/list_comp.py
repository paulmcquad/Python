# List Comprehension

numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]

name = "Angela"
letters_list = [letter for letter in name]

range_list = [num * 2 for num in range(1, 5)]

#new_item for item in list if test
#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)
