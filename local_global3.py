var = 5

def function():
    print("Inside function", var)
def function2():
    var = 7
    print("Inside function", var)
def function3():
    global var
    print("Inside function", var)
    var = 6
    print("Inside function", var)

print("Outside function", var)
function()
print("Outside function", var)
function2()
print("Outside function", var)
function3()
print("Outside function", var)