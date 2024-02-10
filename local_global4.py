def function1():
    x = 5
    def function2():
        global x
        x *= 2
        print("function2(): ", x)
    function2()
    return x

print("function1(): ", function1())