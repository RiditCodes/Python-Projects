def list_items(list2):
    list2.append(50)
    print(list2)

list1 = [10,20,30,40]

print(list1)

list_items(list1)

print(list1)

'''
list1 and list2 are pointing at the same memory address. That's
why any modification is done inside function definition, it can
also be accessed outside the function.
'''