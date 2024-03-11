print("Welcome to your BMI Calculator. Please enjoy.")
# 1st input: enter height in meters e.g: 1.65
height = float(input("Please enter your height in meters.\n"))
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input("Please enter your weight in kilograms.\n"))

# This will provide your bmi amount
bmi = weight / (height * height)

#This set of "if" statements will give your answer to the question.
if bmi < 18.5:
    print(f"You BMI is {bmi:.1f}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.1f}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.1f}, you are slightly overweight.")
elif bmi >= 30:
    print(f"Your BMI is {bmi:.1f}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi:.1f}, you are clinically obese.")