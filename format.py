age = 10
txt = "Ridit is {} years old."
print(txt.format(age))

company = "Reynolds"
quantity = 20
price = 2.5

txt = "I have {1} {0} pens of Rs. {2} each."
print(txt.format(company, quantity, price))

txt = "I have {} {} pens of Rs. {} each."
print(txt.format(quantity, company, price))