def global_keyword():
    global name
    name += " and Gurman"
    print(name)
    name = "Saturday And Sunday"
    print(name)

name = "Ridit"
global_keyword()
print(name)