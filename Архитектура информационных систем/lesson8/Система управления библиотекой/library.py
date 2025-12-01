from book import Book

class Library:
    
    def __init__(self):

        self.books = []
    
    def add_book(self, book: Book):

        self.books.append(book)
    
    def remove_book(self, title: str):

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return True
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def find_books_by_author(self, author: str):

        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def find_books_by_year(self, year: int):

        return [book for book in self.books if book.year == year]
    
    def borrow_book(self, title: str):

        for book in self.books:
            if book.title.lower() == title.lower():
                if book.borrow():
                    return True
                else:
                    return False
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def return_book(self, title: str):

        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return True
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def get_available_books(self):

        return [book for book in self.books if book.is_available]
    
    def get_all_books(self):

        return self.books
    
    def find_book_by_title(self, title: str):

        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None