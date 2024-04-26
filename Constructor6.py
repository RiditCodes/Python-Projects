class Book:
    '''Built-in class atributes'''

    def __init__(self, book_title, book_author, book_price):
        self.book_title = book_title
        self.book_author = book_author
        self.book_price = book_price

book = Book("Java programming", "Kanitkar", 3400)

#Docstring contains the documentation of a class.
print(book.__doc__)

#It provides the dictionary containing class attributes and values.
print(book.__dict__)

#It returns the module n which this class is defined
print(book.__module__)