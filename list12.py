List1 = [8, 4, 3, 5, 0]
List2 = [6, 2, 9, 4, 8, 7]
List3 = []
List4 = [8, 10, 6, 5]

for i in List1:
    if i in List2 and i in List4:
        List3.append(i)

print(List3)