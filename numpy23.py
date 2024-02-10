import numpy as np

arr = np.array([5, 6, 7, 8, 9])

bool_value = []

for element in arr:
    if element%3 == 0:
        bool_value.append(True)
    else:
        bool_value.append(False)

new_arr = arr[bool_value]

print(new_arr)