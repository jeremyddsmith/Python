print("Welcome to the love connection calculator! Is it true love? Or would you truly love to find someone else.")

#Gather the names
name1 = input("What is the first name?\n")
name1b = name1.lower()
name2 = input("What is the second name?\n")
name2b = name2.lower()

#count the number of times each letter in love and true occur in the two names.
truelove = (f"{name1b } + {name2b}")
t = int(truelove.count("t"))
r = int(truelove.count("r"))
u = int(truelove.count("u"))
e = int(truelove.count("e"))
first_digit = t + r + u + e

l = int(truelove.count("l"))
o = int(truelove.count("o"))
v = int(truelove.count("v"))
e = int(truelove.count("e"))
second_digit = l + o + v + e
total = int(str(first_digit) + str(second_digit))

if total < 10 or total > 90:
    print("You go together like coke and mentos!")
elif total > 40 and total < 50:
    print("Your love is alright.")
else:
    print("You don't want to know.")






