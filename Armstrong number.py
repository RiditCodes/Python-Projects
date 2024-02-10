num = int(input("Enter number: "))
i = 0
j = 0
temp = num
product = 1
sum = 0

while temp > 0:
    temp //= 10
    j += 1

temp == num

while temp > 0:
    remainder = temp % 10
    temp //= 10
    product = 1
    for i in range(1, j+1):
        product = product * remainder
    sum = sum + product

if sum == num:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} is not a armstrong number")
