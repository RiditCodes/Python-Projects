import numpy

arr = numpy.array([1,2,3,4,5])

print(arr)

import numpy as n           #We can use alias of numpy module.

arr = n.array([1,2,3,4,5])  #List is passed into the array() method.
print(arr)

arr = n.array((1,2,3,4,5))  #Tuple is passed into the array() method.
print(arr)

print(n.__version__)        #version of numpy module.

#The array object in numpy is called ndarray.
print(type(arr))