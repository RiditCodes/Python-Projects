'''
Random module is an in-built module of Python which is used
to generate random numbers.
'''

import random

list1 = [1, 2, 3, 4, 5]
#choice() prints a random value from the list
print(random.choice(list1))
print(random.random())

#Generates a random number between the range
print(random.randint(10, 20))

'''
shuffle() method is used to change the position of elements
of the sequence(list)
'''
print()
print(list1)

print("\nAfter first shuffle...")
random.shuffle(list1)
print(list1)

print("\nAfter second shuffle...")
random.shuffle(list1)
print(list1)