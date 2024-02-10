num = int(input("Enter your number to multiply: "))
table_till = int(input("Enter where do you want to end your table: "))
multiply = 1
while multiply <= table_till:
    print(f"{num}*{multiply}={num * multiply}")
    multiply += 1
else:
    print("Finished your table!!")
