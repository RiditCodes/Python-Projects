import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
new_arr = arr.reshape(-1)
print(arr)
print(new_arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
new_arr = arr.reshape(-1)
print('\n', arr)
print(new_arr)