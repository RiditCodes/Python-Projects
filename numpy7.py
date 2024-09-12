import numpy as n

arr = n.array([1, 2, 3, 4, 5], dtype = "i4")
print(arr)
print(arr.dtype)

'''
i4 represents integer of size 4 bytes i.e. 4*8 = 32 bits.
So output is displayed as int32
'''

print()
arr = n.array([1.2, 3.4, 5.6])
#astype() method can be used to change the data type of an existing array.

#We can use any one among the below statements.
new_type = arr.astype("i")
#new_type = arr.astype(int)

print(arr)
print(new_type)
print(new_type.dtype)

print()
arr = n.array([1, 2, 0, 4])
new_type = arr.astype(bool)
print(new_type)
print(new_type.dtype)