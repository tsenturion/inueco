from library import Library
from book import Book
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
        
        choice = input("Ваш выбор: ")
        
        if choice == "1": #Добавить новую книгу
            try:
                title, author, year = input_book_data()
                book = Book(title, author, year)
                library.add_book(book)
                print_message("Книга успешно добавлена!")
            except ValueError:
                print_message("Ошибка: Год должен быть числом!")
            except Exception as e:
                print_message(f"Ошибка: {e}")
                

        elif choice == "2": #Показать все книги
            books = library.get_all_books()
            print_books(books)
            

        elif choice == "3": #Показать доступные книги
            books = library.get_available_books()
            print_books(books)
            

        elif choice == "4": #Найти книгу по автору
            author = input("Введите автора для поиска: ")
            books = library.find_books_by_author(author)
            print_books(books)
            

        elif choice == "5": #Найти книгу по году
            try:
                year = int(input("Введите год для поиска: "))
                books = library.find_books_by_year(year)
                print_books(books)
            except ValueError:
                print_message("Ошибка: Год должен быть числом!")
                

        elif choice == "6": #Выдать книгу
            title = input("Введите название книги для выдачи: ")
            library.borrow_book(title)
            

        elif choice == "7": #Вернуть книгу
            title = input("Введите название книги для возврата: ")
            library.return_book(title)
            

        elif choice == "8": #Удалить книгу
            title = input("Введите название книги для удаления: ")
            library.remove_book(title)
            

        elif choice == "0": #Выход
            print_message("Выход из программы. До свидания!")
            break
            

        else:
            print_message("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()