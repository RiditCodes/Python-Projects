import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Converting 1-D array into 3-D array...")
new_arr = arr.reshape(3, 2, 2)
print(new_arr)

'''
The first number represents 1st dimension which contains 3 arrays.
The second number represents 2nd dimension which contains 2 arrays.
The third number represents 3rd dimension which contains 2 values.
'''

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print("\n\nConverting 1-D array into 4-D array...")
new_arr = arr.reshape(2, 5, 2, 1)
print(new_arr)

'''
The first number represents 1st dimension which contains 2 arrays.
The second number represents 2nd dimension which contains 5 arrays.
The third number represents 3rd dimension which contains 2 arrays.
The fourth number represents 4th dimension which contains 1 value.
'''