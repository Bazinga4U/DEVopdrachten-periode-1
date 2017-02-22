#Rock Paper Scissors
#Rules: Rock crushes Scissors, Paper covers Rock, Scissors cuts Paper.

import random

def rps():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    elif computer_choice == 3:
        computer_choice_scissors()

def computer_choice_rock():
    user_choice = str(input("Press 1 for rock, 2 for paper and 3 for scissors: "))
    if user_choice == "1":
        print("The game is tied! You both chose rock.")
        try_again()
    if user_choice == "2":
        print("You win! You chose paper and the computer chose rock.")
        one_more_round()
    if user_choice == "3":
        print("You lose! You chose scissors and the computer chose rock.")
        try_again()
    else:
        print("Try again")
        computer_choice_rock()

def computer_choice_paper():
    user_choice = str(input("Press 1 for rock, 2 for paper and 3 for scissors: "))
    if user_choice == "1":
        print("You lose!. You chose rock and the computer chose paper.")
        try_again()
    if user_choice == "2":
        print("The game is tied! You both chose paper.")
        try_again()
    if user_choice == "3":
        print("You win! You chose scissors and the computer chose paper.")
        one_more_round()
    else:
        print("Try again")
        computer_choice_paper()

def computer_choice_scissors():
    user_choice = str(input("Press 1 for rock, 2 for paper and 3 for scissors: "))
    if user_choice == "1":
        print("You win! You chose rock and the computer chose scissors.")
        one_more_round()
    if user_choice == "2":
        print("You lose! You chose paper and the computer chose scissors.")
        try_again()
    if user_choice == "3":
        print("The game is tied! You both chose scissors.")
        try_again()
    else:
        print("Try again")
        computer_choice_scissors()

def try_again():
    choice = input("Do you want to try it again? Yes or No?")
    if choice == "Yes" or choice == "yes":
        rps()
    elif choice == "No" or choice == "no":
        print("Thank you for playing rock, papers, scissors!")
        quit()

def one_more_round():
    choice = input("Do you want to do another round? Yes or No?")
    if choice == "Yes" or choice == "yes":
        rps()
    elif choice == "No" or choice == "no":
        print("Thank you for playing rock, papaers, scissors, lizard, spock!")
        quit()

rps()
