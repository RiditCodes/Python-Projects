num_rows = int(input("Enter no. of rows: "))

space = num_rows - 1

for rows in range(num_rows):
        for sp in range(space):
            print("",end =" ")

        print("1", end=" ")
        space -= 1
        increment = rows//2

        if (rows%2):
            decrement = rows//2
        else:
            decrement = rows//2-1

        digit = rows
        for column in range(increment):
            print(digit, end = " ")
            digit += 2

        if (rows%2):
            digit -= 2
        else:
            digit -= 4

        for column in range(decrement):
            print(digit, end = " ")
            digit -= 2  
            
        if (rows>0):
            print("1", end = " ")
        print() 