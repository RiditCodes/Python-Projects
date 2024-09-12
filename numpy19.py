'''
where() method searches a specific 
value in an array and returns index of that element.
'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
value = np.where(arr == 2)
#It returns indexes where value 2 is present.
print(value)

print()

arr = np.array([1, 2, 3, 4, 5, 6])
value = np.where(arr%2 == 0)
#It returns indexes where values are even.
print(value)