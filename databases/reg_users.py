from database import User

try:
    jina = input("enter name\n")
    arafa = input("enter email\n")
    siri = input("enter password\n")

    User.create(name=jina, email=arafa, password=siri)
    print("User created successfully")

except:
    print("failed to create user")
