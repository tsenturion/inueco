"""
Тесты для системы управления библиотекой
"""
import pytest
from datetime import datetime, timedelta
from library_system import (
    Book, Reader, Library,
    BookNotAvailableError, ReaderNotFoundError
)


# ============= FIXTURES =============

@pytest.fixture
def sample_book():
    """Фикстура для создания тестовой книги"""
    return Book(isbn="978-0134685991", title="Effective Python", author="Brett Slatkin", year=2019, total_copies=3)


@pytest.fixture
def sample_reader():
    """Фикстура для создания тестового читателя"""
    return Reader(reader_id="R001", name="Alice Smith", email="alice@example.com")


@pytest.fixture
def empty_library():
    """Фикстура для создания пустой библиотеки"""
    return Library("City Library")


@pytest.fixture
def library_with_data():
    """Фикстура для создания библиотеки с предзаполненными данными"""
    lib = Library("Central Library")
    book1 = Book("978-0134685991", "Effective Python", "Brett Slatkin", 2019, 2)
    book2 = Book("978-1491946008", "Fluent Python", "Luciano Ramalho", 2015, 1)
    lib.add_book(book1)
    lib.add_book(book2)
    reader = Reader("R001", "Alice Smith", "alice@example.com")
    lib.register_reader(reader)
    return lib


# ============= ТЕСТЫ КЛАССА BOOK =============

class TestBook:
    def test_should_create_book_with_valid_data(self):
        book = Book("978-0134685991", "Effective Python", "Brett Slatkin", 2019, 5)
        assert book.isbn == "978-0134685991"
        assert book.title == "Effective Python"
        assert book.author == "Brett Slatkin"
        assert book.year == 2019
        assert book.total_copies == 5
        assert book.available_copies == 5

    def test_should_raise_value_error_for_empty_isbn(self):
        with pytest.raises(ValueError, match="ISBN не может быть пустым"):
            Book("", "Effective Python", "Brett Slatkin", 2019, 5)

    def test_should_raise_value_error_for_empty_title(self):
        with pytest.raises(ValueError, match="Название не может быть пустым"):
            Book("978-0134685991", "", "Brett Slatkin", 2019, 5)

    def test_should_raise_value_error_for_empty_author(self):
        with pytest.raises(ValueError, match="Автор не может быть пустым"):
            Book("978-0134685991", "Effective Python", "", 2019, 5)

    @pytest.mark.parametrize("year", [999, 2030, -100, 0, 3000])
    def test_should_raise_value_error_for_invalid_year(self, year):
        with pytest.raises(ValueError, match="Год должен быть между 1000 и текущим годом"):
            Book("978-0134685991", "Effective Python", "Brett Slatkin", year, 5)

    def test_should_raise_value_error_for_negative_copies(self):
        with pytest.raises(ValueError, match="Количество копий не может быть отрицательным"):
            Book("978-0134685991", "Effective Python", "Brett Slatkin", 2019, -1)

    def test_should_return_true_when_available_copies_exist(self, sample_book):
        assert sample_book.is_available() is True

    def test_should_return_false_when_no_available_copies(self):
        book = Book("978-0134685991", "Effective Python", "Brett Slatkin", 2019, 1)
        book.borrow()
        assert book.is_available() is False

    def test_borrow_should_decrease_available_copies_and_return_true(self, sample_book):
        initial_copies = sample_book.available_copies
        result = sample_book.borrow()
        assert result is True
        assert sample_book.available_copies == initial_copies - 1

    def test_borrow_should_return_false_when_no_copies_available(self):
        book = Book("978-0134685991", "Effective Python", "Brett Slatkin", 2019, 1)
        book.borrow()
        result = book.borrow()
        assert result is False

    def test_return_book_should_increase_available_copies_and_return_true(self, sample_book):
        sample_book.borrow()
        initial_copies = sample_book.available_copies
        result = sample_book.return_book()
        assert result is True
        assert sample_book.available_copies == initial_copies + 1

    def test_return_book_should_return_false_when_all_copies_already_returned(self, sample_book):
        result = sample_book.return_book()
        assert result is False


# ============= ТЕСТЫ КЛАССА READER =============

class TestReader:
    def test_should_create_reader_with_valid_data(self):
        reader = Reader("R001", "Alice Smith", "alice@example.com")
        assert reader.reader_id == "R001"
        assert reader.name == "Alice Smith"
        assert reader.email == "alice@example.com"
        assert reader.borrowed_books == []
        assert reader.history == []

    def test_should_raise_value_error_for_empty_reader_id(self):
        with pytest.raises(ValueError, match="ID читателя не может быть пустым"):
            Reader("", "Alice Smith", "alice@example.com")

    def test_should_raise_value_error_for_empty_name(self):
        with pytest.raises(ValueError, match="Имя не может быть пустым"):
            Reader("R001", "", "alice@example.com")

    def test_should_raise_value_error_for_empty_email(self):
        with pytest.raises(ValueError, match="Email не может быть пустым"):
            Reader("R001", "Alice Smith", "")

    @pytest.mark.parametrize("email", ["invalid-email", "no-at-symbol.com", "@", "test@"])
    def test_should_raise_value_error_for_invalid_email(self, email):
        with pytest.raises(ValueError, match="Некорректный email"):
            Reader("R001", "Alice Smith", email)

    def test_can_borrow_should_return_true_when_below_limit(self, sample_reader):
        for _ in range(4):
            sample_reader.add_borrowed_book("ISBN123")
        assert sample_reader.can_borrow() is True

    def test_can_borrow_should_return_false_when_at_limit(self, sample_reader):
        for i in range(5):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        assert sample_reader.can_borrow() is False

    def test_add_borrowed_book_should_add_isbn_to_list(self, sample_reader):
        sample_reader.add_borrowed_book("ISBN123")
        assert "ISBN123" in sample_reader.borrowed_books

    def test_add_borrowed_book_should_return_false_for_duplicate(self, sample_reader):
        sample_reader.add_borrowed_book("ISBN123")
        result = sample_reader.add_borrowed_book("ISBN123")
        assert result is False

    def test_add_borrowed_book_should_return_false_when_over_limit(self, sample_reader):
        for i in range(5):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        result = sample_reader.add_borrowed_book("ISBN6")
        assert result is False

    def test_remove_borrowed_book_should_remove_isbn_from_list(self, sample_reader):
        sample_reader.add_borrowed_book("ISBN123")
        result = sample_reader.remove_borrowed_book("ISBN123")
        assert result is True
        assert "ISBN123" not in sample_reader.borrowed_books

    def test_remove_borrowed_book_should_return_false_if_not_in_list(self, sample_reader):
        result = sample_reader.remove_borrowed_book("ISBN123")
        assert result is False

    def test_history_should_record_operations_with_timestamps(self, sample_reader):
        initial_len = len(sample_reader.history)
        sample_reader.add_borrowed_book("ISBN123")
        assert len(sample_reader.history) == initial_len + 1
        assert "borrow" in sample_reader.history[-1]
        assert "ISBN123" in sample_reader.history[-1]

        sample_reader.remove_borrowed_book("ISBN123")
        assert len(sample_reader.history) == initial_len + 2
        assert "return" in sample_reader.history[-1]
        assert "ISBN123" in sample_reader.history[-1]


# ============= ТЕСТЫ КЛАССА LIBRARY =============

class TestLibrary:
    def test_should_create_library_with_valid_name(self):
        lib = Library("City Library")
        assert lib.name == "City Library"
        assert lib.books == {}
        assert lib.readers == {}
        assert lib.active_loans == {}

    def test_should_raise_value_error_for_empty_library_name(self):
        with pytest.raises(ValueError, match="Название библиотеки не может быть пустым"):
            Library("")

    def test_add_book_should_add_new_book_and_return_true(self, empty_library, sample_book):
        result = empty_library.add_book(sample_book)
        assert result is True
        assert sample_book.isbn in empty_library.books

    def test_add_book_should_increase_copies_for_existing_book(self, empty_library, sample_book):
        empty_library.add_book(sample_book)
        new_book = Book(sample_book.isbn, "Different Title", "Different Author", 2020, 2)
        result = empty_library.add_book(new_book)
        assert result is True
        assert empty_library.books[sample_book.isbn].total_copies == sample_book.total_copies + 2
        assert empty_library.books[sample_book.isbn].available_copies == sample_book.available_copies + 2

    def test_register_reader_should_register_new_reader(self, empty_library, sample_reader):
        result = empty_library.register_reader(sample_reader)
        assert result is True
        assert sample_reader.reader_id in empty_library.readers

    def test_register_reader_should_return_false_for_duplicate(self, empty_library, sample_reader):
        empty_library.register_reader(sample_reader)
        result = empty_library.register_reader(sample_reader)
        assert result is False

    def test_find_books_by_author_should_find_case_insensitive(self, library_with_data):
        results = library_with_data.find_books_by_author("brett slatkin")
        assert len(results) == 1
        assert results[0].author == "Brett Slatkin"

    def test_find_books_by_title_should_find_case_insensitive(self, library_with_data):
        results = library_with_data.find_books_by_title("effective python")
        assert len(results) == 1
        assert results[0].title == "Effective Python"

    def test_get_available_books_should_return_only_available_books(self, library_with_data):
        # Borrow the only copy of Fluent Python
        library_with_data.borrow_book("R001", "978-1491946008")
        available = library_with_data.get_available_books()
        assert len(available) == 1
        assert available[0].isbn == "978-0134685991"

    def test_borrow_book_should_successfully_lend_book(self, library_with_data):
        success, message = library_with_data.borrow_book("R001", "978-0134685991")
        assert success is True
        assert "успешно" in message.lower()
        assert "978-0134685991" in library_with_data.readers["R001"].borrowed_books
        assert (library_with_data.active_loans["R001"]["978-0134685991"] - datetime.now()).days == 14

    def test_borrow_book_should_raise_reader_not_found_error_for_nonexistent_reader(self, empty_library, sample_book):
        empty_library.add_book(sample_book)
        with pytest.raises(ReaderNotFoundError):
            empty_library.borrow_book("R999", "978-0134685991")

    def test_borrow_book_should_return_false_for_nonexistent_book(self, library_with_data):
        success, message = library_with_data.borrow_book("R001", "NONEXISTENT")
        assert success is False
        assert "не найдена" in message

    def test_borrow_book_should_raise_book_not_available_error_when_no_copies(self, library_with_data):
        # Borrow the only copy
        library_with_data.borrow_book("R001", "978-1491946008")
        # Try to borrow again
        success, message = library_with_data.borrow_book("R001", "978-1491946008")
        assert success is False
        assert "недоступна" in message

    def test_borrow_book_should_return_false_when_reader_at_limit(self, empty_library):
        # Create a reader and add 5 books
        reader = Reader("R001", "Alice", "alice@example.com")
        empty_library.register_reader(reader)
        for i in range(5):
            book = Book(f"ISBN{i}", f"Book {i}", "Author", 2020, 1)
            empty_library.add_book(book)
            empty_library.borrow_book("R001", f"ISBN{i}")
        
        # Try to borrow a 6th book
        extra_book = Book("EXTRA", "Extra Book", "Author", 2020, 1)
        empty_library.add_book(extra_book)
        success, message = empty_library.borrow_book("R001", "EXTRA")
        assert success is False
        assert "достигнут лимит" in message

    def test_borrow_book_should_return_false_when_reader_already_has_book(self, library_with_data):
        library_with_data.borrow_book("R001", "978-0134685991")
        success, message = library_with_data.borrow_book("R001", "978-0134685991")
        assert success is False
        assert "уже взята" in message

    def test_return_book_should_successfully_return_without_fine(self, library_with_data):
        library_with_data.borrow_book("R001", "978-0134685991")
        success, fine = library_with_data.return_book("R001", "978-0134685991")
        assert success is True
        assert fine == pytest.approx(0.0)
        assert "978-0134685991" not in library_with_data.readers["R001"].borrowed_books
        assert ("R001", "978-0134685991") not in [
            (rid, isbn) for rid, loans in library_with_data.active_loans.items() for isbn in loans
        ]

    def test_return_book_should_raise_reader_not_found_error_for_nonexistent_reader(self, empty_library, sample_book):
        empty_library.add_book(sample_book)
        with pytest.raises(ReaderNotFoundError):
            empty_library.return_book("R999", "978-0134685991")

    def test_return_book_should_return_false_for_nonexistent_book(self, library_with_data):
        success, fine = library_with_data.return_book("R001", "NONEXISTENT")
        assert success is False
        assert fine == pytest.approx(0.0)

    def test_return_book_should_return_false_if_reader_never_borrowed_book(self, library_with_data):
        success, fine = library_with_data.return_book("R001", "978-1491946008")
        assert success is False
        assert fine == pytest.approx(0.0)

    def test_calculate_fine_should_return_zero_for_on_time_return(self, library_with_data):
        library_with_data.borrow_book("R001", "978-0134685991")
        fine = library_with_data.calculate_fine("R001", "978-0134685991")
        assert fine == pytest.approx(0.0)

    def test_calculate_fine_should_correctly_calculate_overdue_fine(self, library_with_data, monkeypatch):
        library_with_data.borrow_book("R001", "978-0134685991")
        
        # Mock current time to be 5 days overdue
        due_date = library_with_data.active_loans["R001"]["978-0134685991"]
        mock_now = due_date + timedelta(days=5)
        
        class MockDatetime:
            @staticmethod
            def now():
                return mock_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        fine = library_with_data.calculate_fine("R001", "978-0134685991")
        assert fine == pytest.approx(5 * Library.FINE_PER_DAY)

    def test_get_overdue_loans_should_return_overdue_loans_list(self, library_with_data, monkeypatch):
        library_with_data.borrow_book("R001", "978-0134685991")
        
        # Mock current time to be 1 day overdue
        due_date = library_with_data.active_loans["R001"]["978-0134685991"]
        mock_now = due_date + timedelta(days=1)
        
        class MockDatetime:
            @staticmethod
            def now():
                return mock_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        overdue = library_with_data.get_overdue_loans()
        assert len(overdue) == 1
        assert overdue[0]["reader_id"] == "R001"
        assert overdue[0]["isbn"] == "978-0134685991"

    def test_get_reader_stats_should_return_correct_statistics(self, library_with_data):
        stats = library_with_data.get_reader_stats("R001")
        assert stats["reader_id"] == "R001"
        assert stats["total_borrowed"] == 0
        assert stats["currently_borrowed"] == 0
        assert stats["history_length"] == 0

    def test_get_reader_stats_should_raise_reader_not_found_error(self, empty_library):
        with pytest.raises(ReaderNotFoundError):
            empty_library.get_reader_stats("R999")

    def test_get_popular_books_should_return_top_popular_books(self, library_with_data):
        # Borrow books multiple times
        library_with_data.borrow_book("R001", "978-0134685991")
        library_with_data.return_book("R001", "978-0134685991")
        library_with_data.borrow_book("R001", "978-0134685991")
        library_with_data.return_book("R001", "978-0134685991")
        
        popular = library_with_data.get_popular_books(top_n=1)
        assert len(popular) == 1
        assert popular[0]["isbn"] == "978-0134685991"
        assert popular[0]["borrow_count"] == 2


# ============= ИНТЕГРАЦИОННЫЕ ТЕСТЫ =============

class TestIntegration:
    def test_full_book_lifecycle(self):
        """Полный жизненный цикл работы с книгой: добавление, выдача, возврат, проверка статистики"""
        lib = Library("Test Library")
        
        # Добавление книги
        book = Book("ISBN123", "Test Book", "Test Author", 2020, 2)
        assert lib.add_book(book) is True
        
        # Регистрация читателя
        reader = Reader("R001", "Test Reader", "test@example.com")
        assert lib.register_reader(reader) is True
        
        # Проверка начальной статистики
        stats_before = lib.get_reader_stats("R001")
        assert stats_before["total_borrowed"] == 0
        assert stats_before["currently_borrowed"] == 0
        
        # Выдача книги
        success, message = lib.borrow_book("R001", "ISBN123")
        assert success is True
        
        # Проверка статистики после выдачи
        stats_after_borrow = lib.get_reader_stats("R001")
        assert stats_after_borrow["total_borrowed"] == 1
        assert stats_after_borrow["currently_borrowed"] == 1
        
        # Возврат книги
        success, fine = lib.return_book("R001", "ISBN123")
        assert success is True
        assert fine == pytest.approx(0.0)
        
        # Проверка финальной статистики
        stats_after_return = lib.get_reader_stats("R001")
        assert stats_after_return["total_borrowed"] == 1
        assert stats_after_return["currently_borrowed"] == 0
        
        # Проверка доступности книги
        available_books = lib.get_available_books()
        assert len(available_books) == 1
        assert available_books[0].isbn == "ISBN123"

    def test_overdue_scenario_with_fine_calculation(self, monkeypatch):
        """Сценарий с просрочкой: выдача, эмуляция просрочки, расчет штрафа, возврат"""
        lib = Library("Test Library")
        
        # Настройка данных
        book = Book("ISBN123", "Overdue Book", "Author", 2020, 1)
        reader = Reader("R001", "Overdue Reader", "overdue@example.com")
        lib.add_book(book)
        lib.register_reader(reader)
        
        # Выдача книги
        lib.borrow_book("R001", "ISBN123")
        
        # Эмуляция просрочки на 3 дня
        due_date = lib.active_loans["R001"]["ISBN123"]
        mock_now = due_date + timedelta(days=3)
        
        class MockDatetime:
            @staticmethod
            def now():
                return mock_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        # Проверка штрафа
        fine = lib.calculate_fine("R001", "ISBN123")
        expected_fine = 3 * Library.FINE_PER_DAY
        assert fine == pytest.approx(expected_fine)
        
        # Проверка просроченных займов
        overdue_loans = lib.get_overdue_loans()
        assert len(overdue_loans) == 1
        assert overdue_loans[0]["reader_id"] == "R001"
        assert overdue_loans[0]["days_overdue"] == 3
        
        # Возврат с штрафом
        success, returned_fine = lib.return_book("R001", "ISBN123")
        assert success is True
        assert returned_fine == pytest.approx(expected_fine)
        
        # Проверка, что запись удалена из активных займов
        assert "R001" not in lib.active_loans or "ISBN123" not in lib.active_loans.get("R001", {})
        
        pytest test_library_system.py -v
        pytest test_library_system.py --cov=library_system --cov-report=html

