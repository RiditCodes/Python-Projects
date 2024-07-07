def string_change(string):
    string = string + "Python"
    print(f"Inside function: {string}")

string_dif = input("Enter a word: ")
print(string_dif)

string_change(string_dif)
print(string_dif)

'''
string_dif(Argument) and string(Parameter) are different variables.
So they have separate memory locations. Call by value means value
of the argument string is copied to the parameter string. That's
why if we do any modification inside function definition, it won't 
change the value of the argument string.
'''