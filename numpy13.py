import numpy as np

print("Iterating 1-D array")
arr = np.array([4, 5, 6, 7, 8])
for i in arr:
    print(i)

print("\nIterating 2-D array")
arr = np.array([[1, 2, 3], [4, 5, 6]])
for i in arr:
    print(i)

print("\nIterating each element")
for a in arr:
    for b in a:
        print(b)

print("\nnditer() method")
arr = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
for i in np.nditer(arr):
    print(i)