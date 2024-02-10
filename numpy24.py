import numpy as np

arr = np.array([5, 6, 7, 8, 9])

bool_value = arr%2 == 1

new_arr = arr[bool_value]

print(new_arr)