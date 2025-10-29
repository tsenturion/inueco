from book import Book
from library import Library
from utils import input_book_data, print_books, print_message, input_with_validation, validate_year

def main():
    """Главная функция программы"""
    # Создаем экземпляр библиотеки
    library = Library()
    
    demo_books = [
        Book("Мастер и Маргарита", "Михаил Булгаков", 1966),
        Book("Преступление и наказание", "Федор Достоевский", 1866),
        Book("1984", "Джордж Оруэлл", 1949),
        Book("Война и мир", "Лев Толстой", 1869)
    ]
    
    for book in demo_books:
        library.add_book(book)
    
    print_message("Добро пожаловать в систему управления библиотекой!")
    
    while True:
        # Вывод главного меню
        print("\n" + "="*40)
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
        print("="*40)
        
        try:
            choice = input("Ваш выбор: ").strip()
            
            if choice == "0":
                print_message("Спасибо за использование системы! До свидания!")
                break
            
            elif choice == "1":
                # Добавление новой книги
                book_data = input_book_data()
                if book_data:
                    title, author, year = book_data
                    new_book = Book(title, author, year)
                    library.add_book(new_book)
                    print_message(f"Книга '{title}' успешно добавлена!")
            
            elif choice == "2":
                # Показать все книги
                all_books = library.get_all_books()
                print("\n=== Все книги в библиотеке ===")
                print_books(all_books)
            
            elif choice == "3":
                # Показать доступные книги
                available_books = library.get_available_books()
                print("\n=== Доступные книги ===")
                print_books(available_books)
            
            elif choice == "4":
                # Поиск по автору
                author = input_with_validation("Введите автора для поиска: ")
                found_books = library.find_books_by_author(author)
                print(f"\n=== Книги автора '{author}' ===")
                print_books(found_books)
            
            elif choice == "5":
                # Поиск по году
                year_str = input_with_validation("Введите год для поиска: ", validate_year)
                if year_str:
                    found_books = library.find_books_by_year(int(year_str))
                    print(f"\n=== Книги {year_str} года ===")
                    print_books(found_books)
            
            elif choice == "6":
                # Выдача книги
                title = input_with_validation("Введите название книги для выдачи: ")
                if library.borrow_book(title):
                    print_message(f"Книга '{title}' успешно выдана!")
            
            elif choice == "7":
                # Возврат книги
                title = input_with_validation("Введите название книги для возврата: ")
                if library.return_book(title):
                    print_message(f"Книга '{title}' успешно возвращена!")
            
            elif choice == "8":
                # Удаление книги
                title = input_with_validation("Введите название книги для удаления: ")
                if library.remove_book(title):
                    print_message(f"Книга '{title}' успешно удалена!")
            
            else:
                print_message("Неверный выбор! Пожалуйста, выберите пункт из меню.")
        
        except KeyboardInterrupt:
            print_message("\nПрограмма прервана пользователем. До свидания!")
            break
        except Exception as e:
            print_message(f"Произошла ошибка: {e}")

# Точка входа в программу
if __name__ == "__main__":
    main()