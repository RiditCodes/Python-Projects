rows = int(input("Enter the no. of rows you want: "))

for r in range(0, rows):
    for n in range(0, rows-r):
        print("j", end=" ")
    print("\r")

"""
r = 0
n = 0

j j j j j 
j j j j 
j j j 
j j 
j 
"""