def function1():
    x = 5
    def function2():
        nonlocal x
        x = x * 2
        print(f"Inside function2: {x}")
    function2()
    return x

print(f"function1: {function1()}")