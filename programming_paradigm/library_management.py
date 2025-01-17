class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    
class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book): 
        self.__books.append(book)
    
    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and not book.__is_checked_out:
                book.__is_checked_out = True
                return f"Book {title} checked out successfully."
        return f"Book {title} not available."

    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.__is_checked_out:
                book.checked_out = False
                return f"Book {title} returned successfully."
            else:
                return f"Book {title} not found or not checked out."

    def list_available_books(self):
        available_books = [book for book in self.__books if not book.__is_checked_out]
        return [book.title for book in available_books]

