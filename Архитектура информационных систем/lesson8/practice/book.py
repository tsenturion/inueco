class Book:
    def __init__(self, title, author, year, is_available=True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow(self):
        if not self.is_available:
            print(f'Книга "{self.title}" уже выдана.')
            return False
        self.is_available = False
        return True

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Доступна" if self.is_available else "Выдана"
        return f'Название: "{self.title}", Автор: {self.author}, Год: {self.year}, Статус: {status}'