Tuple = tuple(input("Enter the tuple elements: "))

print(Tuple)

a = 0

for i in Tuple:
    print("Tuple[%d]: "%a, i)
    a += 1