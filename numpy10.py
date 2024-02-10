'''
shape is an attribute of an array that returns a tuple
with number of elements in each dimension
'''

import numpy as np

a = np.array([[4, 5, 6, 7, 8], [1, 2, 3, 9, 10], [11, 12, 13, 14, 15]])

print(a)
print(f"Shape of array: {a.shape}")

a = np.array([1, 2, 3, 4, 5, 6], ndmin = 6)
print(a)
print(f"Shape of array: {a.shape}")