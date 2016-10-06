#Rock Paper Scissors
#Rules: Rock crushes Scissors, Paper covers Rock, Scissors cuts Paper, rock crushes lizard, lizard poisons spock, spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves spock, spock vaporizes rock.

import random

def rps():
    computer_choice = random.randint(1,5)
    if computer_choice == 1:
        computer_choice_rock()
    elif computer_choice == 2:
        computer_choice_paper()
    elif computer_choice == 3:
        computer_choice_scissors()
    elif computer_choice == 4:
        computer_choice_lizard()
    elif computer_choice == 5:
        computer_choice_spock()

def computer_choice_rock():
    user_choice = str(input("Press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard and 5 for spock: "))
    if user_choice == "1":
        print("The game is tied! You both chose rock.")
        try_again()
    if user_choice == "2":
        print("You win! You chose paper and the computer chose rock.")
        one_more_round()
    if user_choice == "3":
        print("You lose! You chose scissors and the computer chose rock.")
        try_again()
    if user_choice == "4":
        print("You lose! You chose lizard and the computer chose rock.")
        try_again()
    if user_choice == "5":
        print("You win! You chose spock and the computer chose rock.")
        one_more_round()
    else:
        print("Try again")
        computer_choice_rock()

def computer_choice_paper():
    user_choice = str(input("Press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard and 5 for spock: "))
    if user_choice == "1":
        print("You lose!. You chose rock and the computer chose paper.")
        try_again()
    if user_choice == "2":
        print("The game is tied! You both chose paper.")
        try_again()
    if user_choice == "3":
        print("You win! You chose scissors and the computer chose paper.")
        one_more_round()
    if user_choice == "4":
        print("You win You chose lizard and the computer chose paper.")
        one_more_round()
    if user_choice == "5":
        print("You lose! You chose spock and the computer chose paper.")
        try_again()
    else:
        print("Try again")
        computer_choice_paper()

def computer_choice_scissors():
    user_choice = str(input("Press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard and 5 for spock: "))
    if user_choice == "1":
        print("You win! You chose rock and the computer chose scissors.")
        one_more_round()
    if user_choice == "2":
        print("You lose! You chose paper and the computer chose scissors.")
        try_again()
    if user_choice == "3":
        print("The game is tied! You both chose scissors.")
        try_again()
    if user_choice == "4":
        print("You lose! You chose lizard and the computer chose scissors.")
        try_again()
    if user_choice == "5":
        print("You win! You chose spock and the computer chose scissors.")
        one_more_round()
    else:
        print("Try again")
        computer_choice_scissors()

def computer_choice_lizard():
    user_choice = str(input("Press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard and 5 for spock: "))
    if user_choice == "1":
        print("You win! You chose rock and the computer chose lizard.")
        one_more_round()
    if user_choice == "2":
        print("You lose! You chose paper and the computer chose lizard.")
    if user_choice == "3":
        print("You win! You chose scissors and the computer chose lizard.")
        one_more_round()
    if user_choice == "4":
        print("The game is tied! You both chose lizard.")
        try_again()
    if user_choice == "5":
        print("You lose! You chose spock and the computer chose lizard.")
        try_again()
    else:
        print("Try again")
        computer_choice_rock()

def computer_choice_spock():
    user_choice = str(input("Press 1 for rock, 2 for paper, 3 for scissors, 4 for lizard and 5 for spock: "))
    if user_choice == "1":
        print("You lose! You chose rock and the computer chose spock.")
        try_again()
    if user_choice == "2":
        print("You win! You chose paper and the computer chose spock.")
        one_more_round()
    if user_choice == "3":
        print("You lose! You chose scissors and the computer chose spock.")
        try_again()
    if user_choice == "4":
        print("You win! You chose lizard and the computer chose spock.")
        one_more_round()
    if user_choice == "5":
        print("The game is tied! You both chose spock.")
        try_again()
    else:
        print("Try again")
        computer_choice_rock()

def try_again():
    choice = input("Do you want to try it again? Yes or No?")
    if choice == "Yes" or choice == "yes":
        rps()
    elif choice == "No" or choice == "no":
        print("Thank you for playing rock, papers, scissors, lizard, spock!")
        quit()

def one_more_round():
    choice = input("Do you want to do another round? Yes or No?")
    if choice == "Yes" or choice == "yes":
        rps()
    elif choice == "No" or choice == "no":
        print("Thank you for playing rock, papaers, scissors, lizard, spock!")
        quit()

rps()
