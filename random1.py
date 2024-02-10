import random

list1 = [1, 2, 3, 4, 5]

print(random.choice(list1))
print(random.random())

print(random.randint(10, 20))

print()
print(list1)
random.shuffle(list1)
print()
print(list1)