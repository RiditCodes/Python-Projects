rows = int(input("Enter the no. of rows you want: "))

for r in range(0, rows):
    for n in range(0, r+1):
        print("j", end=" ")
    print("\r")

"""
if rows = 5, output will be: 
   
   j
   j j 
   j j j 
   j j j j 
   j j j j j
"""