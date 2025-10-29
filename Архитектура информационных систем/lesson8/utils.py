def input_book_data():
    """    
    Returns:
        tuple: Кортеж (title, author, year) с данными книги
    """
    title = input("Введите название: ").strip()
    author = input("Введите автора: ").strip()
    
    while True:
        year_input = input("Введите год издания: ").strip()
        try:
            year = int(year_input)
            if year > 0:  
                break
            else:
                print("Год должен быть положительным числом.")
        except ValueError:
            print("Ошибка! Год должен быть целым числом.")
    
    return title, author, year

def print_books(books_list):
    """    
    Args:
        books_list (list): Список объектов Book для вывода
    """
    if not books_list:
        print("Книги не найдены.")
        return
    
    for i, book in enumerate(books_list, 1):
        print(f"{i}. {book}")

def print_message(message):
    """    
    Args:
        message (str): Сообщение для вывода
    """
    print(f"*** {message} ***")