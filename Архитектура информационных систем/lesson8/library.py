from book import Book

class Library:
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """        
        Args:
            book (Book): Объект книги для добавления
        """
        self.books.append(book)
    
    def remove_book(self, title):
        """        
        Args:
            title (str): Название книги для удаления
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                return True
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def find_books_by_author(self, author):
        """        
        Args:
            author (str): Имя автора для поиска
            
        Returns:
            list: Список книг указанного автора
        """
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def find_books_by_year(self, year):
        """        
        Args:
            year (int): Год издания для поиска
            
        Returns:
            list: Список книг указанного года
        """
        return [book for book in self.books if book.year == year]
    
    def borrow_book(self, title):
        """        
        Args:
            title (str): Название книги для выдачи
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.borrow()
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def return_book(self, title):
        """        
        Args:
            title (str): Название книги для возврата
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.return_book()
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def get_available_books(self):
        """        
        Returns:
            list: Список доступных книг
        """
        return [book for book in self.books if book.is_available]
    
    def get_all_books(self):
        """        
        Returns:
            list: Список всех книг
        """
        return self.books.copy()