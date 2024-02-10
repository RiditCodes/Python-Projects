import numpy as n

arr = n.array([1, 2, 3, 4, 5])

copy_array = arr.copy()
view_array = arr.view()

print(copy_array.base)
print(view_array.base)

'''
Array has an attribute base that returns None if the array owns the data

Otherwise, the base attribute refers to the original value
'''