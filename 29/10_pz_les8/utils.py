def input_book_data():
    title = input("Введите название книги: ").strip()
    while not title:
        print("Ошибка: Название книги не может быть пустым!")
        title = input("Введите название книги: ").strip()
    

    author = input("Введите автора книги: ").strip()
    while not author:
        print("Ошибка: Автор книги не может быть пустым!")
        author = input("Введите автора книги: ").strip()
    

    while True:
        year_input = input("Введите год издания книги: ").strip()
        if year_input.isdigit():
            year = int(year_input)
            if year > 0:
                break
            else:
                print("Ошибка: Год должен быть положительным числом!")
        else:
            print("Ошибка: Введите корректный год (только цифры)!")
    
    
    return title, author, year


def print_books(books_list):
    if not books_list:
        print_message("Список книг пуст.")
        return print(f"НАЙДЕНО КНИГ: {len(books_list)}")
    
    for i, book in enumerate(books_list, 1):
        print(f"{i}. {book}")


def print_message(message):
    print(f"*** {message} ***")