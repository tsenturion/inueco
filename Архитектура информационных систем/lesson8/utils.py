# Вспомогательный модуль с функциями для ввода и вывода данных

from book import Book

def input_book_data(title: str, author: str, year: int):
    """Преобразование введенных данных в кортеж для последующей инициализации класса Book"""
    return (title, author, year)

def print_books(books_list: list[Book]):
    """Вывод списка книг"""
    for book in books_list:
        print(book)

def print_message(message: str):
    """Вывод сообщения"""
    print(f"*** {message} ***")
