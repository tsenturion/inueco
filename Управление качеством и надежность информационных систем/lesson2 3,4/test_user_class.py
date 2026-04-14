import unittest

class User:
    """Простой класс пользователя для тестирования"""
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
        self.is_active = True
    
    def add_post(self, post_content):
        """Добавляет пост пользователя"""
        self.posts.append(post_content)
        return len(self.posts)
    
    def deactivate(self):
        """Деактивирует пользователя"""
        self.is_active = False
        return self.is_active
    
    def get_post_count(self):
        """Возвращает количество постов"""
        return len(self.posts)


class TestUserClass(unittest.TestCase):
    """
    Практический пример тестирования класса User.
    Показывает правильное разделение подготовки и тестирования.
    """
    
    def setUp(self):
        """
        Подготавливаем свежего пользователя для каждого теста.
        """
        # Создаём нового пользователя
        self.user = User(
            username="testuser",
            email="test@example.com"
        )
        
        # Добавляем несколько начальных постов
        self.user.add_post("First post")
        self.user.add_post("Second post")
        
        print(f"\nsetUp создал пользователя: {self.user.username}")
        print(f"Начальное состояние: {self.user.get_post_count()} постов")
    
    def tearDown(self):
        """
        Очищаем ресурсы (если бы были внешние ресурсы)
        """
        print(f"tearDown вызван для: {self._testMethodName}")
        # В реальном проекте здесь могло бы быть:
        # - Закрытие соединений
        # - Откат транзакций
        # - Удаление временных данных
    
    def test_user_creation(self):
        """Тест проверяет корректность создания пользователя"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.is_active)
    
    def test_add_post(self):
        """Тест проверяет добавление поста"""
        initial_count = self.user.get_post_count()
        
        # Добавляем новый пост
        new_count = self.user.add_post("New post from test")
        
        # Проверяем результат
        self.assertEqual(new_count, initial_count + 1)
        self.assertEqual(self.user.posts[-1], "New post from test")
        self.assertEqual(self.user.get_post_count(), 3)
        
        print(f"После test_add_post: {self.user.get_post_count()} постов")
    
    def test_deactivate_user(self):
        """Тест проверяет деактивацию пользователя"""
        self.assertTrue(self.user.is_active)
        
        # Деактивируем
        result = self.user.deactivate()
        
        # Проверяем
        self.assertFalse(result)
        self.assertFalse(self.user.is_active)
        
        print(f"Пользователь деактивирован: {not self.user.is_active}")
    
    def test_post_count_after_operations(self):
        """Тест проверяет изоляцию - каждый тест получает свежего пользователя"""
        # Этот тест видит 2 начальных поста, а не 3 из test_add_post
        self.assertEqual(self.user.get_post_count(), 2)
        
        # Добавляем ещё посты
        self.user.add_post("Another post")
        self.user.add_post("One more post")
        
        self.assertEqual(self.user.get_post_count(), 4)
        
        print(f"test_post_count_after_operations: {self.user.get_post_count()} постов")


class TestUserEdgeCases(unittest.TestCase):
    """
    Отдельный класс для тестирования граничных случаев.
    Каждый тестовый класс имеет свою собственную setUp/tearDown.
    """
    
    def setUp(self):
        """Подготовка для тестов граничных случаев"""
        self.user = User("edgeuser", "edge@example.com")
    
    def test_empty_user_posts(self):
        """Тест для пользователя без постов"""
        self.assertEqual(self.user.get_post_count(), 0)
        self.assertEqual(len(self.user.posts), 0)
    
    def test_multiple_posts(self):
        """Тест добавления множества постов"""
        for i in range(10):
            self.user.add_post(f"Post {i+1}")
        
        self.assertEqual(self.user.get_post_count(), 10)
        self.assertEqual(self.user.posts[-1], "Post 10")


if __name__ == '__main__':
    unittest.main(verbosity=2)