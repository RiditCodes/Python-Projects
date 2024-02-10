from words import words
import random

def get_random_word(words): 
    num_of_words = int(input("Enter the number of words you want: "))
    while num_of_words > 0: 
        word = random.choice(words)
        num_of_words -= 1
        print(word)

get_random_word(words)

    
