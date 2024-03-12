print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to The Cave of Dreams.")
print("Your mission is to find the solution to all your dreams.")
print("Every choice will be marked by quotation marks for ease of transition. Good luck.")
## This project is to showcase if statements with conditional operators, nested statements, and logical operators.

choice1 = input("You wake up in a cold dark room. Do you 'check the window' or 'go downstairs'?\n").lower()
if choice1 == "check the window":
    choice2 = input("You hear a loud bang and see three cloaked men running acrossed the field. You go downstairs and see that your house has been ransacked.\n Do you 'grab your sword' and chase after them? Or do you 'stay and tidy' up your house?\n").lower()

else:
    print("You come down the stairs and see three cloaked men ransacking your house. They hear you and rush you. You've died, please try again.")

if choice2 == "grab your sword":
    choice3 = input("You get outside to see the cloaked figures disappear into a cave acrossed the field. Do you chase them or stay?\n").lower()
    
else:
    print("You begin to clean up when you hear the basement door open. There was one more person in the basement that you did not hear. You are too far from your sword to defend yourself. You have died, please try again.")


    


