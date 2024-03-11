class Book:
    def __init__(self, name, author, publish_year):
        self.name = name
        self.author = author
        self.publish_year = publish_year


class BookShelf:
    def __init__(self, books=[]):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_name):
        for x in self.books:
            if x.name == book_name:
                self.books.remove(x)
                return
        print("No such book found.")
        return

    def print_books(self):
        for x in self.books:
            print("------------------------------------------")
            print("Name: " + x.name)
            print("Author: " + x.author)
            print("Year of publish: " + str(x.publish_year))
            print()


book1 = Book(name="Book_name", author="Oleg", publish_year=2000)
book2 = Book(name="Book_name_2", author="Oleg_2", publish_year=2001)
book3 = Book(name="Book_name_3", author="Oleg_3", publish_year=2002)

books = BookShelf()

books.add_book(book1)
books.add_book(book2)
books.add_book(book3)
books.print_books()
books.remove_book("Book_name")
books.print_books()
books.remove_book("name")
books.print_books()
