import numpy as np

arr = np.array([1, 2, 3, 5])
index = np.searchsorted(arr, 100)
print(index)