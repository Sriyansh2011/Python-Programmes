height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight / (height/100)**2

if BMI <= 18.4:
    print("You are Underweight")
elif BMI <= 24.9:
    print("You are Healthy")
elif BMI <= 29.9:
    print("You are Overweight")
elif BMI <= 34.4:
    print("You are severely Overweight")
elif BMI <= 39.9:
    print("You are Obese")
else:
    print("You are severely obese.")