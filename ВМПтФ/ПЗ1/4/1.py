class Book:
    def __init__(self, name, author, publish_year):
        self.name = name
        self.author = author
        self.publish_year = publish_year


book1 = Book(name="Book_name", author="Oleg", publish_year=2000)

print("Name: " + book1.name + ", Author: " + book1.author + ", Publish year: " + str(book1.publish_year))
