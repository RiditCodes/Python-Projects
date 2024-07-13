print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

while True:
    choice = int(input("Enter your choice: "))
    if choice in (1, 2, 3, 4):
        num1 = int(input("Enter a no.: "))
        num2 = int(input("Enter another no.: "))

        if choice == 1:
            print(num1, " + ", num2, " = ", addition(num1, num2))
        if choice == 2:
            print(num1, " - ", num2, " = ", subtraction(num1, num2))
        if choice == 3:
            print(num1, " x ", num2, " = ", multiplication(num1, num2))
        if choice == 4:
            print(num1, " / ", num2, " = ", division(num1, num2))

        exit_choice = int(input("If you want to exit, enter 1. If not, enter any other no.: "))
        if exit_choice == 1:
            break
        else:continue
        
    else:
        print("Invalid choice! Try again...")