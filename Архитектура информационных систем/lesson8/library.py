# Модуль для работы с объектом "Библиотека", который будет использовать объекты "Книга"

from book import Book

class Library:
    """Библиотека, содержащая книги"""
    def __init__(self) -> None:
        """Инициализация библиотеки с пустым списком книг"""
        self.books = []

    def add_book(self, book: Book) -> None:
        """
        Добавить книгу в библиотеку

        `book` – объект класса Book
        """
        if book.title in [b.title for b in self.books]:
            raise Exception(f"Книга с названием {book.title} уже существует в библиотеке")
        self.books.append(book)

    def remove_book(self, title: str) -> Exception | None:
        """
        Удалить книгу из библиотеки

        `title` – название книги
        """
        if title not in [book.title for book in self.books]:
            raise Exception(f"Книга с названием {title} не найдена в библиотеке")
        self.books = [book for book in self.books if book.title != title]

    def find_books_by_title(self, title: str) -> list[Book]:
        """
        Найти книги по названию

        `title` – название книги
        """
        return [book for book in self.books if book.title == title]

    def find_books_by_author(self, author: str) -> list[Book]:
        """
        Найти книги по автору

        `author` – имя автора
        """
        return [book for book in self.books if book.author == author]

    def find_books_by_year(self, year: int) -> list[Book]:
        """
        Найти книги по году издания

        `year` – год издания
        """
        return [book for book in self.books if book.year == year]

    def borrow_book(self, title: str) -> Exception | None:
        """
        Выдать книгу

        `title` – название книги
        """
        book = next((book for book in self.books if book.title == title), None)
        if not book:
            raise Exception(f"Книга с названием {title} не найдена в библиотеке")
        book.borrow()

    def return_book(self, title: str) -> Exception | None:
        """
        Вернуть книгу в библиотеку

        `title` – название книги
        """
        book = next((book for book in self.books if book.title == title), None)
        if not book:
            raise Exception(f"Книга с названием {title} не найдена в библиотеке")
        book.return_book()

    def get_available_books(self) -> list[Book]:
        """Получить список доступных книг"""
        return [book for book in self.books if book.is_available]

    def get_all_books(self) -> list[Book]:
        """Получить список всех книг в библиотеке"""
        return self.books
