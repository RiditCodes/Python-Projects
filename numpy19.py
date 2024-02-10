import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
value = np.where(arr == 2)
print(value)

print()

value = np.where(arr%2 == 0)
print(value)