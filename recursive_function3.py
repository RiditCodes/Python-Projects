def sum(n):
   global count
   if count <= 0:
       return n
   else:
       count -= 1
       return n + sum(n-1)
   
num = int(input("Enter a no.: "))
count = int(input(f"Enter no. of times {num} will be added: "))

print("The sum is",sum(num))