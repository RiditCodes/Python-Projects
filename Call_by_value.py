def string_change(string):
    string = string + "Python"
    print(f"Inside function: {string}")

string = input("Enter a word: ")
print(string)

string_change(string)
print(string)