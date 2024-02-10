List = []

num = int(input("Enter the number of elements in the list: "))

for i in range(0, num):
    List.append(input("Enter the item: "))

print("\nThe list items, before removing any item are given below")

for i in List:
    print(i)

List.remove(input("\nEnter the item to be deleted: "))

print("\nThe list items after removing one item from the list are given below")

for i in List:
    print(i)