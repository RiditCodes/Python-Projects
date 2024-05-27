def division():
    num1 = int(input("Enter number: "))
    num2 = int(input("Enter another number: "))
    div = num1 / num2
    print(num1, " / ", num2, " = ", div)

def modulus(val1, val2):
    mod = val1 % val2
    print(val1, " % ", val2, " = ", mod)

def floor_div():
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    fl_div = a // b
    print(a, " // ", b, " = ", end="")
    return fl_div

def exponent(Base, Power):
    exp = Base ** Power
    return exp

number1 = int(input("Enter number: "))
number2 = int(input("Enter another number: "))

division()
modulus(number1, number2)

temp = floor_div()
print(temp)

temp = exponent(number1, number2)
print(number1, " ** ", number2, " = ", temp)