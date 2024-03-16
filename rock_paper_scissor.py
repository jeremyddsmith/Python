import random
## First we will set our variables that we will be working with
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_integer = random.randint(0, 2)

print("Let's play Rock, Paper, Scissors! Will you beat the computer?!")

computer_choice = random_integer
player_choice = int(input("Rock, Paper, Scissors, SHOOT! Type '0' for Rock. Type '1' for paper. Type '2' for Scissor.\n"))

if player_choice == 0:
    print(f"{rock}\n You chose rock.")
    
    if computer_choice == 0:
        print(f"Your opponent chose rock as well! It's a tie.\n {rock}")
    if computer_choice == 1:
        print(f"Your opponent chose paper. You lose, try again.\n {paper}")
    if computer_choice == 2:
        print(f"Your opponent chose scissors. You win!\n {scissors}\n Please play again.")

if player_choice == 1:
    print(f"{paper}\n You chose paper.")
    
    if computer_choice == 0:
        print(f"Your opponent chose rock. You win!\n {rock}\n Please play again!")
    if computer_choice == 1:
        print(f"Your opponent chose paper as well! It's a tie. Please play again.\n {paper}")
    if computer_choice == 2:
        print(f"Your opponent chose scissors. You lose. Please try again.\n {scissors}")

if player_choice == 2:
    print(f"{scissors}\n You chose scissors.")
    
    if computer_choice == 0:
        print(f"Your opponent chose rock. You lose. Please try again.\n {rock}")
    if computer_choice == 1:
        print(f"Your opponent chose paper. You win!\n {paper}\n Please play again.")
    if computer_choice == 2:
        print(f"Your opponent chose scissors as well! It's a tie. Please play again.\n {scissors}")

else:
    print("Please make a selection from the list.")


