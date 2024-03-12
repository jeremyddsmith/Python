print("Thank you for choosing Jeremy's Python Pizza Deliveries!")

bill = 0
size = input("What size pizza do you want? S, M, L\n") 
if size == "S":
    bill += 15
    print(f"A small pizza is ${bill}.")
elif size == "M":
    bill += 20
    print(f"A medium pizza is ${bill}.")
else:
    bill += 25
    print(f"A large pizza is ${bill}.")

add_pepperoni = input("Would you like to add pepperoni? This is $2 extra. Y or N\n")
if add_pepperoni == "Y":
    bill += 2
    print(f"Your bill is now ${bill}")
else:
    print(f"No pepperoni. Your bill is currently ${bill}")



extra_cheese = input("Would you like to extra cheese? Extra cheese is $1. Y or N\n")
if extra_cheese == "Y":
    bill += 1
    print(f"Your final bill is ${bill}. Thank you for choosing Jeremy's Python Pizza.")
else:
    print(f"Your final bill is ${bill}. Thank you for choosing Jeremy's Python Pizza.")
