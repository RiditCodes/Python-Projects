#tuple() function can be used to enter elements of the tuple in one line

Tuple = tuple(input("Enter the tuple elements: "))

print(Tuple)

a = 0
for i in Tuple:
    print("Tuple[%d]:"%a, i)
    a += 1