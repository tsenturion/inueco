from book import Book


class Library:
    """Класс, представляющий библиотеку с коллекцией книг"""
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def remove_book(self, title: str) -> bool:
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return True
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def find_books_by_author(self, author: str) -> list:
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def find_books_by_year(self, year: int) -> list:
        return [book for book in self.books if book.year == year]
    
    def borrow_book(self, title: str) -> bool:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow()
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def return_book(self, title: str) -> bool:
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return True
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def get_available_books(self) -> list:
        return [book for book in self.books if book.is_available]
    
    def get_all_books(self) -> list:
        return self.books.copy()