rows = int(input("Enter the number of rows you want: "))
space = rows - 1
for r in range(0, rows):
    for n in range(0, space):
        print(end= " ")
    space -= 1
    for n in range(0, r+1):
        print("*",end= " ")
    print("\r")
    
