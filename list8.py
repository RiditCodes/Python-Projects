List1 = [1, 2, 3, 4, 5]
List2 = [1, 2, 3, 4, 5, 4]

print("The list items are given below before removing any item---")

for i in List1:
    print(i)

print("\n")

for i in List2:
    print(i)

List1.remove(3)
List2.remove(4)

print("After removing the item, the list items are given below---")

for i in List1:
    print(i)

print("\n")    

for i in List2:
    print(i)