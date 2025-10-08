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
def library_with_data():
    """Фикстура для создания библиотеки с предзаполненными данными"""
    lib = Library("Городская библиотека")
    
    # Добавляем книги
    books = [
        Book("978-0-545-01022-1", "Гарри Поттер и Дары Смерти", "Дж.К. Роулинг", 2007, 3),
        Book("978-5-17-084716-3", "Мастер и Маргарита", "М.А. Булгаков", 1967, 2),
        Book("978-5-389-01006-7", "1984", "Джордж Оруэлл", 1949, 2),
        Book("978-3-420-011346-2", "1989 дней назад", "Джордж Аруэлл", 1949, 1)
    ]
    
    for book in books:
        lib.add_book(book)
    
    # Регистрируем читателей
    readers = [
        Reader("R001", "Иван Иванов", "ivan@example.com"),
        Reader("R002", "Мария Петрова", "maria@example.com"),
    ]
    
    for reader in readers:
        lib.register_reader(reader)
    
    return lib


@pytest.fixture
def empty_library():
    """Фикстура для создания пустой библиотеки"""
    return Library("Тестовая библиотека")


# ============= ТЕСТЫ КЛАССА BOOK =============

class TestBook:
    """Тесты для класса Book"""
    
    def test_should_create_book_with_valid_data(self, sample_book):
        """Корректное создание объекта книги с валидными данными"""
        assert sample_book.isbn == "978-0-545-01022-1"
        assert sample_book.title == "Гарри Поттер и Дары Смерти"
        assert sample_book.author == "Дж.К. Роулинг"
        assert sample_book.year == 2007
        assert sample_book.total_copies == 3
        assert sample_book.available_copies == 3
    
    @pytest.mark.parametrize("isbn", ["", None])
    def test_should_raise_error_for_empty_isbn(self, isbn):
        """Валидация: пустой ISBN должен вызывать ValueError"""
        with pytest.raises(ValueError, match="ISBN, название и автор обязательны"):
            Book(isbn, "Тестовая книга", "Автор", 2020)
    
    @pytest.mark.parametrize("title", ["", None])
    def test_should_raise_error_for_empty_title(self, title):
        """Валидация: пустое название должно вызывать ValueError"""
        with pytest.raises(ValueError, match="ISBN, название и автор обязательны"):
            Book("123", title, "Автор", 2020)
    
    @pytest.mark.parametrize("author", ["", None])
    def test_should_raise_error_for_empty_author(self, author):
        """Валидация: пустой автор должен вызывать ValueError"""
        with pytest.raises(ValueError, match="ISBN, название и автор обязательны"):
            Book("123", "Тестовая книга", author, 2020)
    
    @pytest.mark.parametrize("year", [999, 2030, -100, 0])
    def test_should_raise_error_for_invalid_year(self, year):
        """Валидация: некорректный год должен вызывать ValueError"""
        with pytest.raises(ValueError, match=f"Некорректный год издания: {year}"):
            Book("123", "Тестовая книга", "Автор", year)
    
    def test_should_raise_error_for_negative_copies(self):
        """Валидация: отрицательное количество копий должно вызывать ValueError"""
        with pytest.raises(ValueError, match="Количество копий не может быть отрицательным"):
            Book("123", "Тестовая книга", "Автор", 2020, -1)
    
    def test_is_available_should_return_true_when_copies_available(self, sample_book):
        """Метод is_available() возвращает True когда есть доступные копии"""
        assert sample_book.is_available() is True
    
    def test_is_available_should_return_false_when_no_copies_available(self, sample_book):
        """Метод is_available() возвращает False когда нет доступных копий"""
        # Занимаем все копии
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
        # Занимаем все копии
        for _ in range(sample_book.total_copies):
            sample_book.borrow()
        
        result = sample_book.borrow()
        assert result is False
        assert sample_book.available_copies == 0
    
    def test_return_book_should_increase_available_copies_and_return_true(self, sample_book):
        """Метод return_book() увеличивает available_copies и возвращает True"""
        # Сначала занимаем книгу
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
    
    def test_should_create_reader_with_valid_data(self, sample_reader):
        """Корректное создание читателя с валидными данными"""
        assert sample_reader.reader_id == "R001"
        assert sample_reader.name == "Иван Иванов"
        assert sample_reader.email == "ivan@example.com"
        assert sample_reader.borrowed_books == []
        assert sample_reader.history == []
    
    @pytest.mark.parametrize("reader_id", ["", None])
    def test_should_raise_error_for_empty_reader_id(self, reader_id):
        """Валидация: пустой reader_id должен вызывать ValueError"""
        with pytest.raises(ValueError, match="ID, имя и email обязательны"):
            Reader(reader_id, "Иван Иванов", "ivan@example.com")
    
    @pytest.mark.parametrize("name", ["", None])
    def test_should_raise_error_for_empty_name(self, name):
        """Валидация: пустое имя должно вызывать ValueError"""
        with pytest.raises(ValueError, match="ID, имя и email обязательны"):
            Reader("R001", name, "ivan@example.com")
    
    @pytest.mark.parametrize("email", ["", None])
    def test_should_raise_error_for_empty_email(self, email):
        """Валидация: пустой email должен вызывать ValueError"""
        with pytest.raises(ValueError, match="ID, имя и email обязательны"):
            Reader("R001", "Иван Иванов", email)
    
    @pytest.mark.parametrize("email", ["invalid", "invalid.com"])
    def test_should_raise_error_for_invalid_email(self, email):
        """Валидация: email без символа '@' должен вызывать ValueError"""
        with pytest.raises(ValueError, match="Некорректный email"):
            Reader("R001", "Иван Иванов", email)
    
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
        result = sample_reader.add_borrowed_book("ISBN123")
        
        assert result is True
        assert "ISBN123" in sample_reader.borrowed_books
        assert len(sample_reader.history) == 1
        assert sample_reader.history[0][0] == "ISBN123"
        assert sample_reader.history[0][1] == "borrowed"
    
    def test_add_borrowed_book_should_return_false_for_duplicate(self, sample_reader):
        """Метод add_borrowed_book() возвращает False при попытке добавить дубликат"""
        sample_reader.add_borrowed_book("ISBN123")
        result = sample_reader.add_borrowed_book("ISBN123")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == 1
    
    def test_add_borrowed_book_should_return_false_when_over_limit(self, sample_reader):
        """Метод add_borrowed_book() возвращает False при превышении лимита"""
        # Добавляем максимальное количество книг
        for i in range(Reader.MAX_BOOKS):
            sample_reader.add_borrowed_book(f"ISBN{i}")
        
        result = sample_reader.add_borrowed_book("ISBN_EXTRA")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == Reader.MAX_BOOKS
    
    def test_remove_borrowed_book_should_remove_isbn_from_borrowed_books(self, sample_reader):
        """Метод remove_borrowed_book() удаляет ISBN из borrowed_books"""
        sample_reader.add_borrowed_book("ISBN123")
        result = sample_reader.remove_borrowed_book("ISBN123")
        
        assert result is True
        assert "ISBN123" not in sample_reader.borrowed_books
        assert len(sample_reader.history) == 2  # borrow + return
    
    def test_remove_borrowed_book_should_return_false_if_book_not_in_list(self, sample_reader):
        """Метод remove_borrowed_book() возвращает False если книги нет в списке"""
        result = sample_reader.remove_borrowed_book("NON_EXISTENT")
        
        assert result is False
        assert len(sample_reader.borrowed_books) == 0
    
    def test_history_should_record_operations_with_timestamps(self, sample_reader):
        """История (history) корректно записывает операции с временными метками"""
        sample_reader.add_borrowed_book("ISBN1")
        sample_reader.remove_borrowed_book("ISBN1")
        sample_reader.add_borrowed_book("ISBN2")
        
        assert len(sample_reader.history) == 3
        
        # Проверяем структуру записей
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
    
    @pytest.mark.parametrize("name", ["", None])
    def test_should_raise_error_for_empty_library_name(self, name):
        """Валидация: пустое название библиотеки должно вызывать ValueError"""
        with pytest.raises(ValueError, match="Название библиотеки обязательно"):
            Library(name)
    
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
        initial_copies = sample_book.total_copies
        
        # Создаем новую книгу с тем же ISBN но другими копиями
        additional_book = Book(sample_book.isbn, "Другое название", "Другой автор", 2020, 2)
        result = empty_library.add_book(additional_book)
        
        assert result is False
        assert empty_library.books[sample_book.isbn].total_copies == initial_copies + 2
        assert empty_library.books[sample_book.isbn].available_copies == initial_copies + 2
    
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
    
    def test_find_books_by_author_should_find_books_case_insensitive(self, library_with_data):
        """Метод find_books_by_author() находит книги (регистронезависимый поиск)"""
        books_lower = library_with_data.find_books_by_author("роулинг")
        books_upper = library_with_data.find_books_by_author("РОУЛИНГ")
        books_mixed = library_with_data.find_books_by_author("РоУлИнГ")
        
        assert len(books_lower) == 1
        assert len(books_upper) == 1
        assert len(books_mixed) == 1
        assert books_lower[0].author == "Дж.К. Роулинг"
    
    def test_find_books_by_title_should_find_books_case_insensitive(self, library_with_data):
        """Метод find_books_by_title() находит книги (регистронезависимый поиск)"""
        books_lower = library_with_data.find_books_by_title("гарри")
        books_upper = library_with_data.find_books_by_title("ГАРРИ")
        books_mixed = library_with_data.find_books_by_title("ГаРрИ")
        
        assert len(books_lower) == 1
        assert len(books_upper) == 1
        assert len(books_mixed) == 1
        assert books_lower[0].title == "Гарри Поттер и Дары Смерти"
    
    def test_get_available_books_should_return_only_available_books(self, library_with_data):
        """Метод get_available_books() возвращает только доступные книги"""
        available_books = library_with_data.get_available_books()
        
        # Все книги должны быть доступны изначально
        assert len(available_books) == len(library_with_data.books)
        
        # Занимаем одну книгу
        library_with_data.borrow_book("R001", "978-3-420-011346-2")
        available_books_after = library_with_data.get_available_books()
        
        assert len(available_books_after) == len(available_books) - 1
    
    def test_borrow_book_should_successfully_lend_book_to_reader(self, library_with_data):
        """Успешная выдача книги читателю"""
        success, message = library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        assert success is True
        assert "выдана до" in message
        assert ("R001", "978-0-545-01022-1") in library_with_data.active_loans
        assert "978-0-545-01022-1" in library_with_data.readers["R001"].borrowed_books
    
    def test_borrow_book_should_raise_reader_not_found_error(self, library_with_data):
        """Выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError, match="Читатель NON_EXISTENT не найден"):
            library_with_data.borrow_book("NON_EXISTENT", "978-0-545-01022-1")
    
    def test_borrow_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Возврат (False, message) для несуществующей книги"""
        success, message = library_with_data.borrow_book("R001", "NON_EXISTENT_ISBN")
        
        assert success is False
        assert "не найдена" in message
    
    def test_borrow_book_should_raise_book_not_available_error(self, library_with_data):
        """Выброс BookNotAvailableError когда книга недоступна"""
        # Занимаем все копии книги
        book = library_with_data.books["978-0-545-01022-1"]
        for _ in range(book.total_copies):
            book.borrow()
        
        with pytest.raises(BookNotAvailableError, match="недоступна"):
            library_with_data.borrow_book("R001", "978-0-545-01022-1")
    
    def test_borrow_book_should_return_false_when_reader_reached_limit(self, library_with_data):
        """Возврат (False, message) когда читатель достиг лимита книг"""
        # Добавляем максимальное количество книг читателю
        reader = library_with_data.readers["R001"]
        for i in range(Reader.MAX_BOOKS):
            reader.add_borrowed_book(f"EXTRA_{i}")
        
        success, message = library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        assert success is False
        assert "лимита книг" in message
    
    def test_borrow_book_should_return_false_when_reader_already_borrowed_book(self, library_with_data):
        """Возврат (False, message) когда читатель уже взял эту книгу"""
        # Выдаем книгу первый раз
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        # Пытаемся выдать ту же книгу еще раз
        success, message = library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        assert success is False
        assert "уже взята" in message
    
    def test_borrow_book_should_add_record_to_active_loans_with_correct_due_date(self, library_with_data, monkeypatch):
        """Проверка добавления записи в active_loans с корректной датой возврата"""
        # Фиксируем текущее время для теста
        fixed_now = datetime(2024, 1, 1)
        
        class MockDatetime:
            @staticmethod
            def now():
                return fixed_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        success, message = library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        assert success is True
        expected_due_date = fixed_now + timedelta(days=Library.LOAN_PERIOD_DAYS)
        assert library_with_data.active_loans[("R001", "978-0-545-01022-1")] == expected_due_date
    
    def test_return_book_should_successfully_return_book_without_fine(self, library_with_data):
        """Успешный возврат книги без штрафа (в срок)"""
        # Сначала выдаем книгу
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        success, fine = library_with_data.return_book("R001", "978-0-545-01022-1")
        
        assert success is True
        assert fine == 0.0
        assert ("R001", "978-0-545-01022-1") not in library_with_data.active_loans
        assert "978-0-545-01022-1" not in library_with_data.readers["R001"].borrowed_books
    
    def test_return_book_should_raise_reader_not_found_error_for_nonexistent_reader(self, library_with_data):
        """Выброс ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError, match="Читатель NON_EXISTENT не найден"):
            library_with_data.return_book("NON_EXISTENT", "978-0-545-01022-1")
    
    def test_return_book_should_return_false_for_nonexistent_book(self, library_with_data):
        """Возврат (False, 0.0) для несуществующей книги"""
        success, fine = library_with_data.return_book("R001", "NON_EXISTENT_ISBN")
        
        assert success is False
        assert fine == 0.0
    
    def test_return_book_should_return_false_if_book_not_borrowed_by_reader(self, library_with_data):
        """Возврат (False, 0.0) если эта книга не была взята читателем"""
        success, fine = library_with_data.return_book("R001", "978-0-545-01022-1")
        
        assert success is False
        assert fine == 0.0
    
    def test_return_book_should_calculate_fine_for_overdue(self, library_with_data, monkeypatch):
        """Расчет штрафа при просрочке возврата"""
        # Выдаем книгу
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        
        # Подменяем текущее время на дату после срока возврата
        fixed_now = datetime(2024, 1, 20)  # +19 дней от выдачи
        
        class MockDatetime:
            @staticmethod
            def now():
                return fixed_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        # Устанавливаем просроченную дату возврата
        overdue_due_date = datetime(2024, 1, 10)  # 10 дней просрочки
        library_with_data.active_loans[("R001", "978-0-545-01022-1")] = overdue_due_date
        
        success, fine = library_with_data.return_book("R001", "978-0-545-01022-1")
        
        assert success is True
        expected_fine = 10 * Library.FINE_PER_DAY  # 10 дней * 10.0
        assert fine == pytest.approx(expected_fine)
    
    def test_calculate_fine_should_return_zero_for_non_overdue_loan(self, library_with_data):
        """Метод calculate_fine() возвращает 0 для непросроченного займа"""
        due_date = datetime.now() + timedelta(days=5)  # еще 5 дней до возврата
        fine = library_with_data.calculate_fine(due_date)
        
        assert fine == 0.0
    
    def test_calculate_fine_should_calculate_fine_correctly(self, library_with_data, monkeypatch):
        """Метод calculate_fine() корректно рассчитывает штраф (дни * FINE_PER_DAY)"""
        # Фиксируем текущее время
        fixed_now = datetime(2024, 1, 15)
        
        class MockDatetime:
            @staticmethod
            def now():
                return fixed_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        due_date = datetime(2024, 1, 10)  # 5 дней просрочки
        fine = library_with_data.calculate_fine(due_date)
        
        expected_fine = 5 * Library.FINE_PER_DAY
        assert fine == pytest.approx(expected_fine)
    
    def test_get_overdue_loans_should_return_list_of_overdue_loans(self, library_with_data, monkeypatch):
        """Метод get_overdue_loans() возвращает список просроченных займов"""
        # Фиксируем текущее время
        fixed_now = datetime(2024, 1, 20)
        
        class MockDatetime:
            @staticmethod
            def now():
                return fixed_now
        
        monkeypatch.setattr('library_system.datetime', MockDatetime)
        
        # Добавляем активные займы с разными датами возврата
        library_with_data.active_loans[("R001", "ISBN1")] = datetime(2024, 1, 10)  # 10 дней просрочки
        library_with_data.active_loans[("R001", "ISBN2")] = datetime(2024, 1, 15)  # 5 дней просрочки
        library_with_data.active_loans[("R002", "ISBN3")] = datetime(2024, 1, 25)  # не просрочен
        
        overdue_loans = library_with_data.get_overdue_loans()
        
        assert len(overdue_loans) == 2
        # Проверяем сортировку по убыванию дней просрочки
        assert overdue_loans[0][2] == 10  # 10 дней просрочки
        assert overdue_loans[1][2] == 5   # 5 дней просрочки
    
    def test_get_reader_stats_should_return_correct_statistics(self, library_with_data):
        """Метод get_reader_stats() возвращает корректную статистику"""
        # Выдаем несколько книг читателю
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        library_with_data.borrow_book("R001", "978-5-17-084716-3")
        
        stats = library_with_data.get_reader_stats("R001")
        
        assert stats['name'] == "Иван Иванов"
        assert stats['currently_borrowed'] == 2
        assert stats['total_borrowed'] >= 2
        assert stats['current_fines'] == 0.0
    
    def test_get_reader_stats_should_raise_reader_not_found_error(self, library_with_data):
        """Метод get_reader_stats() выбрасывает ReaderNotFoundError для несуществующего читателя"""
        with pytest.raises(ReaderNotFoundError, match="Читатель NON_EXISTENT не найден"):
            library_with_data.get_reader_stats("NON_EXISTENT")
    
    def test_get_popular_books_should_return_top_popular_books(self, library_with_data):
        """Метод get_popular_books() возвращает топ популярных книг"""
        # Выдаем книги несколько раз
        library_with_data.borrow_book("R001", "978-0-545-01022-1")
        library_with_data.borrow_book("R002", "978-0-545-01022-1")
        library_with_data.borrow_book("R001", "978-5-17-084716-3")
        
        popular_books = library_with_data.get_popular_books(top_n=2)
        
        assert len(popular_books) == 2
        # Книга с ISBN 978-0-545-01022-1 должна быть самой популярной (2 выдачи)
        assert popular_books[0][0].isbn == "978-0-545-01022-1"
        assert popular_books[0][1] == 2


# ============= ИНТЕГРАЦИОННЫЕ ТЕСТЫ =============

class TestIntegration:
    """Интеграционные тесты"""
    
    def test_full_book_lifecycle(self, empty_library):
        """
        Полный цикл работы с книгой:
        1. Создание библиотеки
        2. Добавление книги
        3. Регистрация читателя
        4. Выдача книги
        5. Проверка статистики
        6. Возврат книги
        7. Проверка обновленной статистики
        """
        # 1. Библиотека уже создана фикстурой
        
        # 2. Добавление книги
        book = Book("TEST-ISBN", "Тестовая книга", "Тестовый автор", 2024, 2)
        empty_library.add_book(book)
        assert book.isbn in empty_library.books
        
        # 3. Регистрация читателя
        reader = Reader("TEST-READER", "Тестовый читатель", "test@example.com")
        empty_library.register_reader(reader)
        assert reader.reader_id in empty_library.readers
        
        # 4. Выдача книги
        success, message = empty_library.borrow_book("TEST-READER", "TEST-ISBN")
        assert success is True
        assert ("TEST-READER", "TEST-ISBN") in empty_library.active_loans
        
        # 5. Проверка статистики
        stats = empty_library.get_reader_stats("TEST-READER")
        assert stats['currently_borrowed'] == 1
        assert stats['total_borrowed'] == 1
        
        # 6. Возврат книги
        success, fine = empty_library.return_book("TEST-READER", "TEST-ISBN")
        assert success is True
        assert fine == 0.0
        assert ("TEST-READER", "TEST-ISBN") not in empty_library.active_loans
        
        # 7. Проверка обновленной статистики
        stats_after = empty_library.get_reader_stats("TEST-READER")
        assert stats_after['currently_borrowed'] == 0
        assert stats_after['total_returned'] == 1
    
    def test_scenario_with_overdue(self, empty_library, monkeypatch):
        """
        Сценарий с просрочкой:
        1. Выдача книги
        2. Эмуляция просрочки (через monkeypatch)
        3. Проверка расчета штрафа
        4. Возврат с штрафом
        """
        # Настройка данных
        book = Book("TEST-ISBN", "Тестовая книга", "Тестовый автор", 2024, 1)
        empty_library.add_book(book)
        
        reader = Reader("TEST-READER", "Тестовый читатель", "test@example.com")
        empty_library.register_reader(reader)
        
        # 1. Выдача книги (фиксируем дату выдачи)
        fixed_borrow_date = datetime(2024, 1, 1)
        
        class MockDatetimeBorrow:
            @staticmethod
            def now():
                return fixed_borrow_date
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeBorrow)
        
        success, message = empty_library.borrow_book("TEST-READER", "TEST-ISBN")
        assert success is True
        
        # 2. Эмуляция просрочки (текущая дата после срока возврата)
        fixed_return_date = datetime(2024, 1, 20)  # 19 дней от выдачи, 5 дней просрочки
        
        class MockDatetimeReturn:
            @staticmethod
            def now():
                return fixed_return_date
        
        monkeypatch.setattr('library_system.datetime', MockDatetimeReturn)
        
        # 3. Проверка расчета штрафа
        due_date = fixed_borrow_date + timedelta(days=Library.LOAN_PERIOD_DAYS)
        fine = empty_library.calculate_fine(due_date)
        expected_fine = 5 * Library.FINE_PER_DAY  # 5 дней просрочки
        assert fine == pytest.approx(expected_fine)
        
        # 4. Возврат с штрафом
        success, actual_fine = empty_library.return_book("TEST-READER", "TEST-ISBN")
        assert success is True
        assert actual_fine == pytest.approx(expected_fine)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

  # test_solution3.py [100%]
  # 88 passed in 0.77s  