from database import Student

try:
    n = input("enter name\n")
    p = input("enter phone number\n")
    a = input("enter age\n")
    g = input("gender\n")
    c = input("student code\n")

    Student.create(name=n, phone=p, age=a,gender=g,studentcode=c)
    print("user created successfully")

except:
    print("failed to create user")
