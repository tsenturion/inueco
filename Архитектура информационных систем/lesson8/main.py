from book import Book
from library import Library
from utils import input_book_data, print_books, print_message, input_int, input_non_empty_string

def main():
    """Главная функция программы"""
    # Создаем экземпляр библиотеки
    library = Library()
    
    # Добавляем несколько тестовых книг для демонстрации
    demo_books = [
        Book("Мастер и Маргарита", "Михаил Булгаков", 1966),
        Book("Преступление и наказание", "Федор Достоевский", 1866),
        Book("1984", "Джордж Оруэлл", 1949),
        Book("Гарри Поттер и философский камень", "Джоан Роулинг", 1997)
    ]
    
    for book in demo_books:
        library.add_book(book)
    
    print_message("Добро пожаловать в систему управления библиотекой!")
    
    while True:
        # Вывод главного меню
        print("\n" + "=" * 40)
        print("=== Система управления библиотекой ===")
        print("1. Добавить новую книгу")
        print("2. Показать все книги")
        print("3. Показать доступные книги")
        print("4. Найти книгу по автору")
        print("5. Найти книгу по году")
        print("6. Выдать книгу")
        print("7. Вернуть книгу")
        print("8. Удалить книгу")
        print("0. Выйти")
        print("=" * 40)
        
        choice = input_int("Ваш выбор: ", 0, 8)
        
        if choice is None:
            continue
        
        if choice == 0:
            print_message("До свидания! Спасибо за использование системы.")
            break
        
        elif choice == 1:
            # Добавление новой книги
            print("\n--- Добавление новой книги ---")
            book_data = input_book_data()
            if book_data:
                title, author, year = book_data
                new_book = Book(title, author, year)
                if library.add_book(new_book):
                    print_message(f"Книга '{title}' успешно добавлена!")
                else:
                    print("Ошибка при добавлении книги!")
        
        elif choice == 2:
            # Показать все книги
            print("\n--- Список всех книг ---")
            all_books = library.get_all_books()
            print_books(all_books)
        
        elif choice == 3:
            # Показать доступные книги
            print("\n--- Список доступных книг ---")
            available_books = library.get_available_books()
            print_books(available_books)
        
        elif choice == 4:
            # Поиск по автору
            print("\n--- Поиск книг по автору ---")
            author = input_non_empty_string("Введите автора для поиска: ")
            if author:
                found_books = library.find_books_by_author(author)
                if found_books:
                    print(f"\nНайдено {len(found_books)} книг автора '{author}':")
                    print_books(found_books)
                else:
                    print(f"Книги автора '{author}' не найдены.")
        
        elif choice == 5:
            # Поиск по году
            print("\n--- Поиск книг по году ---")
            year = input_int("Введите год для поиска: ")
            if year is not None:
                found_books = library.find_books_by_year(year)
                if found_books:
                    print(f"\nНайдено {len(found_books)} книг {year} года:")
                    print_books(found_books)
                else:
                    print(f"Книги {year} года не найдены.")
        
        elif choice == 6:
            # Выдача книги
            print("\n--- Выдача книги ---")
            title = input_non_empty_string("Введите название книги для выдачи: ")
            if title:
                if library.borrow_book(title):
                    print_message(f"Книга '{title}' успешно выдана!")
        
        elif choice == 7:
            # Возврат книги
            print("\n--- Возврат книги ---")
            title = input_non_empty_string("Введите название книги для возврата: ")
            if title:
                if library.return_book(title):
                    print_message(f"Книга '{title}' успешно возвращена!")
        
        elif choice == 8:
            # Удаление книги
            print("\n--- Удаление книги ---")
            title = input_non_empty_string("Введите название книги для удаления: ")
            if title:
                if library.remove_book(title):
                    print_message(f"Книга '{title}' успешно удалена!")
        
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()