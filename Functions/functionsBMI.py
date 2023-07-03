def calc_bmi():
    weight = float(input("enter weight in kgs"))
    height = float(input("enter height in meters"))

    result = weight/(height * height)

    print( f"your BMI is {result}")
    if result <= 18:
        print("Underweight")

    elif result <= 29:
        print(" Normal weight")

    elif result <= 34:
        print("overweight")

    else:
        print("obese")

calc_bmi()