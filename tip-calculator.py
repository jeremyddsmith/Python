print("Hello, welcome to your automatic tip calculator!")
# This line will provide you with your bill amount
bill = input("How much was your bill?\n")
billint = int(bill)
# here we are finding out how many ways we will be splitting the bill
guests = input("How many guests did you dine with today?\n")
guestint = int(guests)
## We are choosing out tip amount here
percentage = input("What percent tip would you like to leave? 10 15 20\n")
percentint = int(percentage)
# Here we are going to present our final bill total and our individual contribution amount
totalbill = ((percentint / 100 * billint) + billint)
print(f"Your total bill is {totalbill: .2f}")
individual = (totalbill / guestint)
print(f"Your total individual contribution is {individual: .2f}")