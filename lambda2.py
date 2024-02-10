function1 = lambda var1 : var1 * 2
print(function1(17))
print(" ")
function2 = lambda var2, var3, var4 : var2 + var3 - var4
print(function2(15, 14, 12))

def function3(var6):
    return lambda var5 : var5 // var6

num1 = int(input("Enter number for function: "))
num2 = int(input("Enter number for args: "))

function4 = function3(num1)
print(function4(num2))