from book import Book

class Library:
    """Класс для управления коллекцией книг"""
    
    def __init__(self):
        """Конструктор библиотеки"""
        self.books = []
    
    def add_book(self, book):
        """
        Добавить книгу в библиотеку
        
        Args:
            book (Book): Объект книги для добавления
        """
        if isinstance(book, Book):
            self.books.append(book)
            return True
        return False
    
    def remove_book(self, title):
        """
        Удалить книгу по названию
        
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
        Найти книги по автору
        
        Args:
            author (str): Имя автора
            
        Returns:
            list: Список книг указанного автора
        """
        return [book for book in self.books if author.lower() in book.author.lower()]
    
    def find_books_by_year(self, year):
        """
        Найти книги по году издания
        
        Args:
            year (int): Год издания
            
        Returns:
            list: Список книг указанного года
        """
        return [book for book in self.books if book.year == year]
    
    def borrow_book(self, title):
        """
        Выдать книгу по названию
        
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
        Вернуть книгу по названию
        
        Args:
            title (str): Название книги для возврата
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return True
        print(f"Книга с названием '{title}' не найдена.")
        return False
    
    def get_available_books(self):
        """
        Получить все доступные книги
        
        Returns:
            list: Список доступных книг
        """
        return [book for book in self.books if book.is_available]
    
    def get_all_books(self):
        """
        Получить все книги библиотеки
        
        Returns:
            list: Список всех книг
        """
        return self.books
    
    def find_book_by_title(self, title):
        """
        Найти книгу по точному названию
        
        Args:
            title (str): Название книги
            
        Returns:
            Book or None: Найденная книга или None
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None