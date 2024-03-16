print("Welcome to who's paying the bill! Let's get started.")

import random 
#This creates the name list we will be appending
names = []

#This provides the opportunity to add the names to the list. This also will adjust the syntax for clarity.
input_names = input("Who is potentially paying for this bill? Enter each name seperated by a comma and space.\n")
names.extend([name.strip() for name in input_names.split(",")])

#This step will give us the number of names in the list
num_names = len(names)

#this command will give us a random number that will decide who the person paying is
random_choice = random.randint(0, num_names - 1)

#here we will use this random number to identify which name alligns with the produced number.
paying = names[random_choice]

print(paying + " has to pay today! Gottem.")


