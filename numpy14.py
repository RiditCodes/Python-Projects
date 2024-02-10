import numpy as np

arr = np.array([2, 3, 4, 5, 6])

for index, element in np.ndenumerate(arr):
    print(index, element)

print("\n")

arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])

for index, element in np.ndenumerate(arr):
    print(index, element)