# Главный файл, который импортирует все модули и запускает программу

from book import Book
from library import Library
from utils import input_book_data, print_books, print_message

# Инициализация класса библиотеки
library = Library()

# Текст для вывода меню
menu_text = """
=== Система управления библиотекой ===
1. Добавить новую книгу
2. Показать все книги
3. Показать доступные книги
4. Найти книгу по автору
5. Найти книгу по году
6. Выдать книгу
7. Вернуть книгу
8. Удалить книгу
0. Выйти
"""

# Основной цикл программы
while True:
    print(menu_text)
    # Запрашиваем у пользователя выбор действия
    choice = input("Ваш выбор: ")
    # Обрабатываем выбор пользователя
    match choice:
        case "1":
            # Функция для добавления книги с обработкой некорректного ввода
            def func():
                try:
                    title = input("Введите название книги: ")
                    author = input("Введите автора книги: ")
                    year = int(input("Введите год издания (только число): "))

                    book_data = input_book_data(title, author, year)
                    try:
                        book = Book(*book_data)
                        library.add_book(book)
                        print_message("Книга добавлена в библиотеку.")
                    except Exception as e:
                        print_message(str(e))

                    return True
                except ValueError:
                    print_message("Некорректный ввод в одном из аргументов. Пожалуйста, введите значения в корректном формате.")
                    return False
            # Если в процессе выполнения программы возникла ошибка ввода – повторяем запрос
            while not func():
                pass
        case "2":
            print_books(library.get_all_books())
        case "3":
            print_books(library.get_available_books())
        case "4":
            author = input("Введите имя автора: ")
            print_books(library.find_books_by_author(author))
        case "5":
            # Функция для поиска книг по году издания с обработкой некорректного ввода
            def func():
                try:
                    year = int(input("Введите год издания (только число): "))
                    print_books(library.find_books_by_year(year))
                    return True
                except ValueError:
                    print_message("Некорректный ввод. Пожалуйста, введите числовое значение.")
                    return False
            # Если в процессе выполнения программы возникла ошибка ввода – повторяем запрос
            while not func():
                pass
        case "6":
            title = input("Введите название книги: ")
            try:
                library.borrow_book(title)
                print_message("Книга выдана.")
            except Exception as e:
                print_message(str(e))
        case "7":
            title = input("Введите название книги: ")
            try:
                library.return_book(title)
                print_message("Книга возвращена.")
            except Exception as e:
                print_message(str(e))
        case "8":
            title = input("Введите название книги: ")
            try:
                library.remove_book(title)
                print_message("Книга удалена.")
            except Exception as e:
                print_message(str(e))
        case "0":
            print_message("Выход из программы")
            # Прерывание цикла для завершения программы
            break
        case _:
            # Обработка непредусмотренного выбора пользователя
            print_message("Действие не распознано. Пожалуйста, выберите корректный пункт меню.")