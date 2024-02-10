#Table Maker
num = int(input("What number do you want the table of: "))
table_till = int(input("When do you want to end your table: "))
for n in range(1, table_till+1):
    print(f"{num} x {n} = {num*n}")
