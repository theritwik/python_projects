//Library Management System
class Book:
    def __init__(self, title, author, isbn, quantity=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"

class Library:
    def __init__(self):
        self.books = {}
    
    def addBook(self, book):
        if book.isbn in self.books:
            self.books[book.isbn].quantity += book.quantity
        else:
            self.books[book.isbn] = book

    def showInfo(self):
        if not self.books:
            print("No books in the library.")
        else:
            print(f"The library has {len(self.books)} unique books:")
            for book in self.books.values():
                print(book)

    def searchBook(self, title):
        found = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if found:
            for book in found:
                print(book)
        else:
            print("No books found with that title.")
    
    def deleteBook(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print(f"Book with ISBN {isbn} has been deleted.")
        else:
            print("No book found with that ISBN.")

    def borrowBook(self, isbn):
        if isbn in self.books and self.books[isbn].quantity > 0:
            self.books[isbn].quantity -= 1
            print(f"You have borrowed {self.books[isbn].title}.")
        else:
            print("Sorry, this book is unavailable.")
    
    def returnBook(self, isbn):
        if isbn in self.books:
            self.books[isbn].quantity += 1
            print(f"You have returned {self.books[isbn].title}.")
        else:
            print("Invalid ISBN.")

# Example usage:
l1 = Library()

# Add books
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780747532699", 3)
book2 = Book("The Hobbit", "J.R.R. Tolkien", "9780261103344", 2)

l1.addBook(book1)
l1.addBook(book2)

# Show library info
l1.showInfo()

# Search for books by title
print("\nSearch results for 'Harry Potter':")
l1.searchBook("Harry Potter")

# Borrow and return books
l1.borrowBook("9780747532699")
l1.returnBook("9780747532699")

# Delete a book
l1.deleteBook("9780261103344")

# Show updated library info
print("\nUpdated library info:")
l1.showInfo()
