import random
num_list = []
range_num = int(input("What is the highest number you want to guess to?: "))

def Guess(f):
    for n in range(0, f+1):
        num_list.append(n)
    num = random.choice(num_list)
    player_guess = int(input(f"Enter a number between 0 and {f}: "))
    while player_guess != num:
        if player_guess < num:
            print("Sorry, your number is too low.")
        elif player_guess > num:
            print("Sorry, your number is too high.")
        player_guess = int(input(f"Enter a guess between 0 and {f}: "))

    print(f"Yay, you guessed the number, {num}, correctly!!")

Guess(range_num)
    
