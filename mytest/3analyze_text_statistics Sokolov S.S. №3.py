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
    return Book("978-3-16-148410-0", "Test Book", "Test Author", 2020, 5, 3)


@pytest.fixture
def sample_reader():
    """Фикстура для создания тестового читателя"""
    return Reader("R001", "John Doe", "john@example.com")


@pytest.fixture
def empty_library():
    """Фикстура для создания пустой библиотеки"""
    return Library("City Library")


@pytest.fixture
def library_with_data():
    """Фикстура для создания библиотеки с предзаполненными данными"""
    library = Library("City Library")
    
    # Добавляем книги
    library.add_book("978-3-16-148410-0", "Python Programming", "John Smith", 2020, 3)
    library.add_book("978-1-23-456789-0", "Data Science", "Jane Doe", 2021, 2)
    library.add_book("978-0-12-345678-9", "Algorithms", "Bob Johnson", 2019, 1)
    
    # Регистрируем читателей
    library.register_reader("R001", "Alice Brown", "alice@example.com")
    library.register_reader("R002", "Charlie Green", "charlie@example.com")
    
    return library


# ============= ТЕСТЫ КЛАССА BOOK =============

class TestBook:
    """Тесты для класса Book"""
    
    def test_should_create_book_with_valid_data(self):
        """Корректное создание объекта книги с валидными данными"""
        book = Book("978-3-16-148410-0", "Test Book", "Test Author", 2020, 5, 3)
        
        assert book.isbn == "978-3-16-148410-0"
        assert book.title == "Test Book"
        assert book.author == "Test Author"
        assert book.year == 2020
        assert book.total_copies == 5
        assert book.available_copies == 3
    
    @pytest.mark.parametrize("isbn", ["", "   ", None])
    def test_should_raise_error_for_empty_isbn(self, isbn):
        """Валидация: пустой ISBN должен вызывать ValueError"""
        with pytest.raises(ValueError, match="ISBN cannot be empty"):
            Book(isbn, "Title", "Author", 2020, 5, 3)
    
    @pytest.mark.parametrize("title", ["", "   ", None])
    def test_should_raise_error_for_empty_title(self, title):
        """Валидация: пустое название должно вызывать ValueError"""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Book("978-3-16-148410-0", title, "Author", 2020, 5, 3)
    
    @pytest.mark.parametrize("author", ["", "   ", None])
    def test_should_raise_error_for_empty_author(self, author):
        """Валидация: пустой автор должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Author cannot be empty"):
            Book("978-3-16-148410-0", "Title", author, 2020, 5, 3)
    
    @pytest.mark.parametrize("year", [999, 2030, -100, 0])
    def test_should_raise_error_for_invalid_year(self, year):
        """Валидация: некорректный год должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Invalid year"):
            Book("978-3-16-148410-0", "Title", "Author", year, 5, 3)
    
    @pytest.mark.parametrize("copies", [-1, -5, -10])
    def test_should_raise_error_for_negative_copies(self, copies):
        """Валидация: отрицательное количество копий должно вызывать ValueError"""
        with pytest.raises(ValueError, match="Number of copies cannot be negative"):
            Book("978-3-16-148410-0", "Title", "Author", 2020, copies, 3)
    
    def test_is_available_should_return_true_when_copies_available(self, sample_book):
        """Метод is_available() возвращает True когда есть доступные копии"""
        assert sample_book.is_available() is True
    
    def test_is_available_should_return_false_when_no_copies_available(self):
        """Метод is_available() возвращает False когда нет доступных копий"""
        book = Book("978-3-16-148410-0", "Test Book", "Test Author", 2020, 5, 0)
        assert book.is_available() is False
    
    def test_borrow_should_decrease_available_copies_and_return_true(self, sample_book):
        """Метод borrow() уменьшает available_copies и возвращает True"""
        initial_copies = sample_book.available_copies
        result = sample_book.borrow()
        
        assert result is True
        assert sample_book.available_copies == initial_copies - 1
    
    def test_borrow_should_return_false_when_no_copies_available(self):
        """Метод borrow() возвращает False когда нет доступных копий"""
        book = Book("978-3-16-148410-0", "Test Book", "Test Author", 2020, 5, 0)
        result = book.borrow()
        
        assert result is False
        assert book.available_copies == 0
    
    def test_return_book_should_increase_available_copies_and_return_true(self, sample_book):
        """Метод return_book() увеличивает available_copies и возвращает True"""
        sample_book.borrow()  # Сначала берем книгу
        initial_copies = sample_book.available_copies
        result = sample_book.return_book()
        
        assert result is True
        assert sample_book.available_copies == initial_copies + 1
    
    def test_return_book_should_return_false_when_all_copies_returned(self):
        """Метод return_book() возвращает False когда все копии уже возвращены"""
        book = Book("978-3-16-148410-0", "Test Book", "Test Author", 2020, 5, 5)
        result = book.return_book()
        
        assert result is False
        assert book.available_copies == 5


# ============= ТЕСТЫ КЛАССА READER =============

class TestReader:
    """Тесты для класса Reader"""
    
    def test_should_create_reader_with_valid_data(self):
        """Корректное создание читателя с валидными данными"""
        reader = Reader("R001", "John Doe", "john@example.com")
        
        assert reader.reader_id == "R001"
        assert reader.name == "John Doe"
        assert reader.email == "john@example.com"
        assert reader.borrowed_books == set()
        assert isinstance(reader.history, list)
    
    @pytest.mark.parametrize("reader_id", ["", "   ", None])
    def test_should_raise_error_for_empty_reader_id(self, reader_id):
        """Валидация: пустой reader_id должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Reader ID cannot be empty"):
            Reader(reader_id, "John Doe", "john@example.com")
    
    @pytest.mark.parametrize("name", ["", "   ", None])
    def test_should_raise_error_for_empty_name(self, name):
        """Валидация: пустое имя должно вызывать ValueError"""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Reader("R001", name, "john@example.com")
    
    @pytest.mark.parametrize("email", ["", "   ", None])
    def test_should_raise_error_for_empty_email(self, email):
        """Валидация: пустой email должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Email cannot be empty"):
            Reader("R001", "John Doe", email)
    
    @pytest.mark.parametrize("email", ["invalid", "invalid@", "@domain.com", "no.at.sign"])
    def test_should_raise_error_for_invalid_email_format(self, email):
        """Валидация: email без символа '@' должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Invalid email format"):
            Reader("R001", "John Doe", email)
    
    def test_can_borrow_should_return_true_when_below_limit(self, sample_reader):
        """Метод can_borrow() возвращает True когда у читателя меньше MAX_BOOKS"""
        # Добавляем несколько книг, но не достигаем лимита
        sample_reader.add_borrowed_book("ISBN1")
        sample_reader.add_borrowed_book("ISBN2")
        
        assert sample_reader.can_borrow() is True
    
    def test_can_borrow_should_return_false_when_limit_reached(self, sample_reader):
        """Метод can_borrow() возвращает False когда достигнут лимит"""
        # Добавляем максимальное количество книг
        for i in range(5):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        
        assert sample_reader.can_borrow() is False
    
    def test_add_borrowed_book_should_add_isbn_to_borrowed_books(self, sample_reader):
        """Метод add_borrowed_book() добавляет ISBN в borrowed_books"""
        result = sample_reader.add_borrowed_book("ISBN001")
        
        assert result is True
        assert "ISBN001" in sample_reader.borrowed_books
        assert len(sample_reader.history) > 0
    
    def test_add_borrowed_book_should_return_false_for_duplicate(self, sample_reader):
        """Метод add_borrowed_book() возвращает False при попытке добавить дубликат"""
        sample_reader.add_borrowed_book("ISBN001")
        result = sample_reader.add_borrowed_book("ISBN001")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == 1
    
    def test_add_borrowed_book_should_return_false_when_limit_exceeded(self, sample_reader):
        """Метод add_borrowed_book() возвращает False при превышении лимита"""
        # Добавляем максимальное количество книг
        for i in range(5):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        
        # Попытка добавить шестую книгу
        result = sample_reader.add_borrowed_book("ISBN5")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == 5
    
    def test_remove_borrowed_book_should_remove_isbn_from_borrowed_books(self, sample_reader):
        """Метод remove_borrowed_book() удаляет ISBN из borrowed_books"""
        sample_reader.add_borrowed_book("ISBN001")
        result = sample_reader.remove_borrowed_book("ISBN001")
        
        assert result is True
        assert "ISBN001" not in sample_reader.borrowed_books
    
    def test_remove_borrowed_book_should_return_false_when_book_not_found(self, sample_reader):
        """Метод remove_borrowed_book() возвращает False если книги нет в списке"""
        result = sample_reader.remove_borrowed_book("NONEXISTENT")
        
        assert result is False
    
    def test_history_should_record_operations_with_timestamps(self, sample_reader):
        """История (history) корректно записывает операции с временными метками"""
        sample_reader.add_borrowed_book("ISBN001")
        sample_reader.remove_borrowed_book("ISBN001")
        
        assert len(sample_reader.history) == 2
        assert "borrowed" in sample_reader.history[0].lower()
        assert "returned" in sample_reader.history[1].lower()


# ============= ТЕСТЫ КЛАССА LIBRARY =============

class TestLibrary:
    """Тесты для класса Library"""
    
    def test_should_create_library_with_valid_name(self):
        """Корректное создание библиотеки"""
        library = Library("City Library")
        
        assert library.name == "City Library"
        assert library.books == {}
        assert library.readers == {}
        assert library.active_loans == {}
    
    @pytest.mark.parametrize("name", ["", "   ", None])
    def test_should_raise_error_for_empty_library_name(self, name):
        """Валидация: пустое название библиотеки должно вызывать ValueError"""
        with pytest.raises(ValueError, match="Library name cannot be empty"):
            Library(name)
    
    def test_add_book_should_add_new_book_and_return_true(self, empty_library):
        """Метод add_book() добавляет новую книгу и возвращает True"""
        result = empty_library.add_book("978-3-16-148410-0", "Python", "Author", 2020, 3)
        
        assert result is True
        assert "978-3-16-148410-0" in empty_library.books
        assert empty_library.books["978-3-16-148410-0"].title == "Python"
    
    def test_add_book_should_increase_copies_for_existing_book(self, empty_library):
        """Метод add_book() увеличивает количество копий для существующей книги"""
        # Добавляем книгу первый раз
        empty_library.add_book("978-3-16-148410-0", "Python", "Author", 2020, 3)
        initial_copies = empty_library.books["978-3-16-148410-0"].total_copies
        
        # Добавляем ту же книгу снова
        result = empty_library.add_book("978-3-16-148410-0", "Python", "Author", 2020, 2)
        
        assert result is True
        assert empty_library.books["978-3-16-148410-0"].total_copies == initial_copies + 2
    
    def test_register_reader_should_register_new_reader(self, empty_library):
        """Метод register_reader() регистрирует нового читателя"""
        result = empty_library.register_reader("R001", "John Doe", "john@example.com")
        
        assert result is True
        assert "R001" in empty_library.readers
        assert empty_library.readers["R001"].name == "John Doe"
    
    def test_register_reader_should_return_false_for_duplicate(self, empty_library):
        """Метод register_reader() возвращает False для дубликата"""
        empty_library.register_reader("R001", "John Doe", "john@example.com")
        result = empty_library.register_reader("R001", "Jane Doe", "jane@example.com")
        
        assert result is False
    
    def test_find_books_by_author_should_find_books_case_insensitive(self, library_with_data):
        """Метод find_books_by_author() находит книги (регистронезависимый поиск)"""
        books_lower = library_with_data.find_books_by_author("john smith")
        books_upper = library_with_data.find_books_by_author("JOHN SMITH")
        
        assert len(books_lower) > 0
        assert len(books_upper) > 0
        assert books_lower[0].author == "John Smith"
    
    def test_find_books_by_title_should_find_books_case_insensitive(self, library_with_data):
        """Метод find_books_by_title() находит книги (регистронезависимый поиск)"""
        books_lower = library_with_data.find_books_by_title("python")
        books_upper = library_with_data.find_books_by_title("PYTHON")
        
        assert len(books_lower) > 0
        assert len(books_upper) > 0
        assert books_lower[0].title == "Python Programming"
    
    def test_get_available_books_should_return_only_available_books(self, library_with_data):
        """Метод get_available_books() возвращает только доступные книги"""
        available_books = library_with_data.get_available_books()
        
        for book in available_books:
            assert book.available_copies > 0
    
    def test_borrow_book_should_successfully_loan_book_to_reader(self, library_with_data):
        """Успешная выдача книги читателю"""
        result, message = library_with_data.borrow_book("R001", "978-3-16-148410-0")
        
        assert result is True
        assert "successfully" in message.lower()
        assert "R001" in library_with_data.active_loans
        assert "978-3-16-148410-0" in library_with_data.active_loans["R001"]
    
    def test_borrow_book_should_raise_reader_not_found_error(self, library_with_data):
        """Выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError):
            library_with_data.borrow_book("NONEXISTENT", "978-3-16-148410-0")
    
    def test_borrow_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Возврат (False, message) для несуществующей книги"""
        result, message = library_with_data.borrow_book("R001", "NONEXISTENT_ISBN")
        
        assert result is False
        assert "not found" in message.lower()
    
    def test_borrow_book_should_raise_book_not_available_error(self, library_with_data):
        """Выброс BookNotAvailableError когда книга недоступна"""
        # Создаем книгу с 0 доступных копий
        library_with_data.add_book("978-0-00-000000-0", "Unavailable", "Author", 2020, 0)
        
        with pytest.raises(BookNotAvailableError):
            library_with_data.borrow_book("R001", "978-0-00-000000-0")
    
    def test_borrow_book_should_return_false_when_reader_reached_limit(self, library_with_data):
        """Возврат (False, message) когда читатель достиг лимита книг"""
        # Выдаем максимальное количество книг
        isbns = ["978-3-16-148410-0", "978-1-23-456789-0", "978-0-12-345678-9"]
        for isbn in isbns[:2]:  # Выдаем 2 книги
            library_with_data.borrow_book("R001", isbn)
        
        # Добавляем еще книги для достижения лимита
        library_with_data.add_book("ISBN1", "Book1", "Author", 2020, 1)
        library_with_data.add_book("ISBN2", "Book2", "Author", 2020, 1)
        library_with_data.add_book("ISBN3", "Book3", "Author", 2020, 1)
        
        library_with_data.borrow_book("R001", "ISBN1")
        library_with_data.borrow_book("R001", "ISBN2")
        
        # Попытка взять шестую книгу
        result, message = library_with_data.borrow_book("R001", "ISBN3")
        
        assert result is False
        assert "limit" in message.lower()
    
    def test_borrow_book_should_return_false_when_reader_already_has_book(self, library_with_data):
        """Возврат (False, message) когда читатель уже взял эту книгу"""
        library_with_data.borrow_book("R001", "978-3-16-148410-0")
        result, message = library_with_data.borrow_book("R001", "978-3-16-148410-0")
        
        assert result is False
        assert "already" in message.lower()
    
    def test_borrow_book_should_add_record_to_active_loans_with_due_date(self, library_with_data):
        """Проверка добавления записи в active_loans с корректной датой возврата"""
        from datetime import datetime, timedelta
        
        result, message = library_with_data.borrow_book("R001", "978-3-16-148410-0")
        
        assert result is True
        assert "R001" in library_with_data.active_loans
        assert "978-3-16-148410-0" in library_with_data.active_loans["R001"]
        
        loan_info = library_with_data.active_loans["R001"]["978-3-16-148410-0"]
        assert "borrow_date" in loan_info
        assert "due_date" in loan_info
        
        expected_due_date = loan_info["borrow_date"] + timedelta(days=14)
        assert loan_info["due_date"] == expected_due_date
    
    def test_return_book_should_successfully_return_book_without_fine(self, library_with_data):
        """Успешный возврат книги без штрафа (в срок)"""
        library_with_data.borrow_book("R001", "978-3-16-148410-0")
        result, fine = library_with_data.return_book("R001", "978-3-16-148410-0")
        
        assert result is True
        assert fine == 0.0
        assert "978-3-16-148410-0" not in library_with_data.active_loans.get("R001", {})
    
    def test_return_book_should_raise_reader_not_found_error(self, library_with_data):
        """Выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError):
            library_with_data.return_book("NONEXISTENT", "978-3-16-148410-0")
    
    def test_return_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Возврат (False, 0.0) для несуществующей книги"""
        result, fine = library_with_data.return_book("R001", "NONEXISTENT_ISBN")
        
        assert result is False
        assert fine == 0.0
    
    def test_return_book_should_return_false_when_book_not_borrowed(self, library_with_data):
        """Возврат (False, 0.0) если эта книга не была взята читателем"""
        result, fine = library_with_data.return_book("R001", "978-3-16-148410-0")
        
        assert result is False
        assert fine == 0.0
    
    def test_calculate_fine_should_return_zero_for_non_overdue_loan(self, library_with_data):
        """Метод calculate_fine() возвращает 0 для непросроченного займа"""
        library_with_data.borrow_book("R001", "978-3-16-148410-0")
        fine = library_with_data.calculate_fine("R001", "978-3-16-148410-0")
        
        assert fine == 0.0
    
    def test_calculate_fine_should_calculate_fine_correctly(self, library_with_data, monkeypatch):
        """Метод calculate_fine() корректно рассчитывает штраф (дни * FINE_PER_DAY)"""
        # Подменяем текущее время для эмуляции просрочки
        class MockDatetime:
            @staticmethod
            def now():
                return datetime(2025, 1, 1)
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        # Создаем займ с просрочкой 5 дней
        library_with_data.active_loans["R001"] = {
            "978-3-16-148410-0": {
                "borrow_date": datetime(2024, 12, 15),
                "due_date": datetime(2024, 12, 27)  # 5 дней просрочки
            }
        }
        
        fine = library_with_data.calculate_fine("R001", "978-3-16-148410-0")
        expected_fine = 5 * 10.0  # 5 дней * 10.0 за день
        
        assert fine == pytest.approx(expected_fine)
    
    def test_get_overdue_loans_should_return_overdue_loans(self, library_with_data, monkeypatch):
        """Метод get_overdue_loans() возвращает список просроченных займов"""
        # Подменяем текущее время
        class MockDatetime:
            @staticmethod
            def now():
                return datetime(2025, 1, 1)
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        # Создаем просроченный займ
        library_with_data.active_loans["R001"] = {
            "978-3-16-148410-0": {
                "borrow_date": datetime(2024, 12, 15),
                "due_date": datetime(2024, 12, 27)  # Просрочен
            }
        }
        
        overdue_loans = library_with_data.get_overdue_loans()
        
        assert len(overdue_loans) > 0
        assert "R001" in overdue_loans
        assert "978-3-16-148410-0" in overdue_loans["R001"]
    
    def test_get_reader_stats_should_return_correct_statistics(self, library_with_data):
        """Метод get_reader_stats() возвращает корректную статистику"""
        # Выдаем несколько книг
        library_with_data.borrow_book("R001", "978-3-16-148410-0")
        library_with_data.borrow_book("R001", "978-1-23-456789-0")
        
        stats = library_with_data.get_reader_stats("R001")
        
        assert "borrowed_count" in stats
        assert "history_count" in stats
        assert stats["borrowed_count"] == 2
    
    def test_get_reader_stats_should_raise_reader_not_found_error(self, library_with_data):
        """Метод get_reader_stats() выбрасывает ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError):
            library_with_data.get_reader_stats("NONEXISTENT")
    
    def test_get_popular_books_should_return_top_popular_books(self, library_with_data):
        """Метод get_popular_books() возвращает топ популярных книг"""
        # Выдаем книги несколько раз для создания статистики популярности
        library_with_data.borrow_book("R001", "978-3-16-148410-0")
        library_with_data.borrow_book("R002", "978-3-16-148410-0")
        library_with_data.return_book("R001", "978-3-16-148410-0")
        library_with_data.borrow_book("R001", "978-3-16-148410-0")
        
        popular_books = library_with_data.get_popular_books(limit=2)
        
        assert len(popular_books) <= 2
        if len(popular_books) > 0:
            assert popular_books[0][0] == "978-3-16-148410-0"


# ============= ИНТЕГРАЦИОННЫЕ ТЕСТЫ =============

class TestIntegration:
    """Интеграционные тесты"""
    
    def test_full_book_lifecycle(self, empty_library):
        """Полный цикл работы с книгой"""
        # Создание библиотеки
        library = empty_library
        
        # Добавление книги
        library.add_book("978-3-16-148410-0", "Python Programming", "John Smith", 2020, 3)
        
        # Регистрация читателя
        library.register_reader("R001", "Alice Brown", "alice@example.com")
        
        # Проверка начальной статистики
        initial_stats = library.get_reader_stats("R001")
        assert initial_stats["borrowed_count"] == 0
        
        # Выдача книги
        result, message = library.borrow_book("R001", "978-3-16-148410-0")
        assert result is True
        
        # Проверка статистики после выдачи
        stats_after_borrow = library.get_reader_stats("R001")
        assert stats_after_borrow["borrowed_count"] == 1
        
        # Возврат книги
        result, fine = library.return_book("R001", "978-3-16-148410-0")
        assert result is True
        assert fine == 0.0
        
        # Проверка финальной статистики
        final_stats = library.get_reader_stats("R001")
        assert final_stats["borrowed_count"] == 0
        assert final_stats["history_count"] > 0
    
    def test_overdue_scenario_with_fine(self, empty_library, monkeypatch):
        """Сценарий с просрочкой возврата и расчетом штрафа"""
        # Настройка мок-даты для просрочки
        class MockDatetime:
            borrow_date = datetime(2024, 12, 15)
            
            @classmethod
            def now(cls):
                return datetime(2025, 1, 1)  # 15 дней просрочки
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        library = empty_library
        
        # Добавление книги и регистрация читателя
        library.add_book("978-3-16-148410-0", "Python Programming", "John Smith", 2020, 3)
        library.register_reader("R001", "Alice Brown", "alice@example.com")
        
        # Выдача книги (с мок-датой)
        library.borrow_book("R001", "978-3-16-148410-0")
        
        # Проверка расчета штрафа
        fine = library.calculate_fine("R001", "978-3-16-148410-0")
        expected_fine = 15 * 10.0  # 15 дней * 10.0 за день
        assert fine == pytest.approx(expected_fine)
        
        # Возврат с штрафом
        result, actual_fine = library.return_book("R001", "978-3-16-148410-0")
        assert result is True
        assert actual_fine == pytest.approx(expected_fine)
        
        # Проверка, что займ удален из активных
        assert "R001" not in library.active_loans or "978-3-16-148410-0" not in library.active_loans.get("R001", {})