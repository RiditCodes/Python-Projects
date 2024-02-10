r = 0
i = 1
d = 0
t = 1
num = int(input("Enter no. of Fibbonacci numbers: "))
while t < num:
       print(r)
       d = r + i
       r = i
       i = d
       t += 1