num = int(input("Enter your number: "))
table_till = int(input("Enter where do you want to end your table: "))
multiply_checker = 1
for x in range(0, table_till):
    print(f"{num}*{multiply_checker}={num * multiply_checker}")
    multiply_checker += 1


