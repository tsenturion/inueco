from book import Book
from library import Library
from utils import input_book_data, print_books, print_message

def main():
    library = Library()
    
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
        
        choice = input("Ваш выбор: ").strip()
        
        if choice == '1':
            title, author, year = input_book_data()
            library.add_book(Book(title, author, year))
            print_message("Книга успешно добавлена!")
            
        elif choice == '2':
            print("\nСписок всех книг:")
            print_books(library.get_all_books())
            
        elif choice == '3':
            print("\nДоступные книги:")
            print_books(library.get_available_books())
            
        elif choice == '4':
            author = input("Введите автора для поиска: ").strip()
            found_books = library.find_books_by_author(author)
            print(f"\nНайденные книги автора {author}:")
            print_books(found_books)
            
        elif choice == '5':
            try:
                year = int(input("Введите год для поиска: "))
                found_books = library.find_books_by_year(year)
                print(f"\nКниги изданные в {year} году:")
                print_books(found_books)
            except ValueError:
                print("Ошибка! Год должен быть числом.")
                
        elif choice == '6':
            title = input("Введите название книги для выдачи: ").strip()
            if library.borrow_book(title):
                print_message(f'Книга "{title}" выдана!')
                
        elif choice == '7':
            title = input("Введите название книги для возврата: ").strip()
            library.return_book(title)
            print_message(f'Книга "{title}" возвращена!')
            
        elif choice == '8':
            title = input("Введите название книги для удаления: ").strip()
            library.remove_book(title)
            print_message(f'Книга "{title}" удалена!')
            
        elif choice == '0':
            print("До свидания!")
            break
            
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()