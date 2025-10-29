def input_book_data() -> tuple:
    title = input("Введите название: ").strip()
    author = input("Введите автора: ").strip()
    
    while True:
        try:
            year = int(input("Введите год издания: "))
            if year < 0 or year > 2100:
                print("Пожалуйста, введите корректный год (0-2100).")
                continue
            break
        except ValueError:
            print("Ошибка! Год должен быть целым числом. Попробуйте снова.")
    
    return title, author, year


def print_books(books_list: list) -> None:
    if not books_list:
        print("Список книг пуст.")
        return
    
    for i, book in enumerate(books_list, 1):
        print(f"{i}. {book}")


def print_message(message: str) -> None:
    print(f"*** {message} ***")