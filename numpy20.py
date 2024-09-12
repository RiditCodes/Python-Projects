'''
searchsorted() method returns the index where the specified 
value should be inserted to maintain the search order.
'''

import numpy as np

arr = np.array([1, 2, 3, 5])
index = np.searchsorted(arr, 100)
print(index)