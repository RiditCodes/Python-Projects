Set = {"January", "February", "March"}
'''
print(Set)

Set.add("April")
Set.add("May")

print(Set)

Set.remove("January")
Set.discard("May")

print(Set)

Set.discard("July")
print(Set)'''

Set.remove("June")
print(Set)

'''
If the item to be deleted does not exist in the set, remove()
function will display error.
'''