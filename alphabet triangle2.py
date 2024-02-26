rows = int(input("Enter the no. of rows you want: "))

for r in range(0, rows):
    for n in range(0, rows-r):
        print("j", end=" ")
    print("\r")