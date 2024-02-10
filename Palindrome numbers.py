num = int(input("Enter a 3-digit number: "))
i = 100
sum = 0

temp = num
while temp > 0:
    rem = temp % 10
    temp //= 10
    sum = sum + rem * i
    i //= 10

if num == sum:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")


