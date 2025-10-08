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
    return Book("978-0-545-01022-1", "Гарри Поттер и Дары Смерти", "Дж.К. Роулинг", 2007, 3)


@pytest.fixture
def sample_reader():
    """Фикстура для создания тестового читателя"""
    return Reader("R001", "Иван Иванов", "ivan@example.com")


@pytest.fixture
def empty_library():
    """Фикстура для создания пустой библиотеки"""
    return Library("Тестовая библиотека")


@pytest.fixture
def library_with_data(sample_book, sample_reader):
    """Фикстура для создания библиотеки с предзаполненными данными"""
    library = Library("Библиотека с данными")
    library.add_book(sample_book)
    library.register_reader(sample_reader)
    return library


@pytest.fixture
def mock_datetime():
    """Фикстура для мока datetime"""
    class MockDateTime:
        def __init__(self, year, month, day):
            self.mock_now = datetime(year, month, day)
        
        def now(self):
            return self.mock_now
        
        def set_now(self, year, month, day):
            self.mock_now = datetime(year, month, day)
    
    return MockDateTime(2024, 1, 1)


# ============= ТЕСТЫ КЛАССА BOOK =============

class TestBook:
    """Тесты для класса Book"""
    
    def test_should_create_book_with_valid_data(self):
        """Корректное создание объекта книги с валидными данными"""
        book = Book("978-0-545-01022-1", "Гарри Поттер", "Дж.К. Роулинг", 2007, 3)
        
        assert book.isbn == "978-0-545-01022-1"
        assert book.title == "Гарри Поттер"
        assert book.author == "Дж.К. Роулинг"
        assert book.year == 2007
        assert book.total_copies == 3
        assert book.available_copies == 3
    
    @pytest.mark.parametrize("isbn,title,author,year,copies", [
        ("", "Title", "Author", 2000, 1),
        ("123", "", "Author", 2000, 1),
        ("123", "Title", "", 2000, 1),
    ])
    def test_should_raise_value_error_for_missing_required_fields(self, isbn, title, author, year, copies):
        """Валидация: пустые обязательные поля должны вызывать ValueError"""
        with pytest.raises(ValueError):
            Book(isbn, title, author, year, copies)
    
    @pytest.mark.parametrize("year", [999, 2030, -100, 0])
    def test_should_raise_value_error_for_invalid_year(self, year):
        """Валидация: некорректный год должен вызывать ValueError"""
        with pytest.raises(ValueError):
            Book("123", "Title", "Author", year, 1)
    
    def test_should_raise_value_error_for_negative_copies(self):
        """Валидация: отрицательное количество копий должно вызывать ValueError"""
        with pytest.raises(ValueError):
            Book("123", "Title", "Author", 2000, -1)
    
    def test_is_available_should_return_true_when_copies_available(self, sample_book):
        """Метод is_available() возвращает True когда есть доступные копии"""
        assert sample_book.is_available() is True
    
    def test_is_available_should_return_false_when_no_copies_available(self, sample_book):
        """Метод is_available() возвращает False когда нет доступных копий"""
        # Забираем все доступные копии
        for _ in range(sample_book.total_copies):
            sample_book.borrow()
        
        assert sample_book.is_available() is False
    
    def test_borrow_should_decrease_available_copies_and_return_true(self, sample_book):
        """Метод borrow() уменьшает available_copies и возвращает True"""
        initial_copies = sample_book.available_copies
        
        result = sample_book.borrow()
        
        assert result is True
        assert sample_book.available_copies == initial_copies - 1
    
    def test_borrow_should_return_false_when_no_copies_available(self, sample_book):
        """Метод borrow() возвращает False когда нет доступных копий"""
        # Забираем все доступные копии
        for _ in range(sample_book.total_copies):
            sample_book.borrow()
        
        result = sample_book.borrow()
        
        assert result is False
        assert sample_book.available_copies == 0
    
    def test_return_book_should_increase_available_copies_and_return_true(self, sample_book):
        """Метод return_book() увеличивает available_copies и возвращает True"""
        # Сначала забираем книгу
        sample_book.borrow()
        initial_copies = sample_book.available_copies
        
        result = sample_book.return_book()
        
        assert result is True
        assert sample_book.available_copies == initial_copies + 1
    
    def test_return_book_should_return_false_when_all_copies_returned(self, sample_book):
        """Метод return_book() возвращает False когда все копии уже возвращены"""
        result = sample_book.return_book()
        
        assert result is False
        assert sample_book.available_copies == sample_book.total_copies


# ============= ТЕСТЫ КЛАССА READER =============

class TestReader:
    """Тесты для класса Reader"""
    
    def test_should_create_reader_with_valid_data(self):
        """Корректное создание читателя с валидными данными"""
        reader = Reader("R001", "Иван Иванов", "ivan@example.com")
        
        assert reader.reader_id == "R001"
        assert reader.name == "Иван Иванов"
        assert reader.email == "ivan@example.com"
        assert reader.borrowed_books == []
        assert len(reader.history) == 0
    
    @pytest.mark.parametrize("reader_id,name,email", [
        ("", "Name", "email@example.com"),
        ("R001", "", "email@example.com"),
        ("R001", "Name", ""),
    ])
    def test_should_raise_value_error_for_missing_required_fields(self, reader_id, name, email):
        """Валидация: пустые обязательные поля должны вызывать ValueError"""
        with pytest.raises(ValueError):
            Reader(reader_id, name, email)
    
    @pytest.mark.parametrize("email", [
    "invalid-email",
    "missing.domain",
    ])
    def test_should_raise_value_error_for_email_without_at_symbol(self, email):
        """Валидация: email без символа '@' должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Некорректный email"):
            Reader("R001", "Name", email)
    
    def test_can_borrow_should_return_true_when_under_limit(self, sample_reader):
        """Метод can_borrow() возвращает True когда у читателя меньше MAX_BOOKS"""
        assert sample_reader.can_borrow() is True
    
    def test_can_borrow_should_return_false_when_limit_reached(self, sample_reader):
        """Метод can_borrow() возвращает False когда достигнут лимит"""
        # Добавляем максимальное количество книг
        for i in range(Reader.MAX_BOOKS):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        
        assert sample_reader.can_borrow() is False
    
    def test_add_borrowed_book_should_add_isbn_to_borrowed_books(self, sample_reader):
        """Метод add_borrowed_book() добавляет ISBN в borrowed_books"""
        isbn = "978-0-545-01022-1"
        
        result = sample_reader.add_borrowed_book(isbn)
        
        assert result is True
        assert isbn in sample_reader.borrowed_books
        assert len(sample_reader.history) == 1
        assert sample_reader.history[0][0] == isbn
        assert sample_reader.history[0][1] == 'borrowed'
    
    def test_add_borrowed_book_should_return_false_for_duplicate(self, sample_reader):
        """Метод add_borrowed_book() возвращает False при попытке добавить дубликат"""
        isbn = "978-0-545-01022-1"
        sample_reader.add_borrowed_book(isbn)
        
        result = sample_reader.add_borrowed_book(isbn)
        
        assert result is False
        assert sample_reader.borrowed_books.count(isbn) == 1
    
    def test_add_borrowed_book_should_return_false_when_limit_exceeded(self, sample_reader):
        """Метод add_borrowed_book() возвращает False при превышении лимита"""
        # Добавляем максимальное количество книг
        for i in range(Reader.MAX_BOOKS):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        
        result = sample_reader.add_borrowed_book("NEW-ISBN")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == Reader.MAX_BOOKS
    
    def test_remove_borrowed_book_should_remove_isbn_from_borrowed_books(self, sample_reader):
        """Метод remove_borrowed_book() удаляет ISBN из borrowed_books"""
        isbn = "978-0-545-01022-1"
        sample_reader.add_borrowed_book(isbn)
        
        result = sample_reader.remove_borrowed_book(isbn)
        
        assert result is True
        assert isbn not in sample_reader.borrowed_books
        assert len(sample_reader.history) == 2  # borrowed + returned
    
    def test_remove_borrowed_book_should_return_false_when_book_not_in_list(self, sample_reader):
        """Метод remove_borrowed_book() возвращает False если книги нет в списке"""
        result = sample_reader.remove_borrowed_book("NONEXISTENT-ISBN")
        
        assert result is False
    
    def test_history_should_record_operations_with_timestamps(self, sample_reader):
        """История корректно записывает операции с временными метками"""
        isbn1 = "ISBN1"
        isbn2 = "ISBN2"
        
        sample_reader.add_borrowed_book(isbn1)
        sample_reader.add_borrowed_book(isbn2)
        sample_reader.remove_borrowed_book(isbn1)
        
        assert len(sample_reader.history) == 3
        
        # Проверяем структуру записей истории
        for record in sample_reader.history:
            assert len(record) == 3
            assert isinstance(record[0], str)  # ISBN
            assert record[1] in ['borrowed', 'returned']  # action
            assert isinstance(record[2], datetime)  # timestamp


# ============= ТЕСТЫ КЛАССА LIBRARY =============

class TestLibrary:
    """Тесты для класса Library"""
    
    def test_should_create_library_with_valid_name(self):
        """Корректное создание библиотеки"""
        library = Library("Тестовая библиотека")
        
        assert library.name == "Тестовая библиотека"
        assert library.books == {}
        assert library.readers == {}
        assert library.active_loans == {}
    
    def test_should_raise_value_error_for_empty_library_name(self):
        """Валидация: пустое название библиотеки должно вызывать ValueError"""
        with pytest.raises(ValueError):
            Library("")
    
    def test_add_book_should_add_new_book_and_return_true(self, empty_library, sample_book):
        """Метод add_book() добавляет новую книгу и возвращает True"""
        result = empty_library.add_book(sample_book)
        
        assert result is True
        assert sample_book.isbn in empty_library.books
        assert empty_library.books[sample_book.isbn] == sample_book
    
    def test_add_book_should_increase_copies_for_existing_book(self, empty_library, sample_book):
        """Метод add_book() увеличивает количество копий для существующей книги"""
        # Добавляем книгу первый раз
        empty_library.add_book(sample_book)
        initial_total = sample_book.total_copies
        initial_available = sample_book.available_copies
        
        # Добавляем ту же книгу с дополнительными копиями
        additional_book = Book(sample_book.isbn, sample_book.title, sample_book.author, 
                              sample_book.year, 2)
        result = empty_library.add_book(additional_book)
        
        assert result is False
        assert empty_library.books[sample_book.isbn].total_copies == initial_total + 2
        assert empty_library.books[sample_book.isbn].available_copies == initial_available + 2
    
    def test_register_reader_should_register_new_reader(self, empty_library, sample_reader):
        """Метод register_reader() регистрирует нового читателя"""
        result = empty_library.register_reader(sample_reader)
        
        assert result is True
        assert sample_reader.reader_id in empty_library.readers
        assert empty_library.readers[sample_reader.reader_id] == sample_reader
    
    def test_register_reader_should_return_false_for_duplicate(self, empty_library, sample_reader):
        """Метод register_reader() возвращает False для дубликата"""
        empty_library.register_reader(sample_reader)
        
        result = empty_library.register_reader(sample_reader)
        
        assert result is False
    
    def test_find_books_by_author_should_find_books_case_insensitive(self, library_with_data, sample_book):
        """Метод find_books_by_author() находит книги (регистронезависимый поиск)"""
        # Поиск разными вариантами написания
        results1 = library_with_data.find_books_by_author("дж.к. роулинг")
        results2 = library_with_data.find_books_by_author("Дж.К. РОУЛИНГ")
        results3 = library_with_data.find_books_by_author("Роулинг")
        
        assert len(results1) == 1
        assert len(results2) == 1
        assert len(results3) == 1
        assert results1[0] == sample_book
        assert results2[0] == sample_book
        assert results3[0] == sample_book
    
    def test_find_books_by_title_should_find_books_case_insensitive(self, library_with_data, sample_book):
        """Метод find_books_by_title() находит книги (регистронезависимый поиск)"""
        # Поиск разными вариантами написания
        results1 = library_with_data.find_books_by_title("гарри поттер")
        results2 = library_with_data.find_books_by_title("ГАРРИ ПОТТЕР")
        results3 = library_with_data.find_books_by_title("поттер")
        
        assert len(results1) == 1
        assert len(results2) == 1
        assert len(results3) == 1
        assert results1[0] == sample_book
        assert results2[0] == sample_book
        assert results3[0] == sample_book
    
    def test_get_available_books_should_return_only_available_books(self, library_with_data, sample_book):
        """Метод get_available_books() возвращает только доступные книги"""
        available_books = library_with_data.get_available_books()
        
        assert len(available_books) == 1
        assert available_books[0] == sample_book
        
        # Забираем книгу и проверяем, что она больше не в списке доступных
        sample_book.borrow()
        available_books = library_with_data.get_available_books()
        
        if sample_book.available_copies == 0:
            assert len(available_books) == 0
        else:
            assert len(available_books) == 1
    
    def test_borrow_book_should_successfully_borrow_book(self, library_with_data):
        """Успешная выдача книги читателю"""
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        success, message = library_with_data.borrow_book(reader_id, isbn)
        
        assert success is True
        assert "выдана до" in message
        assert (reader_id, isbn) in library_with_data.active_loans
        assert isbn in library_with_data.readers[reader_id].borrowed_books
        assert library_with_data.books[isbn].available_copies == 2  # было 3, стало 2
    
    def test_borrow_book_should_raise_reader_not_found_error(self, library_with_data):
        """Выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError):
            library_with_data.borrow_book("NONEXISTENT", "978-0-545-01022-1")
    
    def test_borrow_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Возврат (False, message) для несуществующей книги"""
        success, message = library_with_data.borrow_book("R001", "NONEXISTENT-ISBN")
        
        assert success is False
        assert "не найдена" in message
    
    def test_borrow_book_should_raise_book_not_available_error(self, library_with_data, sample_book):
        """Выброс BookNotAvailableError когда книга недоступна"""
        # Забираем все копии книги
        for _ in range(sample_book.total_copies):
            sample_book.borrow()
        
        with pytest.raises(BookNotAvailableError):
            library_with_data.borrow_book("R001", sample_book.isbn)
    
    def test_borrow_book_should_return_false_when_reader_reached_limit(self, library_with_data):
        """Возврат (False, message) когда читатель достиг лимита книг"""
        reader = library_with_data.readers["R001"]
        isbn = "978-0-545-01022-1"
        
        # Добавляем максимальное количество книг читателю
        for i in range(Reader.MAX_BOOKS):
            reader.add_borrowed_book(f"EXTRA-ISBN-{i}")
        
        success, message = library_with_data.borrow_book("R001", isbn)
        
        assert success is False
        assert "лимита" in message.lower()
    
    def test_borrow_book_should_return_false_when_reader_already_borrowed_book(self, library_with_data):
        """Возврат (False, message) когда читатель уже взял эту книгу"""
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        # Первая выдача успешна
        success1, _ = library_with_data.borrow_book(reader_id, isbn)
        assert success1 is True
        
        # Вторая выдача должна вернуть ошибку
        success2, message = library_with_data.borrow_book(reader_id, isbn)
        
        assert success2 is False
        assert "уже взята" in message.lower()
    
    def test_borrow_book_should_add_record_to_active_loans_with_correct_due_date(self, library_with_data, mock_datetime, monkeypatch):
        """Проверка добавления записи в active_loans с корректной датой возврата"""
        # Мокаем datetime.now
        monkeypatch.setattr('library_system.datetime', mock_datetime)
        
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        success, _ = library_with_data.borrow_book(reader_id, isbn)
        
        assert success is True
        assert (reader_id, isbn) in library_with_data.active_loans
        
        expected_due_date = mock_datetime.now() + timedelta(days=library_with_data.LOAN_PERIOD_DAYS)
        assert library_with_data.active_loans[(reader_id, isbn)] == expected_due_date
    
    def test_return_book_should_successfully_return_book_without_fine(self, library_with_data):
        """Успешный возврат книги без штрафа (в срок)"""
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        # Сначала выдаем книгу
        library_with_data.borrow_book(reader_id, isbn)
        initial_available = library_with_data.books[isbn].available_copies
        
        # Возвращаем книгу
        success, fine = library_with_data.return_book(reader_id, isbn)
        
        assert success is True
        assert fine == 0.0
        assert (reader_id, isbn) not in library_with_data.active_loans
        assert isbn not in library_with_data.readers[reader_id].borrowed_books
        assert library_with_data.books[isbn].available_copies == initial_available + 1
    
    def test_return_book_should_raise_reader_not_found_error(self, library_with_data):
        """Выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError):
            library_with_data.return_book("NONEXISTENT", "978-0-545-01022-1")
    
    def test_return_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Возврат (False, 0.0) для несуществующей книги"""
        success, fine = library_with_data.return_book("R001", "NONEXISTENT-ISBN")
        
        assert success is False
        assert fine == 0.0
    
    def test_return_book_should_return_false_when_book_not_borrowed(self, library_with_data):
        """Возврат (False, 0.0) если эта книга не была взята читателем"""
        success, fine = library_with_data.return_book("R001", "978-0-545-01022-1")
        
        assert success is False
        assert fine == 0.0
    
    def test_calculate_fine_should_return_0_for_loan_not_overdue(self, mock_datetime, monkeypatch):
        """Метод calculate_fine() возвращает 0 для непросроченного займа"""
        # Мокаем datetime.now
        monkeypatch.setattr('library_system.datetime', mock_datetime)
        
        library = Library("Test")
        due_date = mock_datetime.now() + timedelta(days=5)  # еще 5 дней до возврата
        
        fine = library.calculate_fine(due_date)
        
        assert fine == 0.0
    
    def test_calculate_fine_should_calculate_fine_correctly(self, mock_datetime, monkeypatch):
        """Метод calculate_fine() корректно рассчитывает штраф"""
        # Мокаем datetime.now
        monkeypatch.setattr('library_system.datetime', mock_datetime)
        
        library = Library("Test")
        due_date = mock_datetime.now() - timedelta(days=5)  # просрочено на 5 дней
        
        fine = library.calculate_fine(due_date)
        
        expected_fine = 5 * library.FINE_PER_DAY
        assert fine == pytest.approx(expected_fine)
    
    def test_get_overdue_loans_should_return_overdue_loans(self, library_with_data, mock_datetime, monkeypatch):
        """Метод get_overdue_loans() возвращает список просроченных займов"""
        # Мокаем datetime.now
        monkeypatch.setattr('library_system.datetime', mock_datetime)
        
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        # Выдаем книгу
        library_with_data.borrow_book(reader_id, isbn)
        
        # Устанавливаем дату возврата в прошлом (просрочка)
        overdue_date = mock_datetime.now() - timedelta(days=5)
        library_with_data.active_loans[(reader_id, isbn)] = overdue_date
        
        overdue_loans = library_with_data.get_overdue_loans()
        
        assert len(overdue_loans) == 1
        assert overdue_loans[0][0] == reader_id
        assert overdue_loans[0][1] == isbn
        assert overdue_loans[0][2] == 5  # дней просрочки
        assert overdue_loans[0][3] == pytest.approx(5 * library_with_data.FINE_PER_DAY)
    
    def test_get_reader_stats_should_return_correct_stats(self, library_with_data):
        """Метод get_reader_stats() возвращает корректную статистику"""
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        # Выдаем книгу
        library_with_data.borrow_book(reader_id, isbn)
        
        stats = library_with_data.get_reader_stats(reader_id)
        
        assert stats['name'] == "Иван Иванов"
        assert stats['currently_borrowed'] == 1
        assert stats['total_borrowed'] >= 1
        assert stats['current_fines'] == 0.0
    
    def test_get_reader_stats_should_raise_reader_not_found_error(self, library_with_data):
        """Метод get_reader_stats() выбрасывает ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError):
            library_with_data.get_reader_stats("NONEXISTENT")
    
    def test_get_popular_books_should_return_top_popular_books(self, library_with_data):
        """Метод get_popular_books() возвращает топ популярных книг"""
        # Выдаем книгу несколько раз
        reader_id = "R001"
        isbn = "978-0-545-01022-1"
        
        # Эмулируем несколько выдач через историю читателя
        reader = library_with_data.readers[reader_id]
        for _ in range(3):
            reader.history.append((isbn, 'borrowed', datetime.now()))
        
        popular_books = library_with_data.get_popular_books(top_n=3)
        
        assert len(popular_books) == 1
        assert popular_books[0][0] == library_with_data.books[isbn]
        assert popular_books[0][1] == 3  # 3 выдачи


# ============= ИНТЕГРАЦИОННЫЕ ТЕСТЫ =============

class TestIntegration:
    """Интеграционные тесты"""
    
    def test_full_book_lifecycle(self, empty_library):
        """Полный цикл работы с книгой"""
        # 1. Создание библиотеки (уже выполнено в фикстуре)
        library = empty_library
        
        # 2. Добавление книги
        book = Book("978-0-545-01022-1", "Тестовая книга", "Тестовый автор", 2024, 2)
        library.add_book(book)
        
        # 3. Регистрация читателя
        reader = Reader("R001", "Тестовый читатель", "test@example.com")
        library.register_reader(reader)
        
        # 4. Выдача книги
        success, message = library.borrow_book("R001", "978-0-545-01022-1")
        assert success is True
        
        # 5. Проверка статистики
        stats = library.get_reader_stats("R001")
        assert stats['currently_borrowed'] == 1
        assert stats['total_borrowed'] == 1
        assert library.books["978-0-545-01022-1"].available_copies == 1
        
        # 6. Возврат книги
        success, fine = library.return_book("R001", "978-0-545-01022-1")
        assert success is True
        assert fine == 0.0
        
        # 7. Проверка обновленной статистики
        stats = library.get_reader_stats("R001")
        assert stats['currently_borrowed'] == 0
        assert stats['total_borrowed'] == 1
        assert stats['total_returned'] == 1
        assert library.books["978-0-545-01022-1"].available_copies == 2
    
    def test_overdue_scenario_with_fine(self, empty_library, mock_datetime, monkeypatch):
        """Сценарий с просрочкой и штрафом"""
        # Мокаем datetime.now
        monkeypatch.setattr('library_system.datetime', mock_datetime)
        
        library = empty_library
        
        # 1. Добавление книги и регистрация читателя
        book = Book("978-0-545-01022-1", "Тестовая книга", "Тестовый автор", 2024, 1)
        library.add_book(book)
        
        reader = Reader("R001", "Тестовый читатель", "test@example.com")
        library.register_reader(reader)
        
        # 2. Выдача книги
        success, _ = library.borrow_book("R001", "978-0-545-01022-1")
        assert success is True
        
        # 3. Эмуляция просрочки (перемещаем время вперед на 20 дней)
        original_due_date = library.active_loans[("R001", "978-0-545-01022-1")]
        mock_datetime.set_now(2024, 1, 21)  # 20 дней после выдачи
        
        # 4. Проверка расчета штрафа
        overdue_days = (mock_datetime.now() - original_due_date).days
        expected_fine = overdue_days * library.FINE_PER_DAY
        
        calculated_fine = library.calculate_fine(original_due_date)
        assert calculated_fine == pytest.approx(expected_fine)
        
        # 5. Возврат с штрафом
        success, actual_fine = library.return_book("R001", "978-0-545-01022-1")
        assert success is True
        assert actual_fine == pytest.approx(expected_fine)
        
        # Проверяем, что книга снова доступна
        assert library.books["978-0-545-01022-1"].is_available() is True