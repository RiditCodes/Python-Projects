string = input("Enter string: ")

#isalpha() method returns True if all the characters are alphabets
print(string.isalpha())
#isalnum() returns True if each character is either alphabet or number
print(string.isalnum())
#isdigit() returns True if all the characters are numbers
print(string.isdigit())
'''islower() returns True if string contains at least one 
alphabet and all the alphabets are in lower case'''
print(string.islower())
'''isupper() returns True if string contains at least one
alphabet and all the alphabets are in upper case'''
print(string.isupper())
#startswith() returns True if the string starts with the specified value
print(string.startswith("pr"))
#endswith() returns True if the string ends with the specified value
print(string.endswith("re"))
'''center() method will center align the string, using a
specified character(space is default) as the fill character'''
#The entered string should contain the number of characters less than 10
print(string.center(10))
print(string.center(10, "$"))