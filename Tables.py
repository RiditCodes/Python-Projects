num = int(input("Enter your number: "))
table_till = int(input("Enter where do you want to end your table: "))
for x in range(1, table_till+1):
    print(f"{num}*{x}={num * x}")


