List = [2, 3, 2, 4, 5, 6, 4, 5, 7]

List1 = []

for i in List:
    if i not in List1:
        List1.append(i)

print(List1)