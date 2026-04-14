import unittest
import time

class TestExpensiveSetup(unittest.TestCase):
    """
    Демонстрация setUpClass и tearDownClass.
    Эти методы вызываются один раз для всего класса.
    Полезно для дорогих операций (подключение к БД и т.д.)
    """
    
    @classmethod
    def setUpClass(cls):
        """
        Вызывается ОДИН раз перед всеми тестами класса.
        Имитируем дорогую операцию (например, загрузка данных).
        """
        print("\n" + "="*60)
        print("Вызывается setUpClass (один раз для всего класса)")
        print("Имитация дорогой операции...")
        time.sleep(0.5)  # Имитация долгой операции
        
        # Классовые атрибуты (доступны через cls или self)
        cls.shared_data = [1, 2, 3, 4, 5]
        cls.cache = {"key": "value"}
        
        print(f"Создан shared_data: {cls.shared_data}")
        print(f"Создан cache: {cls.cache}")
        print("="*60)
    
    @classmethod
    def tearDownClass(cls):
        """
        Вызывается ОДИН раз после всех тестов класса.
        """
        print("\n" + "="*60)
        print("Вызывается tearDownClass (один раз для всего класса)")
        cls.shared_data.clear()
        cls.cache.clear()
        print("Общие данные очищены")
        print("="*60)
    
    def setUp(self):
        """
        Вызывается перед каждым тестом.
        Здесь можно делать лёгкую подготовку.
        """
        self.local_data = self.shared_data.copy()  # Копируем общие данные
        print(f"\nsetUp для {self._testMethodName}: создана копия shared_data")
    
    def test_sum_of_shared_data(self):
        """Тест использует общие данные"""
        result = sum(self.shared_data)
        self.assertEqual(result, 15)
        
        # Изменяем shared_data - это повлияет на другие тесты!
        self.shared_data.append(6)
        print(f"test_sum_of_shared_data: добавили 6, теперь shared_data = {self.shared_data}")
    
    def test_shared_data_length(self):
        """Этот тест увидит изменение из предыдущего теста!"""
        # Внимание: shared_data был изменён в предыдущем тесте!
        # Это пример проблемы с shared state
        self.assertEqual(len(self.shared_data), 6)  # Было 5, стало 6!
        print(f"test_shared_data_length: длина shared_data = {len(self.shared_data)}")
    
    def test_local_data_isolation(self):
        """Этот тест использует локальную копию, поэтому изолирован"""
        self.assertEqual(len(self.local_data), 5)  # Всегда 5
        self.local_data.append(100)  # Изменяем только локальную копию
        self.assertEqual(len(self.local_data), 6)
        print(f"test_local_data_isolation: local_data = {self.local_data}")
    
    def test_cache_access(self):
        """Тест работает с общим кэшем"""
        self.assertIn("key", self.cache)
        self.cache["new_key"] = "new_value"
        print(f"test_cache_access: cache = {self.cache}")


if __name__ == '__main__':
    unittest.main(verbosity=2)