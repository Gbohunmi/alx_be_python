class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book): 
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f"Book {title} checked out successfully."
        return f"Book {title} not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book.checked_out = False
                return f"Book {title} returned successfully."
            else:
                return f"Book {title} not found or not checked out."

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if available_books == []:
            print("No book is availble")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
    


library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))
# Initial list of available books
print("Available books after setup:")
library.list_available_books()