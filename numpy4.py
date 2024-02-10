import numpy as n 

arr = n.array([1, 2, 3, 4])

print(type(arr))
print(arr.dtype)

'''
type() method returns class type of the argument

dtype is a property of numpy array object tht returns the data type of
an array
'''

arr = n.array(["Apple", "Banana", "cherry"])
print(arr.dtype)

'''
What does <U6 mean?

< - Little Endian
U - Unicode
6 - length

'''