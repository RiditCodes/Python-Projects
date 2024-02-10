list1 = []
o = 0
e = 0
for num in range(0, 6):
    num = int(input("Enter a number: "))
    list1.append(num)
    if (num%2 != 0):
        o = o + num
    if (num%2 == 0):
        e = e + num
print(f"The numbers are: {list1}")
print(f"The sum of the odd numbers is {o}")
print(f"The sum of the even numbers is {e}")
