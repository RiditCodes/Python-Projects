string = input("Enter string: ")

'''
All string methods return new values.
They do not change the original string.
'''

#len() function returns length that is number of items in the string
print("Length of ",string," is ",len(string))
#strip() reutrns a copy of string by removing the leading and trailing whitespace
print(string.strip())
#lower() returns a copy of string converted to lowercase
print(string.lower())
#upper() returns a copy of string converted to uppercase
print(string.upper())

print(string)