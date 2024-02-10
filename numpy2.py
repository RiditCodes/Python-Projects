import numpy as n

arr = n.array([1, 2, 3, 4, 5], ndmin = 6)
print(arr)
print(f"{arr.ndim}-dimensional array")

arr = n.array([1, 2, 3, 4, 5])
print(arr[2])

arr = n.array([[1, 2, 3], [4, 5, 6]])
print(arr[0, 1])

arr = n.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 0, 2])
print(arr[-2, 1, -3])