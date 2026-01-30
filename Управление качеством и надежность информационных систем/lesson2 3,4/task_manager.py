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
        self.next_id = 1