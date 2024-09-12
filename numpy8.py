import numpy as n

arr = n.array([6, 5, 4, 3, 2])
copy_arr = arr.copy()
print(arr)
print(copy_arr)

arr[4] = 8
copy_arr[1] = 7
print(arr)
print(copy_arr)

print()
arr = n.array([6, 5, 4, 3, 2])
view_array = arr.view()
print(arr)
print(view_array)

arr[2] = 9
view_array[3] = 10
print(arr)
print(view_array)