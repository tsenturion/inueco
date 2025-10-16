"""
Полное решение тестов для системы управления библиотекой
Покрытие: 40+ тестов, все требования выполнены
"""
import pytest
from datetime import datetime, timedelta
from library_system import (
    Book, Reader, Library,
    BookNotAvailableError, ReaderNotFoundError,
    create_sample_library
)


# ============= FIXTURES =============

@pytest.fixture
def sample_book():
    """Фикстура для создания тестовой книги"""
    return Book(
        isbn="978-0-123456-78-9",
        title="Тестовая книга",
        author="Тестовый Автор",
        year=2020,
        copies=3
    )


@pytest.fixture
def sample_reader():
    """Фикстура для создания тестового читателя"""
    return Reader(
        reader_id="R001",
        name="Иван Тестов",
        email="test@example.com"
    )


@pytest.fixture
def empty_library():
    """Фикстура для создания пустой библиотеки"""
    return Library("Тестовая библиотека")


@pytest.fixture
def library_with_data():
    """Фикстура для создания библиотеки с предзаполненными данными"""
    lib = Library("Городская библиотека")
    
    # Добавляем книги
    books = [
        Book("978-0-545-01022-1", "Гарри Поттер", "Дж.К. Роулинг", 2007, 3),
        Book("978-5-17-084716-3", "Мастер и Маргарита", "М.А. Булгаков", 1967, 2),
        Book("978-5-389-01006-7", "1984", "Джордж Оруэлл", 1949, 2),
    ]
    
    for book in books:
        lib.add_book(book)
    
    # Регистрируем читателей
    readers = [
        Reader("R001", "Иван Иванов", "ivan@example.com"),
        Reader("R002", "Мария Петрова", "maria@example.com"),
        Reader("R003", "Петр Сидоров", "petr@example.com"),
    ]
    
    for reader in readers:
        lib.register_reader(reader)
    
    return lib


@pytest.fixture
def mock_datetime_now(monkeypatch):
    """Фикстура для подмены datetime.now()"""
    class MockDatetime:
        @staticmethod
        def now():
            return datetime(2025, 10, 6, 12, 0, 0)
    
    return MockDatetime


# ============= ТЕСТЫ КЛАССА BOOK =============

class TestBook:
    """Тесты для класса Book"""
    
    def test_should_create_book_with_valid_data(self):
        """Тест: создание книги с корректными данными"""
        book = Book("978-0-123456-78-9", "Название", "Автор", 2020, 5)
        
        assert book.isbn == "978-0-123456-78-9"
        assert book.title == "Название"
        assert book.author == "Автор"
        assert book.year == 2020
        assert book.total_copies == 5
        assert book.available_copies == 5
    
    def test_should_raise_error_for_empty_isbn(self):
        """Тест: пустой ISBN вызывает ValueError"""
        with pytest.raises(ValueError, match="ISBN, название и автор обязательны"):
            Book("", "Название", "Автор", 2020)
    
    def test_should_raise_error_for_empty_title(self):
        """Тест: пустое название вызывает ValueError"""
        with pytest.raises(ValueError, match="ISBN, название и автор обязательны"):
            Book("978-0-123456-78-9", "", "Автор", 2020)
    
    def test_should_raise_error_for_empty_author(self):
        """Тест: пустой автор вызывает ValueError"""
        with pytest.raises(ValueError, match="ISBN, название и автор обязательны"):
            Book("978-0-123456-78-9", "Название", "", 2020)
    
    @pytest.mark.parametrize("year", [999, 2030, -100, 0, 500])
    def test_should_raise_error_for_invalid_year(self, year):
        """Тест: некорректный год вызывает ValueError"""
        with pytest.raises(ValueError, match="Некорректный год издания"):
            Book("978-0-123456-78-9", "Название", "Автор", year)
    
    def test_should_raise_error_for_negative_copies(self):
        """Тест: отрицательное количество копий вызывает ValueError"""
        with pytest.raises(ValueError, match="Количество копий не может быть отрицательным"):
            Book("978-0-123456-78-9", "Название", "Автор", 2020, -1)
    
    def test_is_available_should_return_true_when_copies_available(self, sample_book):
        """Тест: is_available() возвращает True когда есть копии"""
        assert sample_book.is_available() is True
    
    def test_is_available_should_return_false_when_no_copies(self, sample_book):
        """Тест: is_available() возвращает False когда нет копий"""
        sample_book.available_copies = 0
        assert sample_book.is_available() is False
    
    def test_borrow_should_decrease_available_copies(self, sample_book):
        """Тест: borrow() уменьшает количество доступных копий"""
        initial_copies = sample_book.available_copies
        result = sample_book.borrow()
        
        assert result is True
        assert sample_book.available_copies == initial_copies - 1
    
    def test_borrow_should_return_false_when_no_copies(self, sample_book):
        """Тест: borrow() возвращает False когда нет копий"""
        sample_book.available_copies = 0
        result = sample_book.borrow()
        
        assert result is False
        assert sample_book.available_copies == 0
    
    def test_return_book_should_increase_available_copies(self, sample_book):
        """Тест: return_book() увеличивает количество доступных копий"""
        sample_book.borrow()
        initial_copies = sample_book.available_copies
        result = sample_book.return_book()
        
        assert result is True
        assert sample_book.available_copies == initial_copies + 1
    
    def test_return_book_should_return_false_when_all_returned(self, sample_book):
        """Тест: return_book() возвращает False когда все копии возвращены"""
        result = sample_book.return_book()
        
        assert result is False
        assert sample_book.available_copies == sample_book.total_copies


# ============= ТЕСТЫ КЛАССА READER =============

class TestReader:
    """Тесты для класса Reader"""
    
    def test_should_create_reader_with_valid_data(self):
        """Тест: создание читателя с корректными данными"""
        reader = Reader("R001", "Иван Иванов", "ivan@example.com")
        
        assert reader.reader_id == "R001"
        assert reader.name == "Иван Иванов"
        assert reader.email == "ivan@example.com"
        assert reader.borrowed_books == []
        assert reader.history == []
    
    def test_should_raise_error_for_empty_reader_id(self):
        """Тест: пустой reader_id вызывает ValueError"""
        with pytest.raises(ValueError, match="ID, имя и email обязательны"):
            Reader("", "Имя", "email@example.com")
    
    def test_should_raise_error_for_empty_name(self):
        """Тест: пустое имя вызывает ValueError"""
        with pytest.raises(ValueError, match="ID, имя и email обязательны"):
            Reader("R001", "", "email@example.com")
    
    def test_should_raise_error_for_empty_email(self):
        """Тест: пустой email вызывает ValueError"""
        with pytest.raises(ValueError, match="ID, имя и email обязательны"):
            Reader("R001", "Имя", "")
    
    @pytest.mark.parametrize("email", [
        "invalid",
        "invalid.com",
    ])
    def test_should_raise_error_for_invalid_email(self, email):
        """Тест: некорректный email вызывает ValueError"""
        with pytest.raises(ValueError, match="Некорректный email"):
            Reader("R001", "Имя", email)
    
    def test_can_borrow_should_return_true_when_under_limit(self, sample_reader):
        """Тест: can_borrow() возвращает True когда не достигнут лимит"""
        assert sample_reader.can_borrow() is True
    
    def test_can_borrow_should_return_false_when_at_limit(self, sample_reader):
        """Тест: can_borrow() возвращает False при достижении лимита"""
        # Добавляем MAX_BOOKS книг
        for i in range(Reader.MAX_BOOKS):
            sample_reader.borrowed_books.append(f"ISBN-{i}")
        
        assert sample_reader.can_borrow() is False
    
    def test_add_borrowed_book_should_add_isbn_to_list(self, sample_reader):
        """Тест: add_borrowed_book() добавляет ISBN в список"""
        isbn = "978-0-123456-78-9"
        result = sample_reader.add_borrowed_book(isbn)
        
        assert result is True
        assert isbn in sample_reader.borrowed_books
        assert len(sample_reader.borrowed_books) == 1
    
    def test_add_borrowed_book_should_record_history(self, sample_reader):
        """Тест: add_borrowed_book() записывает в историю"""
        isbn = "978-0-123456-78-9"
        sample_reader.add_borrowed_book(isbn)
        
        assert len(sample_reader.history) == 1
        assert sample_reader.history[0][0] == isbn
        assert sample_reader.history[0][1] == 'borrowed'
        assert isinstance(sample_reader.history[0][2], datetime)
    
    def test_add_borrowed_book_should_return_false_for_duplicate(self, sample_reader):
        """Тест: add_borrowed_book() возвращает False для дубликата"""
        isbn = "978-0-123456-78-9"
        sample_reader.add_borrowed_book(isbn)
        result = sample_reader.add_borrowed_book(isbn)
        
        assert result is False
        assert len(sample_reader.borrowed_books) == 1
    
    def test_add_borrowed_book_should_return_false_when_limit_reached(self, sample_reader):
        """Тест: add_borrowed_book() возвращает False при превышении лимита"""
        # Добавляем MAX_BOOKS книг
        for i in range(Reader.MAX_BOOKS):
            sample_reader.add_borrowed_book(f"ISBN-{i}")
        
        result = sample_reader.add_borrowed_book("ISBN-extra")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == Reader.MAX_BOOKS
    
    def test_remove_borrowed_book_should_remove_isbn(self, sample_reader):
        """Тест: remove_borrowed_book() удаляет ISBN из списка"""
        isbn = "978-0-123456-78-9"
        sample_reader.add_borrowed_book(isbn)
        result = sample_reader.remove_borrowed_book(isbn)
        
        assert result is True
        assert isbn not in sample_reader.borrowed_books
    
    def test_remove_borrowed_book_should_record_history(self, sample_reader):
        """Тест: remove_borrowed_book() записывает в историю"""
        isbn = "978-0-123456-78-9"
        sample_reader.add_borrowed_book(isbn)
        sample_reader.remove_borrowed_book(isbn)
        
        assert len(sample_reader.history) == 2
        assert sample_reader.history[1][1] == 'returned'
    
    def test_remove_borrowed_book_should_return_false_if_not_borrowed(self, sample_reader):
        """Тест: remove_borrowed_book() возвращает False если книга не взята"""
        result = sample_reader.remove_borrowed_book("978-0-123456-78-9")
        
        assert result is False


# ============= ТЕСТЫ КЛАССА LIBRARY =============

class TestLibrary:
    """Тесты для класса Library"""
    
    def test_should_create_library_with_valid_name(self):
        """Тест: создание библиотеки с корректным названием"""
        library = Library("Городская библиотека")
        
        assert library.name == "Городская библиотека"
        assert library.books == {}
        assert library.readers == {}
        assert library.active_loans == {}
    
    def test_should_raise_error_for_empty_name(self):
        """Тест: пустое название вызывает ValueError"""
        with pytest.raises(ValueError, match="Название библиотеки обязательно"):
            Library("")
    
    def test_add_book_should_add_new_book(self, empty_library, sample_book):
        """Тест: add_book() добавляет новую книгу"""
        result = empty_library.add_book(sample_book)
        
        assert result is True
        assert sample_book.isbn in empty_library.books
        assert empty_library.books[sample_book.isbn] == sample_book
    
    def test_add_book_should_increase_copies_for_existing_book(self, empty_library):
        """Тест: add_book() увеличивает количество копий для существующей книги"""
        book1 = Book("978-0-123456-78-9", "Название", "Автор", 2020, 2)
        book2 = Book("978-0-123456-78-9", "Название", "Автор", 2020, 3)
        
        empty_library.add_book(book1)
        result = empty_library.add_book(book2)
        
        assert result is False
        assert empty_library.books[book1.isbn].total_copies == 5
        assert empty_library.books[book1.isbn].available_copies == 5
    
    def test_register_reader_should_register_new_reader(self, empty_library, sample_reader):
        """Тест: register_reader() регистрирует нового читателя"""
        result = empty_library.register_reader(sample_reader)
        
        assert result is True
        assert sample_reader.reader_id in empty_library.readers
        assert empty_library.readers[sample_reader.reader_id] == sample_reader
    
    def test_register_reader_should_return_false_for_duplicate(self, empty_library, sample_reader):
        """Тест: register_reader() возвращает False для дубликата"""
        empty_library.register_reader(sample_reader)
        result = empty_library.register_reader(sample_reader)
        
        assert result is False
        assert len(empty_library.readers) == 1
    
    def test_find_books_by_author_should_find_matching_books(self, library_with_data):
        """Тест: find_books_by_author() находит книги по автору"""
        books = library_with_data.find_books_by_author("Роулинг")
        
        assert len(books) == 1
        assert books[0].title == "Гарри Поттер"
    
    def test_find_books_by_author_should_be_case_insensitive(self, library_with_data):
        """Тест: find_books_by_author() регистронезависимый"""
        books = library_with_data.find_books_by_author("оруэлл")
        
        assert len(books) == 1
        assert books[0].author == "Джордж Оруэлл"
    
    def test_find_books_by_title_should_find_matching_books(self, library_with_data):
        """Тест: find_books_by_title() находит книги по названию"""
        books = library_with_data.find_books_by_title("Мастер")
        
        assert len(books) == 1
        assert "Мастер и Маргарита" in books[0].title
    
    @pytest.mark.parametrize("query,expected_count", [
        ("Гарри", 1),
        ("1984", 1),
        ("Мастер", 1),
        ("Несуществующая", 0),
    ])
    def test_find_books_by_title_parametrized(self, library_with_data, query, expected_count):
        """Тест: find_books_by_title() с параметризацией"""
        books = library_with_data.find_books_by_title(query)
        assert len(books) == expected_count
    
    def test_get_available_books_should_return_only_available(self, library_with_data):
        """Тест: get_available_books() возвращает только доступные книги"""
        available = library_with_data.get_available_books()
        
        assert len(available) == 3
        assert all(book.is_available() for book in available)
    
    def test_get_available_books_should_exclude_borrowed(self, library_with_data):
        """Тест: get_available_books() исключает взятые книги"""
        # Берем все копии одной книги
        isbn = "978-5-389-01006-7"
        library_with_data.borrow_book("R001", isbn)
        library_with_data.borrow_book("R002", isbn)
        
        available = library_with_data.get_available_books()
        
        assert len(available) == 2
        assert not any(book.isbn == isbn for book in available)
    
    def test_borrow_book_should_succeed_with_valid_data(self, library_with_data):
        """Тест: успешная выдача книги"""
        success, msg = library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        assert success is True
        assert "Книга выдана до" in msg
        assert ("R001", "978-0-545-01022-1") in library_with_data.active_loans
    
    def test_borrow_book_should_raise_error_for_nonexistent_reader(self, library_with_data):
        """Тест: выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError, match="Читатель R999 не найден"):
            library_with_data.borrow_book("R999", "978-0-545-01022-1")
    
    def test_borrow_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Тест: возврат False для несуществующей книги"""
        success, msg = library_with_data.borrow_book("R001", "978-9-999999-99-9")
        
        assert success is False
        assert "не найдена" in msg
    
    def test_borrow_book_should_raise_error_when_book_unavailable(self, library_with_data):
        """Тест: выброс BookNotAvailableError когда книга недоступна"""
        isbn = "978-5-389-01006-7"
        # Берем все копии
        library_with_data.borrow_book("R001", isbn)
        library_with_data.borrow_book("R002", isbn)
        
        with pytest.raises(BookNotAvailableError, match="недоступна"):
            library_with_data.borrow_book("R003", isbn)
    
    def test_borrow_book_should_fail_when_reader_at_limit(self, library_with_data):
        """Тест: неудача когда читатель достиг лимита"""
        reader = library_with_data.readers["R001"]
        # Добавляем MAX_BOOKS книг вручную
        for i in range(Reader.MAX_BOOKS):
            reader.borrowed_books.append(f"ISBN-{i}")
        
        success, msg = library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        assert success is False
        assert "лимита книг" in msg
    
    def test_borrow_book_should_fail_if_already_borrowed_by_reader(self, library_with_data):
        """Тест: неудача если читатель уже взял эту книгу"""
        isbn = "978-0-545-01022-1"
        library_with_data.borrow_book("R001", isbn)
        
        success, msg = library_with_data.borrow_book("R001", isbn)
        
        assert success is False
        assert "уже взята" in msg
    
    def test_borrow_book_should_set_correct_due_date(self, library_with_data):
        """Тест: выдача книги устанавливает корректную дату возврата"""
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        due_date = library_with_data.active_loans[("R001", "978-0-545-01022-1")]
        expected_date = datetime.now() + timedelta(days=Library.LOAN_PERIOD_DAYS)
        
        # Проверяем с точностью до минуты
        assert abs((due_date - expected_date).total_seconds()) < 60
    
    def test_return_book_should_succeed_with_valid_data(self, library_with_data):
        """Тест: успешный возврат книги"""
        isbn = "978-0-545-01022-1"
        library_with_data.borrow_book("R001", isbn)
        
        success, fine = library_with_data.return_book("R001", isbn)
        
        assert success is True
        assert fine == 0.0
        assert ("R001", isbn) not in library_with_data.active_loans
    
    def test_return_book_should_raise_error_for_nonexistent_reader(self, library_with_data):
        """Тест: выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError, match="Читатель R999 не найден"):
            library_with_data.return_book("R999", "978-0-545-01022-1")
    
    def test_return_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Тест: возврат False для несуществующей книги"""
        success, fine = library_with_data.return_book("R001", "978-9-999999-99-9")
        
        assert success is False
        assert fine == 0.0
    
    def test_return_book_should_return_false_if_not_borrowed(self, library_with_data):
        """Тест: возврат False если книга не была взята"""
        success, fine = library_with_data.return_book("R001", "978-0-545-01022-1")
        
        assert success is False
        assert fine == 0.0
    
    def test_return_book_should_calculate_fine_for_overdue(self, library_with_data, monkeypatch):
        """Тест: расчет штрафа при просрочке"""
        isbn = "978-0-545-01022-1"
        
        # Устанавливаем текущую дату
        class MockDatetime:
            @staticmethod
            def now():
                return datetime(2025, 10, 6, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        library_with_data.borrow_book("R001", isbn)
        
        # Переносим время на 20 дней вперед (6 дней просрочки)
        class MockDatetimeOverdue:
            @staticmethod
            def now():
                return datetime(2025, 10, 26, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeOverdue)
        
        success, fine = library_with_data.return_book("R001", isbn)
        
        assert success is True
        assert fine == pytest.approx(60.0)  # 6 дней * 10.0
    
    def test_calculate_fine_should_return_zero_for_on_time(self, empty_library):
        """Тест: calculate_fine() возвращает 0 для своевременного возврата"""
        due_date = datetime.now() + timedelta(days=1)
        fine = empty_library.calculate_fine(due_date)
        
        assert fine == 0.0
    
    def test_calculate_fine_should_calculate_correct_amount(self, empty_library):
        """Тест: calculate_fine() корректно рассчитывает штраф"""
        due_date = datetime.now() - timedelta(days=5)
        fine = empty_library.calculate_fine(due_date)
        
        assert fine == pytest.approx(50.0)  # 5 дней * 10.0
    
    def test_get_overdue_loans_should_return_overdue_only(self, library_with_data, monkeypatch):
        """Тест: get_overdue_loans() возвращает только просроченные займы"""
        # Устанавливаем начальную дату
        class MockDatetime:
            @staticmethod
            def now():
                return datetime(2025, 10, 1, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        library_with_data.borrow_book("R002", "978-5-17-084716-3")
        
        # Переносим время на 20 дней вперед
        class MockDatetimeOverdue:
            @staticmethod
            def now():
                return datetime(2025, 10, 21, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeOverdue)
        
        overdue = library_with_data.get_overdue_loans()
        
        assert len(overdue) == 2
        # Проверяем структуру (reader_id, isbn, days_overdue, fine)
        assert all(len(item) == 4 for item in overdue)
        assert all(item[2] > 0 for item in overdue)  # дни просрочки > 0
    
    def test_get_reader_stats_should_return_correct_stats(self, library_with_data):
        """Тест: get_reader_stats() возвращает корректную статистику"""
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        library_with_data.borrow_book("R001", "978-5-17-084716-3")
        library_with_data.return_book("R001", "978-0-545-01022-1")
        
        stats = library_with_data.get_reader_stats("R001")
        
        assert stats['name'] == "Иван Иванов"
        assert stats['currently_borrowed'] == 1
        assert stats['total_borrowed'] == 2
        assert stats['total_returned'] == 1
        assert stats['current_fines'] == pytest.approx(0.0)
    
    def test_get_reader_stats_should_raise_error_for_nonexistent_reader(self, library_with_data):
        """Тест: get_reader_stats() выбрасывает ошибку для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError, match="Читатель R999 не найден"):
            library_with_data.get_reader_stats("R999")
    
    def test_get_popular_books_should_return_top_books(self, library_with_data):
        """Тест: get_popular_books() возвращает топ популярных книг"""
        # Создаем историю займов
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        library_with_data.return_book("R001", "978-0-545-01022-1")
        library_with_data.borrow_book("R002", "978-0-545-01022-1")
        library_with_data.borrow_book("R003", "978-5-17-084716-3")
        
        popular = library_with_data.get_popular_books(top_n=2)
        
        assert len(popular) <= 2
        assert popular[0][0].isbn == "978-0-545-01022-1"  # Самая популярная
        assert popular[0][1] == 2  # Взята 2 раза
    
    def test_get_popular_books_should_handle_empty_history(self, empty_library):
        """Тест: get_popular_books() работает с пустой историей"""
        popular = empty_library.get_popular_books()
        
        assert popular == []


# ============= ИНТЕГРАЦИОННЫЕ ТЕСТЫ =============

class TestIntegration:
    """Интеграционные тесты для полных сценариев"""
    
    def test_full_book_lifecycle(self):
        """Тест: полный жизненный цикл работы с книгой"""
        # 1. Создание библиотеки
        library = Library("Тестовая библиотека")
        
        # 2. Добавление книги
        book = Book("978-0-123456-78-9", "Тестовая книга", "Автор", 2020, 2)
        library.add_book(book)
        assert len(library.books) == 1
        
        # 3. Регистрация читателя
        reader = Reader("R001", "Иван Иванов", "ivan@example.com")
        library.register_reader(reader)
        assert len(library.readers) == 1
        
        # 4. Выдача книги
        success, msg = library.borrow_book("R001", "978-0-123456-78-9")
        assert success is True
        assert library.books["978-0-123456-78-9"].available_copies == 1
        
        # 5. Проверка статистики
        stats = library.get_reader_stats("R001")
        assert stats['currently_borrowed'] == 1
        assert stats['total_borrowed'] == 1
        assert stats['total_returned'] == 0
        
        # 6. Возврат книги
        success, fine = library.return_book("R001", "978-0-123456-78-9")
        assert success is True
        assert fine == 0.0
        assert library.books["978-0-123456-78-9"].available_copies == 2
        
        # 7. Проверка обновленной статистики
        stats = library.get_reader_stats("R001")
        assert stats['currently_borrowed'] == 0
        assert stats['total_borrowed'] == 1
        assert stats['total_returned'] == 1
    
    def test_overdue_scenario_with_fine(self, monkeypatch):
        """Тест: сценарий с просрочкой и штрафом"""
        # 1. Создание библиотеки и данных
        library = Library("Библиотека")
        book = Book("978-0-123456-78-9", "Книга", "Автор", 2020, 1)
        reader = Reader("R001", "Читатель", "reader@example.com")
        
        library.add_book(book)
        library.register_reader(reader)
        
        # 2. Устанавливаем начальную дату (1 октября)
        class MockDatetimeBorrow:
            @staticmethod
            def now():
                return datetime(2025, 10, 1, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeBorrow)
        
        # 3. Выдача книги
        success, msg = library.borrow_book("R001", "978-0-123456-78-9")
        assert success is True
        
        # 4. Проверяем дату возврата (должна быть 15 октября)
        due_date = library.active_loans[("R001", "978-0-123456-78-9")]
        expected_due = datetime(2025, 10, 15, 12, 0, 0)
        assert due_date == expected_due
        
        # 5. Переносим время на 25 октября (10 дней просрочки)
        class MockDatetimeReturn:
            @staticmethod
            def now():
                return datetime(2025, 10, 25, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeReturn)
        
        # 6. Проверяем просроченные займы
        overdue = library.get_overdue_loans()
        assert len(overdue) == 1
        assert overdue[0][0] == "R001"
        assert overdue[0][1] == "978-0-123456-78-9"
        assert overdue[0][2] == 10  # дней просрочки
        assert overdue[0][3] == pytest.approx(100.0)  # штраф
        
        # 7. Возврат с штрафом
        success, fine = library.return_book("R001", "978-0-123456-78-9")
        assert success is True
        assert fine == pytest.approx(100.0)  # 10 дней * 10.0
        
        # 8. Проверяем что займ удален
        assert ("R001", "978-0-123456-78-9") not in library.active_loans
    
    def test_multiple_readers_borrowing_same_book(self):
        """Тест: несколько читателей берут одну и ту же книгу"""
        library = Library("Библиотека")
        
        # Книга с 3 копиями
        book = Book("978-0-123456-78-9", "Популярная книга", "Автор", 2020, 3)
        library.add_book(book)
        
        # 3 читателя
        for i in range(1, 4):
            reader = Reader(f"R00{i}", f"Читатель {i}", f"reader{i}@example.com")
            library.register_reader(reader)
        
        # Первый читатель берет книгу
        success, _ = library.borrow_book("R001", "978-0-123456-78-9")
        assert success is True
        assert library.books["978-0-123456-78-9"].available_copies == 2
        
        # Второй читатель берет книгу
        success, _ = library.borrow_book("R002", "978-0-123456-78-9")
        assert success is True
        assert library.books["978-0-123456-78-9"].available_copies == 1
        
        # Третий читатель берет последнюю копию
        success, _ = library.borrow_book("R003", "978-0-123456-78-9")
        assert success is True
        assert library.books["978-0-123456-78-9"].available_copies == 0
        
        # Четвертый читатель не может взять (нет копий)
        reader4 = Reader("R004", "Читатель 4", "reader4@example.com")
        library.register_reader(reader4)
        
        with pytest.raises(BookNotAvailableError):
            library.borrow_book("R004", "978-0-123456-78-9")
        
        # Первый читатель возвращает книгу
        success, _ = library.return_book("R001", "978-0-123456-78-9")
        assert success is True
        assert library.books["978-0-123456-78-9"].available_copies == 1
        
        # Теперь четвертый может взять
        success, _ = library.borrow_book("R004", "978-0-123456-78-9")
        assert success is True
    
    def test_reader_reaching_book_limit(self):
        """Тест: читатель достигает лимита книг"""
        library = Library("Библиотека")
        
        # Добавляем 6 книг
        for i in range(1, 7):
            book = Book(f"978-0-123456-78-{i}", f"Книга {i}", "Автор", 2020, 1)
            library.add_book(book)
        
        # Регистрируем читателя
        reader = Reader("R001", "Читатель", "reader@example.com")
        library.register_reader(reader)
        
        # Берем MAX_BOOKS (5) книг
        for i in range(1, 6):
            success, _ = library.borrow_book("R001", f"978-0-123456-78-{i}")
            assert success is True
        
        # Проверяем что достигнут лимит
        assert not library.readers["R001"].can_borrow()
        
        # Попытка взять 6-ю книгу должна провалиться
        success, msg = library.borrow_book("R001", "978-0-123456-78-6")
        assert success is False
        assert "лимита книг" in msg
        
        # Возвращаем одну книгу
        library.return_book("R001", "978-0-123456-78-1")
        
        # Теперь можем взять другую
        success, _ = library.borrow_book("R001", "978-0-123456-78-6")
        assert success is True
    
    def test_search_and_borrow_workflow(self):
        """Тест: поиск и выдача книги"""
        library = Library("Библиотека")
        
        # Добавляем книги разных авторов
        books = [
            Book("978-1", "Гарри Поттер и философский камень", "Дж.К. Роулинг", 2001, 2),
            Book("978-2", "Гарри Поттер и тайная комната", "Дж.К. Роулинг", 2002, 2),
            Book("978-3", "1984", "Джордж Оруэлл", 1949, 1),
        ]
        
        for book in books:
            library.add_book(book)
        
        # Регистрируем читателя
        reader = Reader("R001", "Читатель", "reader@example.com")
        library.register_reader(reader)
        
        # Ищем книги Роулинг
        rowling_books = library.find_books_by_author("Роулинг")
        assert len(rowling_books) == 2
        
        # Ищем книги про Гарри Поттера
        harry_books = library.find_books_by_title("Гарри Поттер")
        assert len(harry_books) == 2
        
        # Берем первую найденную книгу
        success, _ = library.borrow_book("R001", harry_books[0].isbn)
        assert success is True
        
        # Проверяем доступные книги
        available = library.get_available_books()
        assert len(available) == 3  # одна копия взята, но остались другие
        
        # Ищем самые популярные
        popular = library.get_popular_books(top_n=3)
        assert len(popular) >= 1
        assert popular[0][1] == 1  # взята 1 раз


# ============= ДОПОЛНИТЕЛЬНЫЕ EDGE CASE ТЕСТЫ =============

class TestEdgeCases:
    """Тесты граничных случаев"""
    
    def test_book_with_zero_copies(self):
        """Тест: книга с 0 копий при создании"""
        book = Book("978-0-123456-78-9", "Книга", "Автор", 2020, 0)
        
        assert book.total_copies == 0
        assert book.available_copies == 0
        assert book.is_available() is False
    
    def test_library_with_special_characters_in_name(self):
        """Тест: библиотека с спецсимволами в названии"""
        library = Library("Библиотека №1 «Центральная» (г. Москва)")
        
        assert library.name == "Библиотека №1 «Центральная» (г. Москва)"
    
    def test_reader_with_multiple_at_signs_in_email(self):
        """Тест: email с несколькими @ должен быть валиден"""
        # В реальности email может иметь @ только один раз, но наша простая
        # валидация просто проверяет наличие @
        reader = Reader("R001", "Имя", "test@@example.com")
        assert reader.email == "test@@example.com"
    
    def test_book_title_with_numbers_and_symbols(self):
        """Тест: название книги с цифрами и символами"""
        book = Book("978-0-123456-78-9", "2001: Космическая одиссея", "А. Кларк", 2000, 1)
        
        assert book.title == "2001: Космическая одиссея"
    
    def test_return_same_book_twice(self):
        """Тест: попытка вернуть одну и ту же книгу дважды"""
        library = Library("Библиотека")
        book = Book("978-0-123456-78-9", "Книга", "Автор", 2020, 1)
        reader = Reader("R001", "Читатель", "reader@example.com")
        
        library.add_book(book)
        library.register_reader(reader)
        
        # Берем и возвращаем
        library.borrow_book("R001", "978-0-123456-78-9")
        success1, _ = library.return_book("R001", "978-0-123456-78-9")
        
        # Попытка вернуть снова
        success2, fine2 = library.return_book("R001", "978-0-123456-78-9")
        
        assert success1 is True
        assert success2 is False
        assert fine2 == 0.0
    
    def test_get_popular_books_with_tied_counts(self):
        """Тест: популярные книги с одинаковым количеством займов"""
        library = Library("Библиотека")
        
        # Добавляем 3 книги
        for i in range(1, 4):
            book = Book(f"978-{i}", f"Книга {i}", "Автор", 2020, 2)
            library.add_book(book)
        
        # Добавляем 3 читателей
        for i in range(1, 4):
            reader = Reader(f"R00{i}", f"Читатель {i}", f"reader{i}@example.com")
            library.register_reader(reader)
        
        # Каждый читатель берет свою книгу (по 1 разу каждая)
        library.borrow_book("R001", "978-1")
        library.borrow_book("R002", "978-2")
        library.borrow_book("R003", "978-3")
        
        popular = library.get_popular_books(top_n=3)
        
        # Все три книги должны иметь счетчик 1
        assert len(popular) == 3
        assert all(count == 1 for _, count in popular)
    
    def test_statistics_for_reader_with_no_activity(self):
        """Тест: статистика для читателя без активности"""
        library = Library("Библиотека")
        reader = Reader("R001", "Читатель", "reader@example.com")
        library.register_reader(reader)
        
        stats = library.get_reader_stats("R001")
        
        assert stats['currently_borrowed'] == 0
        assert stats['total_borrowed'] == 0
        assert stats['total_returned'] == 0
        assert stats['current_fines'] == 0.0
    
    def test_very_long_overdue_period(self, monkeypatch):
        """Тест: очень долгая просрочка"""
        library = Library("Библиотека")
        book = Book("978-0-123456-78-9", "Книга", "Автор", 2020, 1)
        reader = Reader("R001", "Читатель", "reader@example.com")
        
        library.add_book(book)
        library.register_reader(reader)
        
        # Дата выдачи
        class MockDatetimeBorrow:
            @staticmethod
            def now():
                return datetime(2024, 1, 1, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeBorrow)
        library.borrow_book("R001", "978-0-123456-78-9")
        
        # Возврат через год
        class MockDatetimeReturn:
            @staticmethod
            def now():
                return datetime(2025, 1, 1, 12, 0, 0)
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeReturn)
        
        success, fine = library.return_book("R001", "978-0-123456-78-9")
        
        # Вычисляем точную разницу дней между датами
        due_date = datetime(2024, 1, 1, 12, 0, 0) + timedelta(days=14)
        return_date = datetime(2025, 1, 1, 12, 0, 0)
        overdue_days = (return_date - due_date).days
        expected_fine = overdue_days * 10.0
        
        assert success is True
        assert fine == pytest.approx(expected_fine)


# ============= ТЕСТЫ ВСПОМОГАТЕЛЬНЫХ ФУНКЦИЙ =============

class TestHelperFunctions:
    """Тесты вспомогательных функций"""
    
    def test_create_sample_library(self):
        """Тест: функция create_sample_library создает корректную библиотеку"""
        library = create_sample_library()
        
        assert library.name == "Городская библиотека"
        assert len(library.books) == 3
        assert len(library.readers) == 2
        
        # Проверяем наличие конкретных книг
        assert "978-0-545-01022-1" in library.books
        assert "978-5-17-084716-3" in library.books
        
        # Проверяем читателей
        assert "R001" in library.readers
        assert "R002" in library.readers


if __name__ == "__main__":
    # Запуск тестов с подробным выводом
    pytest.main([__file__, "-v", "--tb=short"])