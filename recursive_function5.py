term = int(input("Enter no. of terms: "))

def fibonacci(num1, num2):
    global term
    if term >= 1:
        num3 = num1 + num2
        if term > 1:
            print(num3,end=",")
        else:
            print(num3)
        term -= 1
        fibonacci(num2, num3)

print("Here is the Fibonacci series: ")
print("0,1,", end="")
fibonacci(0, 1)