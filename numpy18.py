import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_arr = np.array_split(arr,3, axis = 1)
print(new_arr)