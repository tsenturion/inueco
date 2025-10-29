class Library:
    def __init__(self):
        self.books = []
    

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")
    

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{title}' удалена из библиотеки.")
                return
        
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке.")
    

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]
    

    def find_books_by_year(self, year):
        return [book for book in self.books if book.year == year]
    

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return        
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке.")
    

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return        
        print(f"Ошибка: Книга '{title}' не найдена в библиотеке.")
    

    def get_available_books(self):
        return [book for book in self.books if book.is_available]
    

    def get_all_books(self):
        return self.books.copy()
    

    def __str__(self):
        if not self.books:
            return "Библиотека пуста."
        result = "Книги в библиотеке:\n"
        for i, book in enumerate(self.books, 1):
            status = "доступна" if book.is_available else "выдана"
            result += f"{i}. '{book.title}' - {book.author} ({book.year}) - {status}\n"
        return result