import numpy as np

arr1 = np.array([4, 5, 6, 7])
arr2 = np.array([8, 9, 10, 11])

arr = np.concatenate((arr1, arr2))

print(arr)

print("\n")

arr1 = np.array([[4, 5], [6, 7]])
arr2 = np.array([[8, 9], [10, 11]])

arr = np.concatenate((arr1, arr2))
print(arr)

print("\n")

arr = np.concatenate((arr1, arr2), axis = 1)
print(arr)