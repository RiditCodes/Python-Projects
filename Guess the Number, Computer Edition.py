import random
num_list = []
guess_num = int(input("What is the number you want the computer to guess?: "))
range_num = int(input(f"Enter the range of the numbers, should be bigger than {guess_num}: "))
#Anti-cheat 1
if range_num < guess_num:
    print("Sorry, you are trying to cheat.Cheaters are not allowed to play!")
    exit()

def Guess(f, x):
    for i in range(0, x+1):
        num_list.append(i)
    
    while True:
        num = random.randrange(0, x)
        response = input(f"Is {num} your number? Y for yes, N for no: ")
        if response == "N":
            num_list.remove(num)
            continue
        elif num !=  f and response == "Y":
            print("Do you remember your number correctly? I think you need to see a doctor.")
            exit()
        elif num == f and response == "Y":
            print(f"Yay! The computer guessed your number,{f},correctly! Now, time to take over the world!")
            exit()
    

Guess(guess_num, range_num)