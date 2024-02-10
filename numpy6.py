import numpy as np

arr = np.array([4, 5, 6, 7], dtype = "S")

#Data type can be defined for the array elements

print(arr)
print(arr.dtype)

'''
b denotes a byte string.
Byte string is a sequence of bytes. 
Everything must be converted into a byte string before storing in a computer.

|S1 means that array contains strings of length 1. 
Pipe symbol(|) is byteorder flag. 
In this case byteorder flag is not required so pipe symbol is used meaning "Not Applicable".
Byteorder is used to represent the integer.
'''