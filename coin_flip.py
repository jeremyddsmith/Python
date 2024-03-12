import random

print("It's time to let fate decide who is right with a good old fashioned coin flip!")

game = input("Are you ready to start? Yes or No\n").lower()

if game == "yes":
    random_integer = random.randint(1, 1000)
    if random_integer % 2 == 0:
        print("Your coin flipped to heads.")
    else:
        print("Your coin flipped to tails.")
else:
    print("Okay, come back when you are ready to play.")
    