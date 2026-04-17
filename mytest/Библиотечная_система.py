#Система управления библиотекой


from datetime import datetime, timedelta
from typing import Optional, List, Dict, Tuple


class BookNotAvailableError(Exception):
    pass

class ReaderNotFoundError(Exception):
    pass

class Book:    
    def __init__(self, isbn: str, title: str, author: str, year: int, copies: int = 1):
        if not isbn or not title or not author:
            raise ValueError("ISBN, название и автор обязательны")
        if year < 1000 or year > datetime.now().year:
            raise ValueError(f"Некорректный год издания: {year}")
        if copies < 0:
            raise ValueError("Количество копий не может быть отрицательным")
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.total_copies = copies
        self.available_copies = copies
    
    def is_available(self) -> bool:
        return self.available_copies > 0
        
    def borrow(self) -> bool:
        if self.is_available():
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self) -> bool:
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def __repr__(self):
        return f"Book('{self.title}' by {self.author}, {self.available_copies}/{self.total_copies})"

class Reader:    
    MAX_BOOKS = 5
    def __init__(self, reader_id: str, name: str, email: str):
        if not reader_id or not name or not email:
            raise ValueError("ID, имя и email обязательны")
        if '@' not in email:
            raise ValueError("Некорректный email")
        
        self.reader_id = reader_id
        self.name = name
        self.email = email
        self.borrowed_books: List[str] = []
        self.history: List[Tuple[str, str, datetime]] = []  
    
    def can_borrow(self) -> bool:
        return len(self.borrowed_books) < self.MAX_BOOKS
    
    def add_borrowed_book(self, isbn: str) -> bool:
        if self.can_borrow() and isbn not in self.borrowed_books:
            self.borrowed_books.append(isbn)
            self.history.append((isbn, 'borrowed', datetime.now()))
            return True
        return False
    
    def remove_borrowed_book(self, isbn: str) -> bool:
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            self.history.append((isbn, 'returned', datetime.now()))
            return True
        return False
    
    def __repr__(self):
        return f"Reader('{self.name}', books: {len(self.borrowed_books)})"

class Library:    
    LOAN_PERIOD_DAYS = 14
    FINE_PER_DAY = 10.0
    def __init__(self, name: str):
        if not name:
            raise ValueError("Название библиотеки обязательно")
        self.name = name
        self.books: Dict[str, Book] = {}
        self.readers: Dict[str, Reader] = {}
        self.active_loans: Dict[Tuple[str, str], datetime] = {}  
    
    def add_book(self, book: Book) -> bool:
        if book.isbn in self.books:
            existing = self.books[book.isbn]
            existing.total_copies += book.total_copies
            existing.available_copies += book.available_copies
            return False
        else:
            self.books[book.isbn] = book
            return True
    
    def register_reader(self, reader: Reader) -> bool:
        if reader.reader_id in self.readers:
            return False
        self.readers[reader.reader_id] = reader
        return True
    
    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books.values() 
                if author.lower() in book.author.lower()]
    
    
    def find_books_by_title(self, title: str) -> List[Book]:
        return [book for book in self.books.values() 
                if title.lower() in book.title.lower()]
    
    def get_available_books(self) -> List[Book]:
        return [book for book in self.books.values() if book.is_available()]
    
    def borrow_book(self, reader_id: str, isbn: str) -> Tuple[bool, str]:
        if reader_id not in self.readers:
            raise ReaderNotFoundError(f"Читатель {reader_id} не найден")
        
        if isbn not in self.books:
            return False, f"Книга с ISBN {isbn} не найдена"
        reader = self.readers[reader_id]
        book = self.books[isbn]
        
        if not reader.can_borrow():
            return False, f"Читатель достиг лимита книг ({Reader.MAX_BOOKS})"
        
        if not book.is_available():
            raise BookNotAvailableError(f"Книга '{book.title}' недоступна")
        
        if (reader_id, isbn) in self.active_loans:
            return False, "Эта книга уже взята данным читателем"
        
        if book.borrow() and reader.add_borrowed_book(isbn):
            due_date = datetime.now() + timedelta(days=self.LOAN_PERIOD_DAYS)
            self.active_loans[(reader_id, isbn)] = due_date
            return True, f"Книга выдана до {due_date.strftime('%Y-%m-%d')}"
        return False, "Ошибка при выдаче книги"
    
    def return_book(self, reader_id: str, isbn: str) -> Tuple[bool, float]:
        if reader_id not in self.readers:
            raise ReaderNotFoundError(f"Читатель {reader_id} не найден")
        
        if isbn not in self.books:
            return False, 0.0
        loan_key = (reader_id, isbn)
        
        if loan_key not in self.active_loans:
            return False, 0.0
        reader = self.readers[reader_id]
        book = self.books[isbn]
        due_date = self.active_loans[loan_key]
        fine = self.calculate_fine(due_date)
        if book.return_book() and reader.remove_borrowed_book(isbn):
            del self.active_loans[loan_key]
            return True, fine
        return False, 0.0
    
    def calculate_fine(self, due_date: datetime) -> float:
        now = datetime.now()
        
        if now <= due_date:
            return 0.0
        overdue_days = (now - due_date).days
        return overdue_days * self.FINE_PER_DAY
    
    def get_overdue_loans(self) -> List[Tuple[str, str, int, float]]:
        now = datetime.now()
        overdue = []
        
        for (reader_id, isbn), due_date in self.active_loans.items():
            if now > due_date:
                days = (now - due_date).days
                fine = self.calculate_fine(due_date)
                overdue.append((reader_id, isbn, days, fine))
        return sorted(overdue, key=lambda x: x[2], reverse=True)
    
    def get_reader_stats(self, reader_id: str) -> Dict:
        if reader_id not in self.readers:
            raise ReaderNotFoundError(f"Читатель {reader_id} не найден")
        reader = self.readers[reader_id]
        borrowed_count = len([h for h in reader.history if h[1] == 'borrowed'])
        returned_count = len([h for h in reader.history if h[1] == 'returned'])
        total_fine = sum(
            self.calculate_fine(due_date) 
            for (rid, isbn), due_date in self.active_loans.items() 
            if rid == reader_id
        )
        return {
            'name': reader.name,
            'currently_borrowed': len(reader.borrowed_books),
            'total_borrowed': borrowed_count,
            'total_returned': returned_count,
            'current_fines': total_fine
        }
    
    def get_popular_books(self, top_n: int = 5) -> List[Tuple[Book, int]]:
        borrow_counts: Dict[str, int] = {}
        for reader in self.readers.values():
            for isbn, action, _ in reader.history:
                if action == 'borrowed':
                    borrow_counts[isbn] = borrow_counts.get(isbn, 0) + 1
        sorted_books = sorted(
            [(self.books[isbn], count) for isbn, count in borrow_counts.items() 
             if isbn in self.books],
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_books[:top_n]


def create_sample_library() -> Library:
    lib = Library("Городская библиотека")
    
    books = [
        Book("978-0-545-01022-1", "Гарри Поттер и Дары Смерти", "Дж.К. Роулинг", 2007, 3),
        Book("978-5-17-084716-3", "Мастер и Маргарита", "М.А. Булгаков", 1967, 2),
        Book("978-5-389-01006-7", "1984", "Джордж Оруэлл", 1949, 2),
    ]
    
    for book in books:
        lib.add_book(book)
    readers = [
        Reader("R001", "Иван Иванов", "ivan@example.com"),
        Reader("R002", "Мария Петрова", "maria@example.com"),
    ]
    for reader in readers:
        lib.register_reader(reader)
    return lib

if __name__ == "__main__":
    library = create_sample_library()
    
    print(f"Библиотека: {library.name}")
    print(f"Книг в каталоге: {len(library.books)}")
    print(f"Зарегистрировано читателей: {len(library.readers)}")
    
    success, msg = library.borrow_book("R001", "978-0-545-01022-1")
    print(f"\nВыдача книги: {success}, {msg}")
    
    stats = library.get_reader_stats("R001")
    print(f"\nСтатистика читателя: {stats}")
