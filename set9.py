Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 6, 7, 4, 8}

print(Set1^Set2)
print(Set2^Set1)


print(Set1.symmetric_difference(Set2))

'''
The symmetric difference of two sets is calculated by ^ operator
or symmetric_difference() method. This type of set removes the common
elements in both sets.
'''