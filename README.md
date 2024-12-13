#.......... ROCK  *  PAPER  *  SCISSORS ..........

import random
user_choice = int(input("Enter your choice:0 for rock,1 for paper,2 for scissors-\n"))

if user_choice >= 3 or user_choice< 0:
    print("your input is wrong. you lose")

else:
 computer_choice = random.randint(0,2)
 print("computer choose:-")
 print(computer_choice)
 if user_choice == computer_choice:
    print("it's a draw")
 elif user_choice == 2 and computer_choice == 0:
    print("you lose")
 elif user_choice == 0 and computer_choice == 2:
    print("you win")
 elif user_choice < computer_choice:
    print("you lose")
 elif computer_choice < user_choice:
    print("you win")
 print("Enjoy The Game")
