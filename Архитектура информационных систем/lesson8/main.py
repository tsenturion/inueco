from book import Book
from library import Library
from utils import input_book_data, print_books, print_message

def main():
    library = Library()
    
    library.add_book(Book("Мастер и Маргарита", "Михаил Булгаков", 1966))
    library.add_book(Book("Преступление и наказание", "Федор Достоевский", 1866))
    library.add_book(Book("1984", "Джордж Оруэлл", 1949))
    
    print("Добро пожаловать в систему управления библиотекой!")
    
    while True:
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
        
        choice = input("Ваш выбор: ").strip()
        
        try:
            if choice == "1":
                title, author, year = input_book_data()
                new_book = Book(title, author, year)
                library.add_book(new_book)
                print_message(f"Книга '{title}' успешно добавлена!")
                
            elif choice == "2":
                print("\nСписок всех книг в библиотеке:")
                all_books = library.get_all_books()
                print_books(all_books)
                
            elif choice == "3":
                print("\nСписок доступных книг:")
                available_books = library.get_available_books()
                print_books(available_books)
                
            elif choice == "4":
                author = input("Введите автора для поиска: ").strip()
                if author:
                    found_books = library.find_books_by_author(author)
                    print(f"\nКниги автора '{author}':")
                    print_books(found_books)
                else:
                    print_message("Неверный ввод автора!")
                    
            elif choice == "5":
                try:
                    year = int(input("Введите год для поиска: ").strip())
                    found_books = library.find_books_by_year(year)
                    print(f"\nКниги {year} года:")
                    print_books(found_books)
                except ValueError:
                    print_message("Ошибка! Год должен быть целым числом.")
                    
            elif choice == "6":
                title = input("Введите название книги для выдачи: ").strip()
                if title:
                    if library.borrow_book(title):
                        print_message(f"Книга '{title}' выдана!")
                else:
                    print_message("Неверный ввод названия!")
                    
            elif choice == "7":
                title = input("Введите название книги для возврата: ").strip()
                if title:
                    if library.return_book(title):
                        print_message(f"Книга '{title}' возвращена!")
                else:
                    print_message("Неверный ввод названия!")
                    
            elif choice == "8":
                title = input("Введите название книги для удаления: ").strip()
                if title:
                    if library.remove_book(title):
                        print_message(f"Книга '{title}' удалена!")
                else:
                    print_message("Неверный ввод названия!")
                    
            elif choice == "0":
                print_message("Спасибо за использование системы! До свидания!")
                break
                
            else:
                print_message("Неверный выбор! Пожалуйста, выберите пункт от 0 до 8.")
                
        except Exception as e:
            print_message(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()