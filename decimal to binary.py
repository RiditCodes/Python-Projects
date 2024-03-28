remainder = 0
position = 1
binary = 0

decimal = int(input("Enter a number: "))
temp = decimal

while temp != 0:
    remainder = temp % 2
    temp //= 2
    binary = binary + (position * remainder)
    position *= 10

print(f"The binary form of {decimal} = {binary}")