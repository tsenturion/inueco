# Модуль для работы с объектом "Библиотека", который будет использовать объекты "Книга"

from book import Book
from utils import print_message

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
        is_existing = False
        for existing_book in self.books:
            if book.title == existing_book.title:
                is_existing = True
                print_message(f"Книга с названием {book.title} уже существует в библиотеке")
                return
        if not is_existing:
            self.books.append(book)
            print_message("Книга добавлена в библиотеку.")

    def remove_book(self, title: str) -> Exception | None:
        """
        Удалить книгу из библиотеки

        `title` – название книги
        """
        is_existing = False
        for book in self.books:
            if book.title == title:
                is_existing = True
                self.books.remove(book)
                print_message("Книга удалена из библиотеки.")
                return
        if not is_existing:
            print_message(f"Книга с названием {title} не найдена в библиотеке")

    def find_book_by_title(self, title: str) -> Book | None:
        """
        Найти книгу по названию

        `title` – название книги
        """
        book = None
        for existing_book in self.books:
            if existing_book.title == title:
                book = existing_book
        if not book:
            print_message(f"Книги с названием {title} нет в библиотеке")
        return book

    def find_books_by_author(self, author: str) -> list[Book]:
        """
        Найти книги по автору

        `author` – имя автора
        """
        books_by_author = [book for book in self.books if book.author == author]
        if len(books_by_author) == 0:
            print_message(f"Книги автора {author} не найдены в библиотеке")
        return books_by_author

    def find_books_by_year(self, year: int) -> list[Book]:
        """
        Найти книги по году издания

        `year` – год издания
        """
        books_by_year = [book for book in self.books if book.year == year]
        if len(books_by_year) == 0:
            print_message(f"Книги, изданные в {year} году, не найдены в библиотеке")
        return books_by_year

    def borrow_book(self, title: str) -> None:
        """
        Выдать книгу

        `title` – название книги
        """
        book = self.find_book_by_title(title)
        if book:
            book.borrow()
            print_message("Книга выдана.")

    def return_book(self, title: str) -> None:
        """
        Вернуть книгу в библиотеку

        `title` – название книги
        """
        book = self.find_book_by_title(title)
        if book:
            book.return_book()
            print_message("Книга возвращена.")

    def get_available_books(self) -> list[Book]:
        """Получить список доступных книг"""
        available_books = [book for book in self.books if book.is_available]
        if len(available_books) == 0:
            print_message("В библиотеке нет доступных книг.")
        return available_books

    def get_all_books(self) -> list[Book]:
        """Получить список всех книг в библиотеке"""
        if len(self.books) == 0:
            print_message("В библиотеке нет книг.")
        return self.books
