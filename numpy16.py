import numpy as np

arr1 = np.array([4, 5, 6, 7])
arr2 = np.array([8, 9, 10, 11])

arr = np.stack((arr1, arr2), axis = 1)
print(arr)

print("\n")

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.stack((arr1, arr2), axis = 1)
print(arr)