class Book:

    '''Attributes'''

    def __init__(self,book_title,book_author,book_price):
        self.book_title = book_title
        self.book_author = book_author
        self.book_price = book_price

book = Book("Python Programming", "Mark Rakes","$200")

print(book.__doc__)

print(book.__dict__)

print(book.__module__)