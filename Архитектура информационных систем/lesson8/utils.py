# Вспомогательный модуль с функциями для ввода и вывода данных

def input_book_data() -> tuple[str, str, int] | None:
    """Сбор данных о книге и преобразование в кортеж"""
    try:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания (только число): "))
        return (title, author, year)
    except ValueError:
        print_message("Некорректный ввод в одном из аргументов. Пожалуйста, введите значения в корректном формате.")
        return None

def print_books(books_list: list) -> None:
    """Вывод списка книг"""
    for book in books_list:
        print(book)

def print_message(message: str) -> None:
    """Вывод сообщения"""
    print(f"*** {message} ***")
