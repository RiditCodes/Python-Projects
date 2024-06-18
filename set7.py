Days1 = {"Monday", "Tuesday","Wednesday"}
Days2 = {"Wednesday", "Thursday"}
Days3 = {"Friday", "Wednesday"}

print(Days1&Days2&Days3)

print(Days1.intersection(Days2, Days3))

'''
The intersection of two sets can be performed by & operator or
intersection() func. The intersection of two sets contains the elements
that are common in both sets.
'''