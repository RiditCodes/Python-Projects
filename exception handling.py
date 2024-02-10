a = 53
b = 0

try:
    print("trying...")
    print(a/b)

except ZeroDivisionError as e:
    print("Number cannot be divided by zero")

except ValueError as e:
    print("Invalid input")

except Exception as e:
    print("Something went wrong")

finally:
    print("finally finished")