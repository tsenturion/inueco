# Модуль для работы с объектом "Книга"

class Book:
    """Книга в библиотеке"""
    def __init__(self, title: str, author: str, year: int, is_available: bool = True):
        """
        Класс, представляющий книгу

        `title` – название книги

        `author` – автор книги
        
        `year` – год издания

        `is_available` – доступность книги (по умолчанию True)
        """
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        """Выдать книгу"""
        if not self.is_available:
            raise Exception(f"Книга {self.title} уже выдана")
        self.is_available = False

    def return_book(self):
        """Вернуть книгу в библиотеку"""
        if self.is_available:
            raise Exception(f"Книга {self.title} никому не выдавалась")
        self.is_available = True

    def __str__(self):
        """Строковое представление книги"""
        status = "Доступна" if self.is_available else "Выдана"
        return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Статус: {status}"
