sum = 0
i = 1
num = int(input("Enter a decimal number: "))

while num > 0:
    remainder = num % 2     
    num = num // 2          
    sum = sum + i * remainder 
    i=i*10              
    
print(sum)
