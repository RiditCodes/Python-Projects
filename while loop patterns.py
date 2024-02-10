rows = int(input("Enter the number of rows you want: "))
a = 0
b = 1
while a <= rows:
    b = 1
    while b <= a:
        print(b,end= " ")
        b += 1
    a += 1
    print("\r")
