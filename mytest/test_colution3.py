import pytest
from libery_class import Book, Reader, Library


class TestAnalyzeBook:
    """Тесты для класса Book"""
    def test_Book_1(self):
        """Корректное создание объекта книги с валидными данными"""
        result = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 100)

        assert result is not None


    def test_Book_2(self):
        """Валидация: пустой ISBN должен вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Book(None, "Рейс 370", "Андреев Константин", 2014, 100)
        assert  "ISBN, название и автор обязательны" in str(e.value)


    def test_Book_3(self):
        """Валидация: пустое название должно вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Book("Андреев Константин", None, "Андреев Константин", 2014, 100)
        assert  "ISBN, название и автор обязательны" in str(e.value)


    def test_Book_4(self):
        """ Валидация: пустой автор должен вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Book("Андреев Константин", "Рейс 370", None, 2014, 100)
        assert  "ISBN, название и автор обязательны" in str(e.value)


    def test_Book_4(self):
        """Валидация: некорректный год (< 1000 или > текущего) должен вызывать"""

        with pytest.raises(ValueError) as e:
            age = 100
            Book("Андреев Константин", "Рейс 370", "Андреев Константин", age, 100)
        assert  f'Некорректный год издания: {age}' in str(e.value)


    def test_Book_5(self):
        """Валидация: отрицательное количество копий должно вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, -1)
        assert  "Количество копий не может быть отрицательным" in str(e.value)


    def test_Book_6(self):
        """Метод is_available() возвращает True когда есть доступные копии"""
        book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 100)
        assert book.is_available() == 1


    def test_Book_7(self):
        """Метод borrow() уменьшает available_copies и возвращает True"""
        book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 100)
        assert book.borrow() == True



    def test_Book_8(self):
        """Метод borrow() возвращает False когда нет доступных копий"""
        book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 1)
        book.borrow()
        assert book.borrow() == False


    def test_Book_9(self):
        """Метод return_book() увеличивает available_copies и возвращает True"""
        book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 1)
        book.borrow()
        assert book.return_book() == True


    def test_Book_10(self):
        """Метод borrow() возвращает False когда нет доступных копий"""
        book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 1)
        assert book.return_book() == False



class TestAnalyzeReader:
    """Тесты для класса Reader"""
    
    def test_Reader_1(self):
        """ Корректное создание читателя с валидными данными"""
        result = Reader("111223334", name="Александр Александрович", email="user@example.com")

        assert result is not None

    def test_Reader_2(self):
        """Валидация: пустой reader_id должен вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Reader(None, "Александр Александрович", "user@example.com")
        assert str(e.value) != None

    def test_Reader_3(self):
        """ Валидация: пустое имя должно вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Reader("1Fg@", None, "user@example.com")
        assert str(e.value) != None

    def test_Reader_4(self):
        """Валидация: пустой email должен вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Reader("1Fg@", "Александр Александрович", None)
        assert str(e.value) != None

    def test_Reader_5(self):
        """Валидация: email без символа '@' должен вызывать ValueError"""

        with pytest.raises(ValueError) as e:
            Reader("1Fg@", "Александр Александрович", "example.com")
        assert str(e.value) != None

    def test_Reader_6(self):
        """ Метод can_borrow() возвращает True когда у читателя меньше MAX_BOOKS"""

        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert reader.can_borrow() == True

    def test_Reader_7(self):
        """Метод can_borrow() возвращает False когда достигнут лимит"""
        import random
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        for i in range(5):
            reader.add_borrowed_book(str(random.randint(0, 1000)))
        assert reader.can_borrow() == False

    def test_Reader_8(self):
        """Метод add_borrowed_book() добавляет ISBN в borrowed_books"""
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert reader.add_borrowed_book("Test") == True

    def test_Reader_9(self):
        """Метод add_borrowed_book() возвращает False при попытке добавить дубликат"""
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert reader.add_borrowed_book("Test") == True
        assert reader.add_borrowed_book("Test") == False

    def test_Reader_10(self):
        """Метод add_borrowed_book() возвращает False при превышении лимита"""
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert reader.add_borrowed_book("Test") == True
        assert reader.add_borrowed_book("Test1") == True
        assert reader.add_borrowed_book("Test2") == True
        assert reader.add_borrowed_book("Test3") == True
        assert reader.add_borrowed_book("Test4") == True
        assert reader.add_borrowed_book("Test5") == False

    def test_Reader_11(self):
        """ Метод remove_borrowed_book() удаляет ISBN из borrowed_books"""
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert reader.add_borrowed_book("Test") == True
        assert reader.remove_borrowed_book("Test") == True


    def test_Reader_12(self):
        """Метод remove_borrowed_book() возвращает False если книги нет в списке"""
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert reader.remove_borrowed_book("Test") == False


    def test_Reader_13(self):
        """История (history) корректно записывает операции с временными метками"""
        reader = Reader("1Fg@", "Александр Александрович", "user@example.com")
        assert len(reader.history) == 0 
        assert reader.add_borrowed_book("Test") == True
        assert len(reader.history) == 1
        assert reader.add_borrowed_book("Test2") == True
        assert len(reader.history) == 2
        assert reader.remove_borrowed_book("Test2") == True
        assert len(reader.history) == 3

    # def test_Book_3(self):
    #     """Валидация: пустое название должно вызывать ValueError"""

    #     with pytest.raises(ValueError) as e:
    #         Book("Андреев Константин", None, "Андреев Константин", 2014, 100)
    #     assert  "ISBN, название и автор обязательны" in str(e.value)

    # def test_Book_4(self):
    #     """ Валидация: пустой автор должен вызывать ValueError"""

    #     with pytest.raises(ValueError) as e:
    #         Book("Андреев Константин", "Рейс 370", None, 2014, 100)
    #     assert  "ISBN, название и автор обязательны" in str(e.value)

    # def test_Book_4(self):
    #     """Валидация: некорректный год (< 1000 или > текущего) должен вызывать"""

    #     with pytest.raises(ValueError) as e:
    #         age = 100
    #         Book("Андреев Константин", "Рейс 370", "Андреев Константин", age, 100)
    #     assert  f'Некорректный год издания: {age}' in str(e.value)

    # def test_Book_5(self):
    #     """Валидация: отрицательное количество копий должно вызывать ValueError"""

    #     with pytest.raises(ValueError) as e:
    #         Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, -1)
    #     assert  "Количество копий не может быть отрицательным" in str(e.value)

    # def test_Book_6(self):
    #     """Метод is_available() возвращает True когда есть доступные копии"""
    #     book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 100)
    #     assert book.is_available() == 1

    # def test_Book_7(self):
    #     """Метод borrow() уменьшает available_copies и возвращает True"""
    #     book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 100)
    #     assert book.borrow() == True

    # def test_Book_8(self):
    #     """Метод borrow() возвращает False когда нет доступных копий"""
    #     book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 1)
    #     book.borrow()
    #     assert book.borrow() == False

    # def test_Book_9(self):
    #     """Метод return_book() увеличивает available_copies и возвращает True"""
    #     book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 1)
    #     book.borrow()
    #     assert book.return_book() == True

    # def test_Book_10(self):
    #     """Метод borrow() возвращает False когда нет доступных копий"""
    #     book = Book("Андреев Константин", "Рейс 370", "Андреев Константин", 2014, 1)
    #     assert book.return_book() == False




if __name__ == "__main__":
    pytest.main([__file__, "-v"])