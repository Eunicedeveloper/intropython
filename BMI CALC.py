#enable user to enter input

weight = input("enter weight in kgs")
height = input(" enter height in meters")


weight = float(weight)
height = float(height)

#the result is your BMI

result = weight/float(height * height)


if result <= 18:
    print("Underweight")

elif result >=18.1:
    print(" Normal weight")

elif result >=29.1:
    print("overweight")

else:
    print("obese")







