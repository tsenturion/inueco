import unittest

class TestListExample(unittest.TestCase):
    """
    Простой пример использования setUp и tearDown.
    Демонстрирует изоляцию тестов.
    """
    
    def setUp(self):
        """
        Вызывается перед КАЖДЫМ тестом.
        Создаёт свежий список для каждого теста.
        """
        print(f"\nВызывается setUp для теста: {self._testMethodName}")
        self.data = [1, 2, 3]
        print(f"Создан список: {self.data}")
    
    def tearDown(self):
        """
        Вызывается после КАЖДОГО теста.
        Даже если тест упал с ошибкой.
        """
        print(f"Вызывается tearDown для теста: {self._testMethodName}")
        self.data.clear()
        print(f"Список очищен: {self.data}")
    
    def test_length(self):
        """Тест проверяет длину списка"""
        print(f"Выполняется test_length, список: {self.data}")
        self.assertEqual(len(self.data), 3)
        # Изменяем список в тесте
        self.data.append(99)
        print(f"Список изменён в тесте: {self.data}")
    
    def test_sum(self):
        """Тест проверяет сумму элементов"""
        print(f"Выполняется test_sum, список: {self.data}")
        self.assertEqual(sum(self.data), 6)
        # Этот тест видит исходный список [1, 2, 3], 
        # а не изменённый из test_length
    
    def test_append(self):
        """Тест проверяет добавление элемента"""
        print(f"Выполняется test_append, список: {self.data}")
        original_length = len(self.data)
        self.data.append(4)
        self.assertEqual(len(self.data), original_length + 1)
        self.assertEqual(self.data[-1], 4)


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
def test_user_creation(self):
    # Подготовка
    db_connection = connect_to_database()
    create_test_tables(db_connection)
    cleanup_old_data(db_connection)
    
    # Сам тест
    create_user(db_connection, "test_user")
    user = get_user(db_connection, "test_user")
    
    # Проверка
    self.assertIsNotNone(user)
    
    # Очистка
    delete_user(db_connection, "test_user")
    drop_test_tables(db_connection)
    db_connection.close()
    
    
    
def setUp(self):
    self.db_connection = connect_to_database()
    create_test_tables(self.db_connection)
    
def tearDown(self):
    drop_test_tables(self.db_connection)
    self.db_connection.close()
    
def test_user_creation(self):
    create_user(self.db_connection, "test_user")
    user = get_user(self.db_connection, "test_user")
    self.assertIsNotNone(user)