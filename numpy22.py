'''
Filtering Arrays

If the value at an index is True that element is contained
in the filtered array.
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

bool_value = [False, True, False, True, True]

new_arr = arr[bool_value]

print(new_arr)