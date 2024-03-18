List1 = [1, 2, 3, 4, 2, 5, 6, 4, 7]
List2 = []

print("Before removing duplicates...")
print(List1)

for i in List1:
    if i in List2:
        continue
    else:
        List2.append(i)

List1 = List2

print("After removing duplicates...")
print(List1)