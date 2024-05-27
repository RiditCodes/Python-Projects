a = 0
b = 1
c = 0
d = 1
num = int(input("Enter no. of terms: "))
while d <= num:
       if d != num:
           print(a, end=",")
       else:
            print(a)
       c = a + b
       a = b
       b = c
       d += 1