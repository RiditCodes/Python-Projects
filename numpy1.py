import numpy as n

arr = n.array(20)
print(arr)
print(f"{arr.ndim}-dimensional array")

print()
arr = n.array([1, 2, 3, 4, 5])
print(arr)
print(f"{arr.ndim}-dimensional array")

print()
arr = n.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(f"{arr.ndim}-dimensional array")

print()
arr = n.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(f"{arr.ndim}-dimensional array")

print(n.__version__)

print(type(arr))