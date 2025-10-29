def input_book_data():

    try:
        title = input("Введите название: ").strip()
        if not title:
            print("Название не может быть пустым!")
            return None
        
        author = input("Введите автора: ").strip()
        if not author:
            print("Автор не может быть пустым!")
            return None
        
        year_str = input("Введите год издания: ").strip()
        year = int(year_str)
        
        if year < 0 or year > 2024:  # Предполагаем, что год не может быть в будущем
            print("Некорректный год издания!")
            return None
        
        return title, author, year
    
    except ValueError:
        print("Ошибка: год должен быть числом!")
        return None

def print_books(books_list):

    if not books_list:
        print("Список книг пуст.")
        return
    
    print(f"\nНайдено книг: {len(books_list)}")
    for i, book in enumerate(books_list, 1):
        print(f"{i}. {book}")

def print_message(message):

    print(f"\n*** {message} ***\n")

def input_with_validation(prompt, validation_func=None):

    while True:
        value = input(prompt).strip()
        if not value:
            print("Поле не может быть пустым!")
            continue
        if validation_func and not validation_func(value):
            continue
        return value

def validate_year(year_str):

    try:
        year = int(year_str)
        if 0 < year <= 2024:
            return True
        else:
            print("Некорректный год! Год должен быть между 1 и 2024.")
            return False
    except ValueError:
        print("Ошибка: год должен быть числом!")
        return False