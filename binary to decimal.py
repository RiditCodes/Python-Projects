num = int(input("Enter a number in Binary: "))
count = 0
temp = num
power = 1
add = 0

while temp > 0:
    remainder = temp % 10
    temp //= 10
    count += 1
    for i in range(1, count):
        power *= 2
    add = add + remainder * power
    power = 1

print(f"{num} in Binary System is: {add}") 