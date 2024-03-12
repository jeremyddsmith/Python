print("Welcome to the love connection calculator! Is it true love? Or would you truly love to find someone else.")

#Gather the names
name1 = input("What is the first name?\n")
name1b = name1.lower()
name2 = input("What is the second name?\n")
name2b = name2.lower()

#count the number of times each letter in love and true occur in the two names.
truelove = (f"{name1b } + {name2b}")
tcount = int(truelove.count("t"))
rcount = int(truelove.count("r"))
ucount = int(truelove.count("u"))
ecount = int(truelove.count("e"))
lcount = int(truelove.count("l"))
ocount = int(truelove.count("o"))
vcount = int(truelove.count("v"))
ecount2 = int(truelove.count("e"))

total = tcount + rcount + ucount + ucount + ecount + lcount + ocount + vcount + ecount2

if total < 10 or total > 90:
    print("You go together like coke and mentos!")
elif total > 40 and total < 50:
    print("Your love is alright.")
else:
    print("You don't want to know.")






