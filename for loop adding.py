list1 = []
x = 0
for num in range(1, 6):
    num = int(input("Please enter a number: "))
    list1.append(num)
    x = x + num
print(f"These are the numbers: {list1}")
print(f"The sum is {x}")    
