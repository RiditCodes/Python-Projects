class Book:
    def __init__(self, book_title, book_author, book_price):
        self.book_title = book_title
        self.book_author = book_author
        self.book_price = book_price

    def show(self):
        print(self.book_title, "\n", self.book_author, "\n", self.book_price)

book = Book("Python programming", "Mark", 3000)
book.show()

#getattr returns the attribute value of an object
print(getattr(book, "book_title"))

#setattr assigns a new value to an existing attribute
setattr(book, "book_price", 3200)

print(getattr(book, "book_price"))

#hasattr will return True as book_author is an attribute of object
print(hasattr(book, "book_author"))

#delattr deletes the attributes
delattr(book, "book_title")