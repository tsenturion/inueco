import unittest
from task_manager import TaskManager, Task


class TestTaskManagerBasic(unittest.TestCase):
    """Базовые тесты для TaskManager"""

    def setUp(self):
        """Создаёт новый экземпляр TaskManager для каждого теста"""
        self.manager = TaskManager()
        print(f"\nsetUp вызван для теста: {self._testMethodName}")

    def tearDown(self):
        """Очищает состояние менеджера задач после каждого теста"""
        self.manager.clear_all()
        print(f"tearDown вызван для теста: {self._testMethodName}")

    def test_add_task(self):
        """Тест добавления задачи"""
        # Добавляем задачу
        task_id = self.manager.add_task("Test task", "Test description")
        
        # Проверяем, что ID корректный
        self.assertEqual(task_id, 1)
        
        # Проверяем, что задача добавлена
        task = self.manager.get_task(task_id)
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Test task")
        self.assertEqual(task.description, "Test description")
        self.assertFalse(task.completed)
        
        # Проверяем увеличение next_id
        task_id2 = self.manager.add_task("Another task")
        self.assertEqual(task_id2, 2)

    def test_get_task(self):
        """Тест получения задачи по ID"""
        # Добавляем задачи
        task_id1 = self.manager.add_task("Task 1")
        task_id2 = self.manager.add_task("Task 2")
        
        # Проверяем получение существующих задач
        task1 = self.manager.get_task(task_id1)
        self.assertEqual(task1.title, "Task 1")
        
        task2 = self.manager.get_task(task_id2)
        self.assertEqual(task2.title, "Task 2")
        
        # Проверяем получение несуществующей задачи
        nonexistent_task = self.manager.get_task(999)
        self.assertIsNone(nonexistent_task)

    def test_complete_task(self):
        """Тест отметки задачи как выполненной"""
        # Добавляем задачу
        task_id = self.manager.add_task("Task to complete")
        
        # Проверяем начальное состояние
        task = self.manager.get_task(task_id)
        self.assertFalse(task.completed)
        
        # Отмечаем как выполненную
        result = self.manager.complete_task(task_id)
        self.assertTrue(result)
        
        # Проверяем изменение состояния
        task = self.manager.get_task(task_id)
        self.assertTrue(task.completed)
        
        # Проверяем списки выполненных/невыполненных задач
        completed_tasks = self.manager.get_completed_tasks()
        pending_tasks = self.manager.get_pending_tasks()
        
        self.assertEqual(len(completed_tasks), 1)
        self.assertEqual(len(pending_tasks), 0)
        
        # Проверяем попытку отметить несуществующую задачу
        result = self.manager.complete_task(999)
        self.assertFalse(result)

    def test_delete_task(self):
        """Тест удаления задачи"""
        # Добавляем задачи
        task_id1 = self.manager.add_task("Task 1")
        task_id2 = self.manager.add_task("Task 2")
        
        # Проверяем начальное количество
        self.assertEqual(len(self.manager.get_all_tasks()), 2)
        
        # Удаляем задачу
        result = self.manager.delete_task(task_id1)
        self.assertTrue(result)
        
        # Проверяем изменение количества
        self.assertEqual(len(self.manager.get_all_tasks()), 1)
        
        # Проверяем, что правильная задача удалена
        remaining_task = self.manager.get_task(task_id2)
        self.assertIsNotNone(remaining_task)
        self.assertEqual(remaining_task.title, "Task 2")
        
        # Проверяем удаление несуществующей задачи
        result = self.manager.delete_task(999)
        self.assertFalse(result)


class TestTaskManagerAdvanced(unittest.TestCase):
    """Расширенные тесты для TaskManager"""

    def setUp(self):
        """Создаём менеджер задач с тестовыми данными"""
        self.manager = TaskManager()
        
        # Добавляем тестовые задачи с разными статусами
        self.task_ids = []
        
        # Невыполненные задачи
        self.task_ids.append(self.manager.add_task(
            "Купить продукты", 
            "Молоко, хлеб, яйца"
        ))
        self.task_ids.append(self.manager.add_task(
            "Сделать домашнее задание",
            "Математика и физика"
        ))
        
        # Выполненные задачи
        self.task_ids.append(self.manager.add_task(
            "Позвонить маме",
            "Поздравить с днём рождения"
        ))
        self.manager.complete_task(self.task_ids[2])
        
        self.task_ids.append(self.manager.add_task(
            "Записаться к врачу",
            "Стоматолог на следующей неделе"
        ))
        self.manager.complete_task(self.task_ids[3])
        
        # Ещё невыполненная задача
        self.task_ids.append(self.manager.add_task(
            "Прочитать книгу",
            "Новый роман Достоевского"
        ))

    def test_get_all_tasks(self):
        """Тест получения всех задач"""
        all_tasks = self.manager.get_all_tasks()
        
        # Проверяем количество
        self.assertEqual(len(all_tasks), 5)
        
        # Проверяем, что все задачи имеют уникальные ID
        task_ids = [task.id for task in all_tasks]
        self.assertEqual(len(set(task_ids)), 5)
        
        # Проверяем содержимое
        titles = [task.title for task in all_tasks]
        expected_titles = [
            "Купить продукты",
            "Сделать домашнее задание",
            "Позвонить маме",
            "Записаться к врачу",
            "Прочитать книгу"
        ]
        for title in expected_titles:
            self.assertIn(title, titles)

    def test_search_tasks(self):
        """Тест поиска задач по ключевому слову"""
        # Поиск по заголовку (не зависит от регистра)
        results = self.manager.search_tasks("продукты")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Купить продукты")
        
        results = self.manager.search_tasks("ПРОДУКТЫ")
        self.assertEqual(len(results), 1)
        
        # Поиск по описанию
        results = self.manager.search_tasks("молоко")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].description, "Молоко, хлеб, яйца")
        
        # Поиск, который находит несколько задач
        results = self.manager.search_tasks("домашнее")
        self.assertEqual(len(results), 1)
        
        # Поиск, который не находит ничего
        results = self.manager.search_tasks("несуществующее")
        self.assertEqual(len(results), 0)
        
        # ИСПРАВЛЕННЫЙ ПОИСК: слово "на" есть только в описании одной задачи
        results = self.manager.search_tasks("на")
        self.assertEqual(len(results), 1)  # Только "Записаться к врачу"
        
        # Проверим, какая именно задача найдена
        found_titles = [task.title for task in results]
        self.assertIn("Записаться к врачу", found_titles)
        
        # Поиск слова "математика" (есть в описании)
        results = self.manager.search_tasks("математика")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Сделать домашнее задание")
        
        # Поиск по части слова (регистронезависимый)
        results = self.manager.search_tasks("достоевского")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Прочитать книгу")

    def test_task_isolation(self):
        """
        Докажите изоляцию тестов: 
        измените данные в этом тесте и убедитесь, 
        что другие тесты этого не видят
        """
        # Модифицируем состояние
        self.manager.add_task("Изолированная задача")
        self.manager.complete_task(self.task_ids[0])  # Отмечаем первую задачу как выполненную
        self.manager.delete_task(self.task_ids[1])    # Удаляем вторую задачу
        
        # Проверяем изменения
        all_tasks = self.manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 5)  # 5 исходных - 1 удаленная + 1 новая = 5
        
        # Проверяем выполненность первой задачи
        task1 = self.manager.get_task(self.task_ids[0])
        self.assertTrue(task1.completed)
        
        # Проверяем удаление второй задачи
        task2 = self.manager.get_task(self.task_ids[1])
        self.assertIsNone(task2)
        
        # Проверяем добавление новой задачи
        new_task_exists = False
        for task in all_tasks:
            if task.title == "Изолированная задача":
                new_task_exists = True
                break
        self.assertTrue(new_task_exists)
        
        print("Этот тест изменил данные, но другие тесты этого не увидят")


class TestTaskManagerEdgeCases(unittest.TestCase):
    """Тесты граничных случаев"""

    def setUp(self):
        self.manager = TaskManager()

    def test_empty_manager(self):
        """Тест пустого менеджера задач"""
        # Проверяем методы на пустом менеджере
        self.assertEqual(len(self.manager.get_all_tasks()), 0)
        self.assertEqual(len(self.manager.get_completed_tasks()), 0)
        self.assertEqual(len(self.manager.get_pending_tasks()), 0)
        
        # Поиск на пустом менеджере
        results = self.manager.search_tasks("что-то")
        self.assertEqual(len(results), 0)
        
        # Операции с несуществующими задачами
        self.assertFalse(self.manager.complete_task(1))
        self.assertFalse(self.manager.delete_task(1))
        self.assertIsNone(self.manager.get_task(1))

    def test_nonexistent_task(self):
        """Тест операций с несуществующей задачей"""
        # Добавляем реальную задачу для контекста
        real_task_id = self.manager.add_task("Реальная задача")
        
        # Пробуем операции с несуществующим ID
        self.assertFalse(self.manager.complete_task(999))
        self.assertFalse(self.manager.delete_task(999))
        self.assertIsNone(self.manager.get_task(999))
        
        # Проверяем, что реальная задача не пострадала
        real_task = self.manager.get_task(real_task_id)
        self.assertIsNotNone(real_task)
        self.assertEqual(real_task.title, "Реальная задача")
        
        # Проверяем, что ID следующей задачи не изменился
        next_id = self.manager.add_task("Следующая задача")
        self.assertEqual(next_id, 2)  # После первой задачи с ID=1

    def test_duplicate_titles(self):
        """Тест добавления задач с одинаковыми заголовками"""
        # Добавляем задачи с одинаковыми заголовками
        task_id1 = self.manager.add_task("Повторяющаяся задача")
        task_id2 = self.manager.add_task("Повторяющаяся задача")
        task_id3 = self.manager.add_task("Повторяющаяся задача", "Но с другим описанием")
        
        # Проверяем, что все задачи добавлены
        self.assertEqual(len(self.manager.get_all_tasks()), 3)
        
        # Проверяем, что у всех разные ID
        self.assertNotEqual(task_id1, task_id2)
        self.assertNotEqual(task_id2, task_id3)
        
        # Проверяем, что можем получить каждую задачу
        task1 = self.manager.get_task(task_id1)
        task2 = self.manager.get_task(task_id2)
        task3 = self.manager.get_task(task_id3)
        
        self.assertEqual(task1.title, task2.title)
        self.assertEqual(task2.title, task3.title)
        self.assertNotEqual(task1.description, task3.description)
        
        # Проверяем поиск - должен найти все три
        results = self.manager.search_tasks("Повторяющаяся")
        self.assertEqual(len(results), 3)


class TestTaskManagerWithoutSetup(unittest.TestCase):
    """
    Демонстрация проблемы: 
    что происходит, когда тесты используют общее состояние
    """
    
    # НЕ ИСПОЛЬЗУЙТЕ setUp здесь!
    manager = TaskManager()  # Общий для всех тестов (статическая переменная)

    def test_first(self):
        """Первый тест добавляет задачу"""
        # Этот тест добавляет задачу
        task_id = self.manager.add_task("Задача из первого теста")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.manager.get_all_tasks()), 1)
        print(f"Первый тест: добавлена задача с ID={task_id}")

    def test_second(self):
        """Второй тест видит задачу из первого теста - ЭТО ПРОБЛЕМА!"""
        # Этот тест ВИДИТ задачу из первого теста!
        # Это неправильно - тесты должны быть изолированы
        all_tasks = self.manager.get_all_tasks()
        
        # ВНИМАНИЕ: Этот assert может провалиться, если тесты запускаются в другом порядке!
        # Тесты не должны зависеть от порядка выполнения
        print(f"Второй тест: видит {len(all_tasks)} задач (должно быть 0 или 1)")
        
        # Это демонстрирует проблему:
        # Если тесты запускаются в порядке test_first, затем test_second,
        # то test_second увидит данные из test_first
        if len(all_tasks) > 0:
            print(f"ПРОБЛЕМА: Второй тест видит задачу из первого теста: {all_tasks[0].title}")
            
        # Правильный подход: каждый тест должен начинаться с чистого состояния
        # Именно для этого нужны setUp и tearDown
        
        # Проверяем, что это действительно проблема
        # Тесты не должны зависеть друг от друга!
        # В идеале этот тест должен работать независимо от порядка выполнения


class TestTaskManagerAdditional(unittest.TestCase):
    """Дополнительные тесты для демонстрации важности setUp/tearDown"""
    
    def setUp(self):
        """Демонстрация: setUp создаёт изолированное окружение для каждого теста"""
        self.manager = TaskManager()
        # Каждый тест получает СВОЙ собственный менеджер с 3 задачами
        self.task_ids = []
        for i in range(3):
            task_id = self.manager.add_task(f"Базовая задача {i+1}")
            self.task_ids.append(task_id)
        
        print(f"\nsetUp: создан менеджер с {len(self.task_ids)} задачами для {self._testMethodName}")
    
    def tearDown(self):
        """Демонстрация: tearDown очищает ресурсы после каждого теста"""
        self.manager.clear_all()
        print(f"tearDown: менеджер очищен для {self._testMethodName}")
    
    def test_independent_test_1(self):
        """Тест 1: работает с изолированными данными"""
        # Добавляем свою задачу
        new_id = self.manager.add_task("Задача теста 1")
        
        # Проверяем, что у нас 4 задачи (3 из setUp + 1 новая)
        self.assertEqual(len(self.manager.get_all_tasks()), 4)
        
        # Помечаем первую задачу как выполненную
        self.manager.complete_task(self.task_ids[0])
        
        # Проверяем изменения
        completed = self.manager.get_completed_tasks()
        self.assertEqual(len(completed), 1)
        
        print(f"Тест 1: ID новой задачи = {new_id}, выполненных задач = {len(completed)}")
    
    def test_independent_test_2(self):
        """Тест 2: тоже работает с изолированными данными"""
        # В ЭТОМ тесте у нас снова 3 задачи из setUp
        # (setUp вызывается заново для каждого теста!)
        
        # Удаляем первую задачу
        self.manager.delete_task(self.task_ids[0])
        
        # Проверяем, что осталось 2 задачи
        self.assertEqual(len(self.manager.get_all_tasks()), 2)
        
        # Добавляем новую задачу
        new_id = self.manager.add_task("Задача теста 2")
        
        # Теперь должно быть 3 задачи
        self.assertEqual(len(self.manager.get_all_tasks()), 3)
        
        print(f"Тест 2: после удаления и добавления задач осталось {len(self.manager.get_all_tasks())}")
    
    def test_test_order_independence(self):
        """Демонстрация: порядок выполнения тестов не важен"""
        # Этот тест всегда видит ровно 3 задачи из setUp
        # Не важно, какие тесты выполнялись до него
        
        all_tasks = self.manager.get_all_tasks()
        self.assertEqual(len(all_tasks), 3)
        
        # Проверяем, что все задачи новые (не из других тестов)
        for task in all_tasks:
            self.assertTrue(task.title.startswith("Базовая задача"))
        
        print(f"Тест независимости: всегда вижу {len(all_tasks)} базовых задач")


if __name__ == '__main__':
    unittest.main(verbosity=2)