from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return
        print(f'Книга "{title}" не найдена.')

    def find_books_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def find_books_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow()
        print(f'Книга "{title}" не найдена.')
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f'Книга "{title}" не найдена.')

    def get_available_books(self):
        return [book for book in self.books if book.is_available]

    def get_all_books(self):
        return self.books