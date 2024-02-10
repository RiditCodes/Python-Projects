rows = int(input("Enter the number of rows you want: "))
for r in range(0, rows):
    for n in range(0, r+1):
        print("*",end= " ")
    print("\r")
