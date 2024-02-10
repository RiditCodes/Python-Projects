import random

while True:
    choices = [1, 2, 3]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = int(input("Enter 1 for Rock, 2 for Paper and 3 for Scissors: "))

    #Tie
    if player == computer:
        print("\nTie!")

    #Win or Lose

    #Player = rock
    if player == 1:
        if computer == 2:
            print(f"Computer: Paper")
            print(f"Player: Rock")
            print("\nComputer wins! Try again")
        elif computer == 3:
            print(f"Computer: Scissors")
            print(f"Player: Rock")
            print("\nYou win!")

    #Player = paper
    elif player == 2:
        if computer == 3:
            print(f"Computer: Scissors")
            print(f"Player: Paper")
            print("\nComputer wins! Try again")
        elif computer == 1:
            print(f"Computer: Rock")
            print(f"Player: Paper")
            print("\nYou win!")

    #Player = scissors
    elif player == 3:
        if computer == 1:
            print(f"Computer: Rock")
            print(f"Player: Scissors")
            print("\nComputer wins! Try again")
        if computer == 2:
            print(f"Computer: Paper")
            print(f"Player: Scissors")
            print("\nYou win!")

    play_again = input("Play again?: ")
    if play_again == "no":
        exit()
    else:
        pass