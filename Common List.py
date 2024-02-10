List1 = [1, 8, 3, 10, 5, 6]

List2 = [6, 7, 3, 1, 9, 8]

List3 = []

for i in List1:
    if i in List2:
        List3.append(i)

print(List3)