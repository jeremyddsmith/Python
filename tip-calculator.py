print("Hello, welcome to your automatic tip calculator!")
# This line will provide you with your bill amount
bill = float(input("How much was your bill?\n"))
# here we are finding out how many ways we will be splitting the bill
guests = int(input("How many guests did you dine with today?\n"))
## We are choosing out tip amount here
percentage = int(input("What percent tip would you like to leave? 10 15 20 or custom\n"))
# Here we are going to present our final bill total and our individual contribution amount
totalbill = float((percentage / 100 * bill) + bill)
print(f"Your total bill is {totalbill: .2f}")
individual = (totalbill / guests)
print(f"Your total individual contribution is {individual: .2f}")