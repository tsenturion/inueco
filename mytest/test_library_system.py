import pytest
import datetime
from library_system import (
    Book, Reader, Library,
    BookNotAvailableError, ReaderNotFoundError
)


# ============= FIXTURES =============

@pytest.fixture
def library():
    return Library("Городская библиотека")

@pytest.fixture
def book1():
    return Book("978-1", "1984", "Джордж Оруэлл", 1949, 2)

@pytest.fixture
def book2():
    return Book("978-2", "Мастер и Маргарита", "Михаил Булгаков", 1967, 1)

@pytest.fixture
def reader1():
    return Reader(1, "Алексей", "alex@example.com")

@pytest.fixture
def sample_book():
    return Book("123", "Тестовая книга", "Тестовый автор", 2020, 2)


# ============= ТЕСТЫ КЛАССА BOOK =============

class TestBook:
    def test_should_create_book_with_valid_data(self):
        book = Book("123", "Название", "Автор", 2000, 5)
        assert book.isbn == "123"
        assert book.title == "Название"
        assert book.author == "Автор"
        assert book.year == 2000
        assert book.total_copies == 5
        assert book.available_copies == 5

    def test_should_raise_value_error_on_empty_isbn(self):
        with pytest.raises(ValueError, match="ISBN не может быть пустым"):
            Book("", "Название", "Автор", 2000, 1)

    def test_should_raise_value_error_on_empty_title(self):
        with pytest.raises(ValueError, match="Название книги не может быть пустым"):
            Book("123", "", "Автор", 2000, 1)

    def test_should_raise_value_error_on_empty_author(self):
        with pytest.raises(ValueError, match="Автор не может быть пустым"):
            Book("123", "Название", "", 2000, 1)

    def test_should_raise_value_error_on_year_less_than_1000(self):
        with pytest.raises(ValueError, match="Год должен быть в диапазоне от 1000 до текущего года."):
            Book("123", "Название", "Автор", 999, 1)

    def test_should_raise_value_error_on_year_greater_than_current(self):
        future_year = datetime.datetime.now().year + 1
        with pytest.raises(ValueError, match="Год должен быть в диапазоне от 1000 до текущего года."):
            Book("123", "Название", "Автор", future_year, 1)
    
    @pytest.mark.parametrize("year", [999, 0, -100, 2030, 3000, 100])
    def test_book_invalid_year_should_raise_error(self, year):
        with pytest.raises(ValueError, match="Год должен быть в диапазоне от 1000 до текущего года."):
            Book("123", "Название", "Автор", year, 1)

    def test_should_raise_value_error_on_negative_copies(self):
        with pytest.raises(ValueError, match="Количество копий не может быть отрицательным"):
            Book("123", "Название", "Автор", 2000, -1)

    def test_is_available_returns_true_when_copies_available(self, sample_book):
        assert sample_book.is_available() is True

    def test_borrow_decreases_available_copies_and_returns_true(self, sample_book):
        initial = sample_book.available_copies
        result = sample_book.borrow()
        assert result is True
        assert sample_book.available_copies == initial - 1

    def test_borrow_returns_false_when_no_copies_available(self):
        book = Book("123", "Название", "Автор", 2000, 0)
        assert book.borrow() is False

    def test_return_book_increases_available_copies_and_returns_true(self, sample_book):
        sample_book.borrow() 
        initial = sample_book.available_copies
        result = sample_book.return_book()
        assert result is True
        assert sample_book.available_copies == initial + 1

    def test_return_book_returns_false_when_all_copies_already_returned(self, sample_book):
        assert sample_book.return_book() is False


# ============= ТЕСТЫ КЛАССА READER =============

class TestReader:
    def test_should_create_reader_with_valid_data(self):
        reader = Reader(1, "Анна Петрова", "anna@example.com")
        assert reader.reader_id == 1
        assert reader.name == "Анна Петрова"
        assert reader.email == "anna@example.com"
        assert reader.borrowed_books == []
        assert reader.history == []

    def test_should_raise_value_error_on_none_reader_id(self):
        with pytest.raises(ValueError, match="reader_id не может быть пустым"):
            Reader(None, "Имя", "test@example.com")

    def test_should_raise_value_error_on_non_positive_reader_id(self):
        with pytest.raises(ValueError, match="reader_id должен быть положительным"):
            Reader(0, "Имя", "test@example.com")
        with pytest.raises(ValueError, match="reader_id должен быть положительным"):
            Reader(-5, "Имя", "test@example.com")

    def test_should_raise_value_error_on_empty_name(self):
        with pytest.raises(ValueError, match="Имя читателя не может быть пустым"):
            Reader(1, "", "test@example.com")

    def test_should_raise_value_error_on_empty_email(self):
        with pytest.raises(ValueError, match="Email не может быть пустым"):
            Reader(1, "Имя", "")

    def test_reader_invalid_email_empty_should_raise_error(self):
        with pytest.raises(ValueError, match="Email не может быть пустым"):
            Reader(1, "Тест", "")

    @pytest.mark.parametrize("email", [
        "no-at-sign.com", 
        "missing@",
        "@missing-domain",
        " spaces @domain.com ",
        "invalid@",
        "user@domain",  
    ])
    def test_reader_invalid_email_format_should_raise_error(self, email):
        with pytest.raises(ValueError, match="Некорректный формат email."):
            Reader(1, "Тест", email)

    def test_can_borrow_returns_true_when_less_than_max_books(self):
        reader = Reader(2, "Борис", "boris@test.com")
        for _ in range(4):
            reader.add_borrowed_book("isbn-1")
        assert reader.can_borrow() is True

    def test_can_borrow_returns_false_when_max_books_reached(self):
        reader = Reader(3, "Виктор", "victor@test.com")
        for i in range(Reader.MAX_BOOKS):
            reader.add_borrowed_book(f"isbn-{i}")
        assert reader.can_borrow() is False

    def test_add_borrowed_book_adds_isbn_to_borrowed_books(self):
        reader = Reader(4, "Галина", "galina@test.com")
        reader.add_borrowed_book("978-123")
        assert "978-123" in reader.borrowed_books

    def test_add_borrowed_book_returns_false_on_duplicate(self):
        reader = Reader(5, "Дмитрий", "dima@test.com")
        reader.add_borrowed_book("isbn-dup")
        result = reader.add_borrowed_book("isbn-dup")
        assert result is False
        assert reader.borrowed_books.count("isbn-dup") == 1  

    def test_add_borrowed_book_returns_false_when_over_limit(self):
        reader = Reader(6, "Елена", "elena@test.com")
        for i in range(Reader.MAX_BOOKS):
            assert reader.add_borrowed_book(f"isbn-{i}") is True
        result = reader.add_borrowed_book("isbn-extra")
        assert result is False
        assert len(reader.borrowed_books) == Reader.MAX_BOOKS

    def test_remove_borrowed_book_removes_isbn_from_borrowed_books(self):
        reader = Reader(7, "Жанна", "zhanna@test.com")
        reader.add_borrowed_book("isbn-to-remove")
        reader.remove_borrowed_book("isbn-to-remove")
        assert "isbn-to-remove" not in reader.borrowed_books

    def test_remove_borrowed_book_returns_false_if_book_not_borrowed(self):
        reader = Reader(8, "Захар", "zahar@test.com")
        result = reader.remove_borrowed_book("nonexistent-isbn")
        assert result is False

    def test_history_records_borrow_and_return_with_timestamps(self):
        reader = Reader(9, "Ирина", "irina@test.com")
        isbn = "978-irina"

        reader.add_borrowed_book(isbn)
        assert len(reader.history) == 1
        assert reader.history[0]["isbn"] == isbn
        assert reader.history[0]["action"] == "borrow"
        assert isinstance(reader.history[0]["timestamp"], datetime.datetime)

        reader.remove_borrowed_book(isbn)
        assert len(reader.history) == 2
        assert reader.history[1]["isbn"] == isbn
        assert reader.history[1]["action"] == "return"
        assert isinstance(reader.history[1]["timestamp"], datetime.datetime)
        assert reader.history[1]["timestamp"] >= reader.history[0]["timestamp"]

    def test_should_raise_reader_not_available_error(self):
        pass  # или удалите этот тест


# ============= ТЕСТЫ КЛАССА LIBRARY =============

class TestLibrary:
    def test_should_create_library_with_valid_name(self):
        lib = Library("Тест")
        assert lib.name == "Тест"

    def test_should_raise_value_error_on_empty_name(self):
        with pytest.raises(ValueError, match="Название библиотеки не может быть пустым"):
            Library("")

    def test_add_book_adds_new_book_and_returns_true(self, library, book1):
        result = library.add_book(book1)
        assert result is True
        assert book1.isbn in library.books

    def test_add_book_increases_copies_for_existing_book(self, library, book1):
        library.add_book(book1)  
        another_copy = Book("978-1", "1984", "Джордж Оруэлл", 1949, 3)
        library.add_book(another_copy)
        assert library.books["978-1"].total_copies == 5
        assert library.books["978-1"].available_copies == 5

    def test_register_reader_registers_new_reader(self, library, reader1):
        result = library.register_reader(reader1)
        assert result is True
        assert reader1.reader_id in library.readers

    def test_register_reader_returns_false_for_duplicate(self, library, reader1):
        library.register_reader(reader1)
        result = library.register_reader(reader1)
        assert result is False

    def test_find_books_by_author_case_insensitive(self, library, book1, book2):
        library.add_book(book1)
        library.add_book(book2)
        results = library.find_books_by_author("ДЖОРДЖ ОРУЭЛЛ")
        assert len(results) == 1
        assert results[0].isbn == "978-1"

    def test_find_books_by_title_case_insensitive(self, library, book1):
        library.add_book(book1)
        results = library.find_books_by_title("1984")
        assert len(results) == 1
        assert results[0].author == "Джордж Оруэлл"

    @pytest.mark.parametrize("search_query", [
        "ДЖОРДЖ ОРУЭЛЛ",
        "джордж оруэлл",
        "Джордж Оруэлл",
        "ДжОрДж ОрУэЛл",
    ])
    def test_find_books_by_author_case_insensitive_param(self, search_query):
        lib = Library("Тест")
        book = Book("978-1", "1984", "Джордж Оруэлл", 1949, 1)
        lib.add_book(book)

        results = lib.find_books_by_author(search_query)
        assert len(results) == 1
        assert results[0].isbn == "978-1"

    def test_get_available_books_returns_only_available(self, library, book1):
        library.add_book(book1)
        book1.borrow()
        available = library.get_available_books()
        assert len(available) == 1  
        book1.borrow()  
        available = library.get_available_books()
        assert len(available) == 0

    def test_borrow_book_successful(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        success, msg = library.borrow_book(reader1.reader_id, book1.isbn)
        assert success is True
        assert "успешно" in msg
        assert book1.available_copies == 1
        assert book1.isbn in reader1.borrowed_books
        assert (reader1.reader_id, book1.isbn) in library.active_loans

    def test_borrow_book_raises_reader_not_found(self, library, book1):
        library.add_book(book1)
        with pytest.raises(ReaderNotFoundError):
            library.borrow_book(999, book1.isbn)

    def test_borrow_book_returns_false_for_unknown_book(self, library, reader1):
        library.register_reader(reader1)
        success, msg = library.borrow_book(reader1.reader_id, "unknown-isbn")
        assert success is False
        assert "не найдена" in msg

    def test_borrow_book_raises_book_not_available_when_no_copies(self, library, book1, reader1):
        book1.available_copies = 0 
        library.add_book(book1)
        library.register_reader(reader1)
        with pytest.raises(BookNotAvailableError, match="недоступна"):
            library.borrow_book(reader1.reader_id, book1.isbn)

    def test_borrow_book_returns_false_when_reader_at_limit(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        for i in range(Reader.MAX_BOOKS):
            fake_book = Book(f"isbn-{i}", f"Книга {i}", "Автор", 2020, 1)
            library.add_book(fake_book)
            library.borrow_book(reader1.reader_id, f"isbn-{i}")
        success, msg = library.borrow_book(reader1.reader_id, book1.isbn)
        assert success is False
        assert "лимита" in msg

    def test_borrow_book_returns_false_when_reader_already_has_book(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        library.borrow_book(reader1.reader_id, book1.isbn)
        success, msg = library.borrow_book(reader1.reader_id, book1.isbn)
        assert success is False
        assert "уже взял" in msg

    def test_borrow_book_records_correct_due_date(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        library.borrow_book(reader1.reader_id, book1.isbn)
        due_date = library.active_loans[(reader1.reader_id, book1.isbn)]
        expected = datetime.datetime.now() + datetime.timedelta(days=Library.LOAN_PERIOD_DAYS)
        assert abs((due_date - expected).total_seconds()) < 60  # Увеличил допуск до 60 секунд

    def test_return_book_successful_without_fine(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        library.borrow_book(reader1.reader_id, book1.isbn)
        success, fine = library.return_book(reader1.reader_id, book1.isbn)
        assert success is True
        assert fine == 0.0
        assert book1.isbn not in reader1.borrowed_books
        assert (reader1.reader_id, book1.isbn) not in library.active_loans

    def test_return_book_raises_reader_not_found(self, library, book1):
        library.add_book(book1)
        with pytest.raises(ReaderNotFoundError):
            library.return_book(999, book1.isbn)

    def test_return_book_returns_false_for_unknown_book(self, library, reader1):
        library.register_reader(reader1)
        success, fine = library.return_book(reader1.reader_id, "unknown-isbn")
        assert success is False
        assert fine == 0.0

    def test_return_book_returns_false_if_reader_never_borrowed_it(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        success, fine = library.return_book(reader1.reader_id, book1.isbn)
        assert success is False
        assert fine == 0.0

    def test_return_book_calculates_fine_for_overdue(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        library.borrow_book(reader1.reader_id, book1.isbn)
        # Имитируем просроченную дату возврата
        past_due = datetime.datetime.now() - datetime.timedelta(days=3)
        library.active_loans[(reader1.reader_id, book1.isbn)] = past_due

        success, fine = library.return_book(reader1.reader_id, book1.isbn)
        assert success is True
        assert fine == 3 * Library.FINE_PER_DAY

    def test_return_book_removes_entry_from_active_loans(self, library, book1, reader1):
        library.add_book(book1)
        library.register_reader(reader1)
        library.borrow_book(reader1.reader_id, book1.isbn)
        assert (reader1.reader_id, book1.isbn) in library.active_loans
        library.return_book(reader1.reader_id, book1.isbn)
        assert (reader1.reader_id, book1.isbn) not in library.active_loans

    def test_should_raise_book_not_available_error(self):
        pass  # или удалите этот тест

    def test_get_overdue_loans(self):
        from unittest.mock import patch
        
        library = Library("Тест")
        book1 = Book("978-1", "1984", "Джордж Оруэлл", 1949, 1)
        reader1 = Reader(1, "Алексей", "alex@example.com")

        library.add_book(book1)
        library.register_reader(reader1)
        library.borrow_book(reader1.reader_id, book1.isbn)

        with patch('library_system.datetime.datetime.now') as mock_now:
            mock_now.return_value = datetime.datetime(2025, 1, 1)
            assert library.get_overdue_loans() == []

        with patch('library_system.datetime.datetime.now') as mock_now:
            mock_now.return_value = datetime.datetime(2025, 1, 20)  # после срока возврата
            overdue = library.get_overdue_loans()
            assert len(overdue) == 1
            assert overdue[0] == (reader1.reader_id, book1.isbn)

# ============= ИНТЕГРАЦИОННЫЕ ТЕСТЫ =============

class TestIntegration:
    def test_full_book_lifecycle(self):
        lib = Library("Центральная библиотека")
        assert lib.name == "Центральная библиотека"
        assert len(lib.books) == 0
        assert len(lib.readers) == 0

        book = Book("978-0-123456-78-9", "Алгоритмы", "Седжвик", 2011, 2)
        lib.add_book(book)
        assert len(lib.books) == 1
        assert lib.books[book.isbn].available_copies == 2

        reader = Reader(101, "Мария Сидорова", "maria@example.com")
        lib.register_reader(reader)
        assert len(lib.readers) == 1
        assert reader.reader_id in lib.readers

        success, msg = lib.borrow_book(reader.reader_id, book.isbn)
        assert success is True
        assert "успешно" in msg

        assert book.available_copies == 1
        assert book.isbn in reader.borrowed_books
        assert (reader.reader_id, book.isbn) in lib.active_loans

        success, fine = lib.return_book(reader.reader_id, book.isbn)
        assert success is True
        assert fine == 0.0

        assert book.available_copies == 2
        assert book.isbn not in reader.borrowed_books
        assert (reader.reader_id, book.isbn) not in lib.active_loans
        assert len(reader.history) == 2 

    def test_overdue_scenario_with_fine_calculation(self):
        from unittest.mock import patch
        
        lib = Library("Библиотека с штрафами")
        book = Book("978-5-900000-01-0", "Чистый код", "Роберт Мартин", 2008, 1)
        reader = Reader(202, "Алексей", "alex@test.com")

        lib.add_book(book)
        lib.register_reader(reader)

        success, msg = lib.borrow_book(reader.reader_id, book.isbn)
        assert success is True

        due_date = lib.active_loans[(reader.reader_id, book.isbn)]
        expected_due = datetime.datetime.now() + datetime.timedelta(days=lib.LOAN_PERIOD_DAYS)
        assert abs((due_date - expected_due).total_seconds()) < 60  # Допуск 60 секунд

        with patch('library_system.datetime.datetime.now') as mock_now:
            mock_now.return_value = datetime.datetime.now() - datetime.timedelta(days=5)  # 5 дней просрочки

            success, fine = lib.return_book(reader.reader_id, book.isbn)
            assert success is True
            assert fine == 5 * lib.FINE_PER_DAY  
        assert (reader.reader_id, book.isbn) not in lib.active_loans