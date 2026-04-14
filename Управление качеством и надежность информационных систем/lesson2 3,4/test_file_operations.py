import unittest
import os
import tempfile

class TestFileOperations(unittest.TestCase):
    """
    Пример с файлами, где tearDown особенно важен.
    Показывает необходимость очистки ресурсов.
    """
    
    def setUp(self):
        """
        Создаём временный файл для каждого теста.
        """
        print(f"\nВызывается setUp для: {self._testMethodName}")
        # Создаём временный файл
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w', 
            delete=False,  # Не удалять автоматически
            suffix='.txt'
        )
        self.filename = self.temp_file.name
        
        # Записываем начальные данные
        self.temp_file.write("Hello, World!\n")
        self.temp_file.write("This is a test file.\n")
        self.temp_file.close()
        
        print(f"Создан файл: {self.filename}")
    
    def tearDown(self):
        """
        Удаляем временный файл после каждого теста.
        Важно: вызывается даже если тест упал!
        """
        print(f"Вызывается tearDown для: {self._testMethodName}")
        if os.path.exists(self.filename):
            os.unlink(self.filename)
            print(f"Файл удалён: {self.filename}")
    
    def test_file_exists(self):
        """Проверяем, что файл создан"""
        self.assertTrue(os.path.exists(self.filename))
        
        # Проверяем содержимое
        with open(self.filename, 'r') as f:
            content = f.read()
            self.assertIn("Hello, World!", content)
    
    def test_file_write(self):
        """Проверяем запись в файл"""
        # Дописываем в файл
        with open(self.filename, 'a') as f:
            f.write("New line added by test.\n")
        
        # Проверяем, что добавилась строка
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), 3)
            self.assertIn("New line added", lines[2])
    
    def test_file_size(self):
        """Проверяем размер файла"""
        size = os.path.getsize(self.filename)
        self.assertGreater(size, 0)
        print(f"Размер файла: {size} байт")


if __name__ == '__main__':
    unittest.main(verbosity=2)