from book import Book
from library import Library
from utils import input_book_data, print_books, print_message


def main():
    """Главная функция программы"""
    library = Library()
    
    # Добавил несколько тестовых книг
    library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков", 1966))
    library.add_book(Book("Преступление и наказание", "Федор Достоевский", 1866))
    library.add_book(Book("1984", "Джордж Оруэлл", 1949))
    
    print("Добро пожаловать в систему управления библиотекой!")
    
    while True:
        print("\n=== Система управления библиотекой ===")
        print("1. Добавить новую книгу")
        print("2. Показать все книги")
        print("3. Показать доступные книги")
        print("4. Найти книгу по автору")
        print("5. Найти книгу по году")
        print("6. Выдать книгу")
        print("7. Вернуть книгу")
        print("8. Удалить книгу")
        print("0. Выйти")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == "0":
            print_message("До свидания!")
            break
        
        elif choice == "1":
            try:
                title, author, year = input_book_data()
                new_book = Book(title, author, year)
                library.add_book(new_book)
                print_message(f"Книга '{title}' успешно добавлена!")
            except Exception as e:
                print(f"Ошибка при добавлении книги: {e}")
        
        elif choice == "2":
            print("\nСписок всех книг:")
            print_books(library.get_all_books())
        
        elif choice == "3":
            print("\nСписок доступных книг:")
            available_books = library.get_available_books()
            if available_books:
                print_books(available_books)
            else:
                print("Нет доступных книг.")
        
        elif choice == "4":
            author = input("Введите автора для поиска: ").strip()
            if author:
                found_books = library.find_books_by_author(author)
                if found_books:
                    print(f"\nНайдено книг автора '{author}':")
                    print_books(found_books)
                else:
                    print(f"Книги автора '{author}' не найдены.")
            else:
                print("Ошибка: не введено имя автора.")
        
        elif choice == "5":
            try:
                year = int(input("Введите год для поиска: "))
                found_books = library.find_books_by_year(year)
                if found_books:
                    print(f"\nНайдено книг {year} года:")
                    print_books(found_books)
                else:
                    print(f"Книги {year} года не найдены.")
            except ValueError:
                print("Ошибка! Год должен быть целым числом.")
        
        elif choice == "6":
            title = input("Введите название книги для выдачи: ").strip()
            if title:
                if library.borrow_book(title):
                    print_message(f"Книга '{title}' выдана!")
            else:
                print("Ошибка: не введено название книги.")
        
        elif choice == "7":
            title = input("Введите название книги для возврата: ").strip()
            if title:
                if library.return_book(title):
                    print_message(f"Книга '{title}' возвращена!")
            else:
                print("Ошибка: не введено название книги.")
        
        elif choice == "8":
            title = input("Введите название книги для удаления: ").strip()
            if title:
                if library.remove_book(title):
                    print_message(f"Книга '{title}' удалена!")
            else:
                print("Ошибка: не введено название книги.")
        
        else:
            print("Ошибка! Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()