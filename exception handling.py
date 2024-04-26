a = 10
b = 1

try:
    print(a/b)
    k = int(input("Enter number: "))
    print(k)

except ZeroDivisionError as e:
    print("Number cannot be divided by zero", e)

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong...")

finally:
    print("End")