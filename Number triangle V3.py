rows = int(input("Enter the number of rows you want: "))
for n in range(rows):
    for r in range(n+1, rows+1):
        print(r, end = " ")
    print("\r")