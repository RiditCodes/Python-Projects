num = int(input("Enter a number: "))

if (num<0):
    print("Please don't write negative numbers")
else:
    if (num%2==0):
        print(f"{num} is even")
    elif(num%2!=0):
        print(f"{num} is odd")
