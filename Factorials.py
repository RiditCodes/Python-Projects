def factorials(x):
    if x > 1:
        return x * factorials(x-1)
    else:
        return 1

num = int(input("Enter a number: "))
if num >= 0:
    print(f"Factorial of {num} is {factorials(num)}")
else:
    num = num * -1
    print(f"Factorial of {-1 * num} is {-1 * factorials(num)}")