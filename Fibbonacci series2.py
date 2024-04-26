term = int(input("Enter no. of terms: "))
i = 3
def fibonacci(num1, num2):
    global i
    global term
    if term >= i:
        num3 = num1 + num2
        if term > i:
            print(num3,end=",")
        else:
            print(num3)
        i = i + 1
        fibonacci(num2, num3)

print("Here is the Fibonacci series: ")
print("0,1,", end="")
fibonacci(0, 1)