import unittest
import tempfile
import json
import os
from task_manager import TaskManager, Task


class TestTaskManagerWithFile(unittest.TestCase):
    """
    Тесты с работой с файлами.
    Демонстрация важности tearDown для очистки ресурсов.
    """

    def setUp(self):
        """
        Создаём временный файл для тестов
        Имитация сохранения задач в файл
        """
        # Создаём временный файл
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w+', 
            delete=False,  # Не удалять автоматически
            suffix='.json',
            prefix='test_tasks_'
        )
        self.temp_file.close()  # Закрываем для использования в тестах
        self.file_path = self.temp_file.name
        
        print(f"Создан временный файл: {self.file_path}")
        
        # Создаём менеджер задач для тестов
        self.manager = TaskManager()

    def tearDown(self):
        """
        Удаляем временный файл
        Убеждаемся, что файл удаляется даже если тест упал
        """
        try:
            if os.path.exists(self.file_path):
                os.unlink(self.file_path)  # Удаляем файл
                print(f"Удалён временный файл: {self.file_path}")
        except Exception as e:
            print(f"Ошибка при удалении файла: {e}")
            # Продолжаем выполнение, не прерываем из-за ошибки очистки

    def save_tasks_to_file(self, tasks):
        """Сохраняет задачи в файл в формате JSON"""
        tasks_data = []
        for task in tasks:
            task_data = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed
            }
            tasks_data.append(task_data)
        
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(tasks_data, f, ensure_ascii=False, indent=2)

    def load_tasks_from_file(self):
        """Загружает задачи из файла"""
        if not os.path.exists(self.file_path):
            return []
        
        with open(self.file_path, 'r', encoding='utf-8') as f:
            tasks_data = json.load(f)
        
        return tasks_data

    def test_save_and_load(self):
        """Тест сохранения и загрузки задач из файла"""
        # Добавляем задачи в manager
        task_ids = []
        task_ids.append(self.manager.add_task("Задача 1", "Описание 1"))
        task_ids.append(self.manager.add_task("Задача 2", "Описание 2"))
        self.manager.complete_task(task_ids[0])  # Первую отмечаем как выполненную
        
        # Получаем все задачи
        tasks = self.manager.get_all_tasks()
        
        # Сохраняем в файл
        self.save_tasks_to_file(tasks)
        
        # Проверяем, что файл создан и не пустой
        self.assertTrue(os.path.exists(self.file_path))
        file_size = os.path.getsize(self.file_path)
        self.assertGreater(file_size, 0)
        
        # Загружаем из файла
        loaded_data = self.load_tasks_from_file()
        
        # Проверяем, что данные корректны
        self.assertEqual(len(loaded_data), 2)
        
        # Проверяем первую задачу
        self.assertEqual(loaded_data[0]['title'], "Задача 1")
        self.assertEqual(loaded_data[0]['description'], "Описание 1")
        self.assertTrue(loaded_data[0]['completed'])
        
        # Проверяем вторую задачу
        self.assertEqual(loaded_data[1]['title'], "Задача 2")
        self.assertEqual(loaded_data[1]['description'], "Описание 2")
        self.assertFalse(loaded_data[1]['completed'])

    def test_file_persistence(self):
        """
        Проверяем, что данные сохраняются между операциями
        и корректно очищаются в tearDown
        """
        # Добавляем задачу
        task_id = self.manager.add_task("Постоянная задача", "Должна сохраниться")
        
        # Сохраняем
        tasks = self.manager.get_all_tasks()
        self.save_tasks_to_file(tasks)
        
        # Читаем файл напрямую для проверки
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Проверяем, что задача в файле
        self.assertIn("Постоянная задача", content)
        self.assertIn("Должна сохраниться", content)
        
        # Имитируем перезапуск приложения: создаём новый менеджер
        new_manager = TaskManager()
        
        # Загружаем данные из файла
        loaded_data = self.load_tasks_from_file()
        
        # Восстанавливаем задачи в новом менеджере
        for task_data in loaded_data:
            # В реальном приложении нужно обрабатывать ID, но для теста упрощаем
            print(f"Загружена задача: {task_data['title']}")

    def test_empty_file(self):
        """Тест работы с пустым файлом"""
        # Сохраняем пустой список
        self.save_tasks_to_file([])
        
        # Загружаем
        loaded_data = self.load_tasks_from_file()
        
        # Проверяем
        self.assertEqual(len(loaded_data), 0)
        self.assertEqual(loaded_data, [])

    def test_file_not_exists(self):
        """Тест обработки отсутствующего файла"""
        # Удаляем файл, если существует
        if os.path.exists(self.file_path):
            os.unlink(self.file_path)
        
        # Пробуем загрузить из несуществующего файла
        loaded_data = self.load_tasks_from_file()
        
        # Должен вернуться пустой список
        self.assertEqual(loaded_data, [])


class TestTaskManagerWithDatabaseMock(unittest.TestCase):
    """Тесты с имитацией работы с базой данных"""
    
    def setUp(self):
        """Создаём мок базы данных"""
        self.manager = TaskManager()
        
        # Имитируем таблицу в "базе данных"
        self.mock_database = {
            'tasks': [],
            'next_id': 1
        }
        
    def mock_save_to_db(self):
        """Сохраняем задачи в мок базу данных"""
        self.mock_database['tasks'] = []
        for task in self.manager.get_all_tasks():
            self.mock_database['tasks'].append({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'completed': task.completed
            })
        self.mock_database['next_id'] = self.manager.next_id
        
    def mock_load_from_db(self):
        """Загружаем задачи из мок базы данных"""
        self.manager.clear_all()
        for task_data in self.mock_database['tasks']:
            # Восстанавливаем задачу
            task = Task(
                task_data['id'],
                task_data['title'],
                task_data['description'],
                task_data['completed']
            )
            self.manager.tasks[task_data['id']] = task
            self.manager.next_id = max(self.manager.next_id, task_data['id'] + 1)
    
    def tearDown(self):
        """Очищаем мок базу данных"""
        self.mock_database.clear()
    
    def test_database_persistence(self):
        """Тест сохранения и загрузки из базы данных"""
        # Добавляем задачи
        self.manager.add_task("DB Task 1", "Description 1")
        self.manager.add_task("DB Task 2", "Description 2")
        
        # Сохраняем в "БД"
        self.mock_save_to_db()
        
        # Проверяем сохранение
        self.assertEqual(len(self.mock_database['tasks']), 2)
        self.assertEqual(self.mock_database['next_id'], 3)
        
        # Создаём новый менеджер
        new_manager = TaskManager()
        self.manager = new_manager
        
        # Загружаем из "БД"
        self.mock_load_from_db()
        
        # Проверяем загрузку
        all_tasks = self.manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 2)
        self.assertEqual(all_tasks[0].title, "DB Task 1")
        self.assertEqual(all_tasks[1].title, "DB Task 2")


if __name__ == '__main__':
    unittest.main(verbosity=2)