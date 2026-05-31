from student_utils import 

students = [
    Student("Alice",99),
    Student("Mike",88),
    Student("John",69),
    Student("Kim",49),
    Student("Fums",10),
]

for student in students:
    print(student)

print(get_failures(students))
