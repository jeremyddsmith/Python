#This calculator will tell you if the entered year is a leap year. This showcases the functionality of if and nested if statements.
print("Welcome to your Leap Year Calculator!")

#Creates our variable for the calculation. We specify that we want to receive the number as an integer and not a string
year = int(input("What year would you like to check?\n"))

#This calculation checks the year by making sure the number is evenly divisible by four, but is not evenly divisible by 4, unless it is evenly divisible by 400
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")