import random as r
import time

possible_actions = ["Rock", "Paper", "Scissors"]

computer_action = possible_actions[r.randint(0,2)]



def rps_game():
    player_input = input("Rock, Paper, or Scissors?\n")
    time.sleep(1)
    print("Computer picked", computer_action)
    print( )
    print("Result:")
    if player_input == "Rock" or "Paper" or "Scissors":
        if player_input == computer_action:
            print("Tie!")
        elif player_input == "Rock":
            if computer_action == "Paper":
                print("You Lose!", "Paper beats Rock")
            else:
                print("You win!")
        elif player_input == "Paper":
            if computer_action == "Scissors":
                print("You Lose!", "Scissors beat Paper")
            else:
                print("You Win!")
        elif player_input == "Scissors":
            if computer_action == "Rock":
                print("You Lose!", "Rock beats Scissors")
            else:
                print("You Win!")
        else:
            print("Invalid input, please type Rock, Paper or Scissors!")

rps_game()
