def input_book_data():
    title = input("Введите название: ").strip()
    author = input("Введите автора: ").strip()
    while True:
        try:
            year = int(input("Введите год издания: "))
            return title, author, year
        except ValueError:
            print("Ошибка! Год должен быть числом.")

def print_books(books_list):
    if not books_list:
        print("Список книг пуст.")
        return
    for book in books_list:
        print(book)

def print_message(message):
    print(f"*** {message} ***")