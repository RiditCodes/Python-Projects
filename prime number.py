import time
num = int(input("Enter a number: "))
count = 2

while count < num:
    modulo = num % count
    if modulo == 0:
        print("This is not a prime number")
        time.sleep(2)
        exit()
    else:
        pass
print("This is a prime number")
