# Практическое задание: Тестирование системы управления задачами (To-Do List)

## Цель

Научиться применять setUp и tearDown для создания изолированных, стабильных и поддерживаемых тестов на практике.

## Задание: Система управления задачами

Вы разрабатываете простую систему управления задачами. Вам нужно:

1. Реализовать класс TaskManager с базовыми операциями
2. Написать комплексные тесты с использованием setUp и tearDown
3. Обеспечить полную изоляцию тестов

## Шаг 1: Реализуйте класс TaskManager

Создайте файл `task_manager.py`:

```python
class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', completed={self.completed})"


class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, title, description=""):
        """Добавляет новую задачу и возвращает её ID"""
        task = Task(self.next_id, title, description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task.id

    def get_task(self, task_id):
        """Возвращает задачу по ID или None если не найдена"""
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        """Возвращает список всех задач"""
        return list(self.tasks.values())

    def get_completed_tasks(self):
        """Возвращает список выполненных задач"""
        return [task for task in self.tasks.values() if task.completed]

    def get_pending_tasks(self):
        """Возвращает список невыполненных задач"""
        return [task for task in self.tasks.values() if not task.completed]

    def complete_task(self, task_id):
        """Отмечает задачу как выполненную"""
        task = self.tasks.get(task_id)
        if task:
            task.mark_completed()
            return True
        return False

    def delete_task(self, task_id):
        """Удаляет задачу по ID"""
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    def search_tasks(self, keyword):
        """Ищет задачи по ключевому слову в заголовке или описании"""
        keyword = keyword.lower()
        results = []
        for task in self.tasks.values():
            if (keyword in task.title.lower() or 
                keyword in task.description.lower()):
                results.append(task)
        return results

    def clear_all(self):
        """Очищает все задачи"""
        self.tasks.clear()
```

## Шаг 2: Создайте базовые тесты с setUp и tearDown

Создайте файл `test_task_manager.py`:

```python
import unittest
from task_manager import TaskManager, Task


class TestTaskManagerBasic(unittest.TestCase):
    """Базовые тесты для TaskManager"""

    # TODO: Реализуйте методы setUp и tearDown
    # setUp должен создавать новый экземпляр TaskManager для каждого теста
    # tearDown должен очищать состояние менеджера задач

    # TODO: Напишите тесты:

    def test_add_task(self):
        """Тест добавления задачи"""
        pass  # Ваша реализация

    def test_get_task(self):
        """Тест получения задачи по ID"""
        pass  # Ваша реализация

    def test_complete_task(self):
        """Тест отметки задачи как выполненной"""
        pass  # Ваша реализация

    def test_delete_task(self):
        """Тест удаления задачи"""
        pass  # Ваша реализация


# TODO: Создайте второй тестовый класс для расширенных тестов
class TestTaskManagerAdvanced(unittest.TestCase):
    """Расширенные тесты для TaskManager"""

    def setUp(self):
        """Создаём менеджер задач с тестовыми данными"""
        pass  # Ваша реализация

    def test_get_all_tasks(self):
        """Тест получения всех задач"""
        pass  # Ваша реализация

    def test_search_tasks(self):
        """Тест поиска задач по ключевому слову"""
        pass  # Ваша реализация

    def test_task_isolation(self):
        """
        Докажите изоляцию тестов: 
        измените данные в этом тесте и убедитесь, 
        что другие тесты этого не видят
        """
        pass  # Ваша реализация
```

## Шаг 3: Реализуйте тесты с разными сценариями

Добавьте в `test_task_manager.py`:

```python
# TODO: Создайте тестовый класс для граничных случаев
class TestTaskManagerEdgeCases(unittest.TestCase):
    """Тесты граничных случаев"""

    def test_empty_manager(self):
        """Тест пустого менеджера задач"""
        pass  # Ваша реализация

    def test_nonexistent_task(self):
        """Тест операций с несуществующей задачей"""
        pass  # Ваша реализация

    def test_duplicate_titles(self):
        """Тест добавления задач с одинаковыми заголовками"""
        pass  # Ваша реализация


# TODO: Создайте тестовый класс, демонстрирующий проблему без setUp
class TestTaskManagerWithoutSetup(unittest.TestCase):
    """
    Демонстрация проблемы: 
    что происходит, когда тесты используют общее состояние
    """

    # НЕ ИСПОЛЬЗУЙТЕ setUp здесь!
    manager = TaskManager()  # Общий для всех тестов

    def test_first(self):
        """Первый тест добавляет задачу"""
        pass  # Ваша реализация

    def test_second(self):
        """Второй тест видит задачу из первого теста - ЭТО ПРОБЛЕМА!"""
        pass  # Ваша реализация
```

## Шаг 4: Создайте тесты с имитацией внешних ресурсов

Создайте файл `test_task_manager_with_resources.py`:

```python
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
        TODO: Создайте временный файл для тестов
        Имитация сохранения задач в файл
        """
        pass  # Ваша реализация

    def tearDown(self):
        """
        TODO: Удалите временный файл
        Убедитесь, что файл удаляется даже если тест упал
        """
        pass  # Ваша реализация

    def test_save_and_load(self):
        """Тест сохранения и загрузки задач из файла"""
        pass  # Ваша реализация

    def test_file_persistence(self):
        """
        Проверьте, что данные сохраняются между операциями
        и корректно очищаются в tearDown
        """
        pass  # Ваша реализация
```

## Подсказки по ключевым частям

### Для TestTaskManagerBasic

```python
def setUp(self):
    # Создайте новый TaskManager для каждого теста
    self.manager = TaskManager()
    # Можете добавить несколько тестовых задач для некоторых тестов

def test_add_task(self):
    # Добавьте задачу
    # Проверьте, что она добавилась
    # Проверьте, что ID увеличился

def test_complete_task(self):
    # Добавьте задачу
    # Отметьте её как выполненную
    # Проверьте статус completed
    # Проверьте, что она есть в get_completed_tasks()
```

### Для TestTaskManagerAdvanced

```python
def setUp(self):
    self.manager = TaskManager()
    # Добавьте 5-6 тестовых задач с разными статусами
    # Некоторые completed=True, некоторые completed=False
    # Разные заголовки и описания

def test_search_tasks(self):
    # Ищите задачи по ключевым словам
    # Проверьте, что поиск не зависит от регистра
    # Проверьте поиск и в заголовке и в описании
```

### Для TestTaskManagerWithFile

```python
def setUp(self):
    # Используйте tempfile.NamedTemporaryFile
    # Не забудьте delete=False
    # Сохраните путь к файлу в self.temp_file

def test_save_and_load(self):
    # Добавьте задачи в manager
    # Сохраните в файл (например, как JSON)
    # Создайте новый manager
    # Загрузите из файла
    # Проверьте, что задачи восстановились
```

## Что проверить перед отправкой (чек-лист)

### Обязательные проверки

1. **Изоляция тестов**: Каждый тест работает независимо
2. **setUp вызывается перед каждым тестом**: Используйте print или счётчик
3. **tearDown вызывается после каждого теста**: Даже при ошибке в тесте
4. **Нет побочных эффектов**: Тесты можно запускать в любом порядке
5. **Ресурсы очищаются**: Файлы удаляются, соединения закрываются

### Качество кода

1. **Тесты читаемы**: Названия методов понятны (test_что_тестируем_что_ожидаем)
2. **Минимум дублирования**: Общая логика в setUp
3. **Одна проверка на тест**: В идеале один assert на метод
4. **Документация**: Есть docstrings для классов и методов

### Покрытие функциональности

1. **Основные операции**: add, get, complete, delete
2. **Граничные случаи**: Пустые данные, несуществующие ID
3. **Поиск и фильтрация**: search_tasks, get_completed_tasks
4. **Ошибки и исключения**: Как система ведёт себя при ошибках

### Запуск тестов

```bash
# Все тесты проходят
python -m unittest discover -v

# Тесты изолированы (порядок не важен)
python -m unittest test_task_manager.TestTaskManagerBasic.test_add_task
python -m unittest test_task_manager.TestTaskManagerBasic.test_delete_task

# Ресурсы очищаются
# Проверьте, что временные файлы удаляются после тестов
```

## Советы по улучшению работы

### 1. **Используйте вспомогательные методы**

```python
def create_test_tasks(self, count=3):
    """Создаёт несколько тестовых задач"""
    task_ids = []
    for i in range(count):
        task_id = self.manager.add_task(f"Task {i}", f"Description {i}")
        task_ids.append(task_id)
    return task_ids
```

### 2. **Проверяйте не только успешные сценарии**

```python
def test_delete_nonexistent_task(self):
    """Попытка удалить несуществующую задачу"""
    result = self.manager.delete_task(999)
    self.assertFalse(result)  # Должно вернуть False
    self.assertEqual(len(self.manager.get_all_tasks()), 0)
```

### 3. **Тестируйте состояние после операций**

```python
def test_complete_task_changes_counts(self):
    """Проверка, что complete_task меняет counts"""
    initial_pending = len(self.manager.get_pending_tasks())
    initial_completed = len(self.manager.get_completed_tasks())

    # Добавляем и выполняем задачу
    task_id = self.manager.add_task("Test")
    self.manager.complete_task(task_id)

    # Проверяем изменения
    self.assertEqual(len(self.manager.get_pending_tasks()), initial_pending)
    self.assertEqual(len(self.manager.get_completed_tasks()), initial_completed + 1)
```

### 4. **Добавьте тесты на порядок выполнения**

```python
def test_setup_called_for_each_test(self):
    """Докажите, что setUp вызывается перед каждым тестом"""
    if not hasattr(self, 'setup_counter'):
        self.setup_counter = 0
    self.setup_counter += 1
    print(f"Setup вызван {self.setup_counter} раз для этого теста")

    # Запустите этот тест несколько раз
    # Убедитесь, что счётчик сбрасывается
```

### 5. **Создайте тест на race condition (продвинутый уровень)**

```python
class TestTaskManagerConcurrency(unittest.TestCase):
    """Тесты на потенциальные проблемы с параллельным доступом"""

    def setUp(self):
        self.manager = TaskManager()
        # Добавьте 100 задач
        for i in range(100):
            self.manager.add_task(f"Task {i}")

    def test_id_generation_under_load(self):
        """ID должны быть уникальными даже при быстром добавлении"""
        ids = set()
        for i in range(50):
            task_id = self.manager.add_task(f"Quick add {i}")
            ids.add(task_id)

        # Все ID должны быть уникальными
        self.assertEqual(len(ids), 50)
```

### 6. **Напишите интеграционный тест**

```python
def test_full_workflow(self):
    """Полный сценарий использования менеджера задач"""
    # 1. Создайте менеджер
    # 2. Добавьте 3 задачи
    # 3. Отметьте одну как выполненную
    # 4. Удалите одну
    # 5. Найдите задачу по ключевому слову
    # 6. Проверьте итоговое состояние

    # Этот тест проверяет, что все части работают вместе
```
