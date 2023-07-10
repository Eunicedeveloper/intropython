from database import Student

students = Student.select()

#use forloop to display

for student in students:
    print(student.name, student.phone, student.age, student.gender, student.studentcode)
