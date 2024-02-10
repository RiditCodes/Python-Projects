import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new_arr = np.array_split(arr, 4)
print(new_arr)

new_arr = np.array_split(arr, 6)
print()
print(new_arr)

print()
print(new_arr[0])
print(new_arr[1])
print(new_arr[2])

arr = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
new_arr = np.array_split(arr, 3)
print()
print(new_arr)

new_arr = np.array_split(arr, 4)
print()
print(new_arr)