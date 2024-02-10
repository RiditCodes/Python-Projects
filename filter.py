list1 = [5,6,7,9,10]

list2 = list(filter(lambda a : a%2 != 1, list1))

print(list2)