'''
format() can be used to insert numbers into
strings. This method
takes the passed arguments and places them 
in the string where the
placeholders {} are specified.
'''

age = 13
txt = "I am {} years old."
print(txt.format(age))


company = "Parker"
quantity = 2
price = 400

txt = "I have {} {} pens of Rs.{} each."
print(txt.format(quantity, company, price))

#index number can be used in placeholder for the arguments.

txt = "I have {1} {0} pens of Rs.{2} each."
print(txt.format(company, quantity, price))