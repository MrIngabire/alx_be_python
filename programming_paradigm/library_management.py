# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track book availability

    def checkout(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        else:
            return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        else:
            return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.checkout():
                    print(f"Successfully checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book with title '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Successfully returned '{title}'.")
                else:
                    print(f"'{title}' is already in the library.")
                return
        print(f"Book with title '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            print("Available books:")
            for book_title in available_books:
                print(f"   {book_title}")
        else:
            print("No books available.")

