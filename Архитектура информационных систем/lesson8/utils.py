def input_book_data():
    """
    Запросить данные книги у пользователя
    
    Returns:
        tuple: Кортеж (title, author, year) или None при ошибке
    """
    try:
        title = input("Введите название: ").strip()
        author = input("Введите автора: ").strip()
        year = int(input("Введите год издания: "))
        
        if not title or not author:
            print("Название и автор не могут быть пустыми!")
            return None
            
        return title, author, year
    except ValueError:
        print("Ошибка: Год издания должен быть числом!")
        return None

def print_books(books_list):
    """
    Вывести список книг
    
    Args:
        books_list (list): Список объектов Book
    """
    if not books_list:
        print("Список книг пуст.")
        return
    
    for i, book in enumerate(books_list, 1):
        print(f"{i}. {book}")

def print_message(message):
    """
    Вывести сообщение с выделением
    
    Args:
        message (str): Сообщение для вывода
    """
    print(f"*** {message} ***")

def input_int(prompt, min_val=None, max_val=None):
    """
    Безопасный ввод целого числа
    
    Args:
        prompt (str): Подсказка для ввода
        min_val (int): Минимальное допустимое значение
        max_val (int): Максимальное допустимое значение
        
    Returns:
        int or None: Введенное число или None при ошибке
    """
    try:
        value = int(input(prompt))
        if min_val is not None and value < min_val:
            print(f"Значение не может быть меньше {min_val}!")
            return None
        if max_val is not None and value > max_val:
            print(f"Значение не может быть больше {max_val}!")
            return None
        return value
    except ValueError:
        print("Ошибка: Введите целое число!")
        return None

def input_non_empty_string(prompt):
    """
    Безопасный ввод непустой строки
    
    Args:
        prompt (str): Подсказка для ввода
        
    Returns:
        str or None: Введенная строка или None если пустая
    """
    value = input(prompt).strip()
    if not value:
        print("Поле не может быть пустым!")
        return None
    return value