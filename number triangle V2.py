rows = int(input("Enter the number of rows in your number triangle: "))
num = 1
for r in range(0, rows):
    for n in range(0,r+1):
        print(num,end= " ")
    print("\r")
    num += 1
