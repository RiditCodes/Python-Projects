import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper or Scissors?: ").lower()

    #Tie
    if player == computer:
        print(f"Computer: {computer}")
        print(f"Player: {player}")
        print("\nTie!")

    #Win or Lose

    #Player = rock
    if player == "rock":
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("\nComputer wins! Try again")
        elif computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("\nYou win!")

    #Player = paper
    elif player == "paper":
        if computer == "scissors":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("\nComputer wins! Try again")
        elif computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("\nYou win!")

    #Player = scissors
    elif player == "scissors":
        if computer == "rock":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("\nComputer wins! Try again")
        if computer == "paper":
            print(f"Computer: {computer}")
            print(f"Player: {player}")
            print("\nYou win!")

    play_again = input("Play again?: ").lower()
    if play_again == "no":
        exit()
    else:
        pass