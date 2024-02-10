rows = int(input("Enter the number of rows you want in star triangle: "))
for r in range(rows, -1, -1):
    for n in range(r+1, 1, -1):
        print("*",end= " ")
    print("\r")
