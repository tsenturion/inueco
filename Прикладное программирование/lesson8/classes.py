"""
1. Класс Book
Добавьте методы для работы с статусом доступности книги

Реализуйте возможность оценивать книгу

2. Класс Student
Добавьте методы для работы с посещаемостью

Реализуйте функционал для определения успеваемости

3. Класс Rectangle
Добавьте методы для изменения размеров

Реализуйте функционал для сравнения прямоугольников

4. Класс BankAccount
Добавьте методы для работы с историей операций

Реализуйте функционал для начисления процентов

5. Класс Dog
Добавьте методы для работы с породой и навыками собаки

Реализуйте функционал для определения жизненного этапа

6. Класс Point2D
Добавьте методы для вычисления расстояний между точками

Реализуйте функционал для работы с координатами

7. Класс Lamp
Добавьте методы для работы с яркостью и цветом

Реализуйте функционал для создания световых эффектов

8. Класс SocialProfile
Добавьте методы для работы с лайками и подписчиками

Реализуйте функционал для анализа активности

9. Класс CoffeeMachine
Добавьте методы для работы с уровнем кофе и режимами

Реализуйте функционал для обслуживания аппарата

10. Класс GameCharacter
Добавьте методы для лечения и повышения уровня

Реализуйте функционал для инвентаря и экипировки
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.ratings = []
        self.average_rating = 0
    
    def get_info(self):
        status = "доступна" if self.is_available else "недоступна"
        return f"Книга: '{self.title}'. Автор: {self.author}. Статус: {status}. Рейтинг: {self.average_rating:.1f}"
    
    def borrow_book(self):
        """Взять книгу"""
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        """Вернуть книгу"""
        self.is_available = True
    
    def add_rating(self, rating):
        """Добавить оценку книге"""
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            self.average_rating = sum(self.ratings) / len(self.ratings)
            return True
        return False
    
    def get_rating_stats(self):
        """Получить статистику оценок"""
        if not self.ratings:
            return "Оценок пока нет"
        return f"Оценок: {len(self.ratings)}, Средняя: {self.average_rating:.1f}"


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
        self.attendance = {}
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def mark_attendance(self, date, status=True):
        """Отметить посещаемость"""
        self.attendance[date] = status
    
    def get_attendance_rate(self):
        """Получить процент посещаемости"""
        if not self.attendance:
            return 0
        present_days = sum(1 for status in self.attendance.values() if status)
        return (present_days / len(self.attendance)) * 100
    
    def get_performance(self):
        """Определить успеваемость"""
        avg_grade = self.get_average()
        attendance_rate = self.get_attendance_rate()
        
        if avg_grade >= 4.5 and attendance_rate >= 90:
            return "Отличная"
        elif avg_grade >= 3.5 and attendance_rate >= 80:
            return "Хорошая"
        elif avg_grade >= 3.0 and attendance_rate >= 70:
            return "Удовлетворительная"
        else:
            return "Неудовлетворительная"


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    def resize(self, new_length, new_width):
        """Изменить размеры"""
        self.length = new_length
        self.width = new_width
    
    def scale(self, factor):
        """Масштабировать прямоугольник"""
        self.length *= factor
        self.width *= factor
    
    def __eq__(self, other):
        """Сравнение на равенство"""
        return self.calculate_area() == other.calculate_area()
    
    def __lt__(self, other):
        """Сравнение на меньше"""
        return self.calculate_area() < other.calculate_area()
    
    def __gt__(self, other):
        """Сравнение на больше"""
        return self.calculate_area() > other.calculate_area()
    
    def compare(self, other):
        """Сравнить с другим прямоугольником"""
        area1 = self.calculate_area()
        area2 = other.calculate_area()
        
        if area1 > area2:
            return "Первый прямоугольник больше"
        elif area1 < area2:
            return "Второй прямоугольник больше"
        else:
            return "Прямоугольники равны по площади"


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
        self.interest_rate = 0.02  # 2% годовых
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Пополнение: +{amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            self.transaction_history.append(f"Попытка снятия: -{amount} (неудачно)")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Снятие: -{amount}")
        return True
    
    def get_transaction_history(self):
        """Получить историю операций"""
        return self.transaction_history
    
    def add_interest(self):
        """Начислить проценты"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Начисление процентов: +{interest:.2f}")
        return interest
    
    def set_interest_rate(self, rate):
        """Установить процентную ставку"""
        self.interest_rate = rate


class Dog:
    def __init__(self, name, age, breed="неизвестна"):
        self.name = name
        self.age = age
        self.breed = breed
        self.skills = []
    
    def bark(self):
        print("Гав!")
    
    def human_age(self):
        return self.age * 7
    
    def set_breed(self, breed):
        """Установить породу"""
        self.breed = breed
    
    def add_skill(self, skill):
        """Добавить навык"""
        if skill not in self.skills:
            self.skills.append(skill)
    
    def get_skills(self):
        """Получить список навыков"""
        return self.skills
    
    def get_life_stage(self):
        """Определить жизненный этап"""
        if self.age <= 1:
            return "Щенок"
        elif self.age <= 7:
            return "Взрослая собака"
        else:
            return "Пожилая собака"
    
    def perform_skill(self, skill):
        """Выполнить навык"""
        if skill in self.skills:
            print(f"{self.name} выполняет: {skill}")
            return True
        print(f"{self.name} не умеет: {skill}")
        return False


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to(self, other_point):
        """Расстояние до другой точки"""
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
    
    def move(self, dx, dy):
        """Переместить точку"""
        self.x += dx
        self.y += dy
    
    def set_coordinates(self, x, y):
        """Установить координаты"""
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        """Получить координаты"""
        return (self.x, self.y)
    
    def __str__(self):
        return f"Point2D({self.x}, {self.y})"


class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on
        self.brightness = 50  # от 0 до 100
        self.color = "white"
        self.colors = ["white", "warm white", "red", "green", "blue", "yellow"]
    
    def switch_on(self):
        self.is_on = True
    
    def switch_off(self):
        self.is_on = False
    
    def status(self):
        if self.is_on:
            return f"Светильник включен. Яркость: {self.brightness}%, Цвет: {self.color}"
        else:
            return "Светильник выключен"
    
    def set_brightness(self, level):
        """Установить яркость"""
        if 0 <= level <= 100:
            self.brightness = level
            return True
        return False
    
    def set_color(self, color):
        """Установить цвет"""
        if color in self.colors:
            self.color = color
            return True
        return False
    
    def create_effect(self, effect_name):
        """Создать световой эффект"""
        effects = {
            "disco": {"brightness": 100, "color": "random"},
            "romantic": {"brightness": 30, "color": "red"},
            "reading": {"brightness": 80, "color": "warm white"},
            "night_light": {"brightness": 10, "color": "blue"}
        }
        
        if effect_name in effects:
            effect = effects[effect_name]
            self.set_brightness(effect["brightness"])
            if effect["color"] != "random":
                self.set_color(effect["color"])
            else:
                import random
                self.set_color(random.choice([c for c in self.colors if c != "white"]))
            return f"Эффект '{effect_name}' активирован"
        return "Эффект не найден"


class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.likes = 0
        self.followers = set()
        self.following = set()
    
    def add_post(self, text):
        self.posts.append({"text": text, "likes": 0})
    
    def show_posts(self):
        for i, post in enumerate(self.posts, 1):
            print(f"{i}. {post['text']} ({post['likes']} лайков)")
    
    def like_post(self, post_index):
        """Лайкнуть пост"""
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]["likes"] += 1
            self.likes += 1
            return True
        return False
    
    def add_follower(self, username):
        """Добавить подписчика"""
        self.followers.add(username)
    
    def follow(self, username):
        """Подписаться на кого-то"""
        self.following.add(username)
    
    def get_engagement_rate(self):
        """Анализ активности - коэффициент вовлеченности"""
        if not self.posts:
            return 0
        total_posts = len(self.posts)
        followers_count = len(self.followers)
        
        if followers_count == 0:
            return 0
        
        avg_likes_per_post = self.likes / total_posts
        return (avg_likes_per_post / followers_count) * 100
    
    def get_activity_summary(self):
        """Получить сводку активности"""
        engagement = self.get_engagement_rate()
        
        if engagement > 10:
            activity_level = "Высокая"
        elif engagement > 5:
            activity_level = "Средняя"
        else:
            activity_level = "Низкая"
        
        return f"Подписчики: {len(self.followers)}, Лайки: {self.likes}, Активность: {activity_level}"


class CoffeeMachine:
    def __init__(self, water_level=0):
        self.water_level = water_level
        self.coffee_level = 0
        self.modes = ["espresso", "americano", "cappuccino"]
        self.current_mode = "espresso"
        self.maintenance_needed = False
    
    def add_water(self, amount):
        self.water_level += amount
    
    def add_coffee(self, amount):
        self.coffee_level += amount
    
    def make_coffee(self):
        water_needed = 200
        coffee_needed = 20
        
        if self.water_level >= water_needed and self.coffee_level >= coffee_needed:
            self.water_level -= water_needed
            self.coffee_level -= coffee_needed
            self.maintenance_needed = True
            return f"Кофе {self.current_mode} готов!"
        else:
            missing = []
            if self.water_level < water_needed:
                missing.append(f"воды (нужно {water_needed}, есть {self.water_level})")
            if self.coffee_level < coffee_needed:
                missing.append(f"кофе (нужно {coffee_needed}, есть {self.coffee_level})")
            return f"Недостаточно: {', '.join(missing)}"
    
    def set_mode(self, mode):
        """Установить режим приготовления"""
        if mode in self.modes:
            self.current_mode = mode
            return True
        return False
    
    def get_levels(self):
        """Получить уровни воды и кофе"""
        return f"Вода: {self.water_level}ml, Кофе: {self.coffee_level}g"
    
    def perform_maintenance(self):
        """Выполнить обслуживание"""
        if self.maintenance_needed:
            self.maintenance_needed = False
            return "Обслуживание выполнено"
        return "Обслуживание не требуется"


class GameCharacter:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.equipped = {}
    
    def attack(self, other_character):
        other_character.health -= self.damage
        print(f"{self.name} атакует {other_character.name} и наносит {self.damage} урона")
    
    def heal(self, amount):
        """Лечение персонажа"""
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} восстановил {amount} здоровья")
    
    def level_up(self):
        """Повышение уровня"""
        if self.experience >= self.level * 100:
            self.level += 1
            self.max_health += 20
            self.health = self.max_health
            self.damage += 5
            self.experience = 0
            print(f"{self.name} достиг {self.level} уровня!")
            return True
        return False
    
    def add_experience(self, exp):
        """Добавить опыт"""
        self.experience += exp
        print(f"{self.name} получил {exp} опыта")
        self.level_up()
    
    def add_to_inventory(self, item):
        """Добавить предмет в инвентарь"""
        self.inventory.append(item)
        print(f"{item} добавлен в инвентарь")
    
    def equip_item(self, item):
        """Экипировать предмет"""
        if item in self.inventory:
            # Определяем тип предмета по названию
            if "меч" in item.lower() or "оружие" in item.lower():
                self.equipped["weapon"] = item
                self.damage += 10
            elif "щит" in item.lower() or "броня" in item.lower():
                self.equipped["armor"] = item
                self.max_health += 30
                self.health += 30
            elif "кольцо" in item.lower():
                self.equipped["ring"] = item
                self.damage += 5
            
            self.inventory.remove(item)
            print(f"{item} экипирован")
            return True
        return False
    
    def get_character_info(self):
        """Получить информацию о персонаже"""
        return f"""
{self.name}
Уровень: {self.level}
Здоровье: {self.health}/{self.max_health}
Урон: {self.damage}
Опыт: {self.experience}/{self.level * 100}
Экипировка: {', '.join(self.equipped.values()) if self.equipped else 'нет'}
Инвентарь: {', '.join(self.inventory) if self.inventory else 'пуст'}
        """


# Демонстрация работы классов
if __name__ == "__main__":
    print("=== Демонстрация работы классов ===\n")
    
    # 1. Book
    book = Book("1984", "Джордж Оруэлл")
    book.borrow_book()
    book.add_rating(5)
    book.add_rating(4)
    print("1. Book:", book.get_info())
    
    # 2. Student
    student = Student("Иван")
    student.add_grade(5)
    student.add_grade(4)
    student.mark_attendance("2024-01-01", True)
    student.mark_attendance("2024-01-02", False)
    print("2. Student:", f"Успеваемость: {student.get_performance()}")
    
    # 3. Rectangle
    rect1 = Rectangle(5, 3)
    rect2 = Rectangle(4, 4)
    print("3. Rectangle:", rect1.compare(rect2))
    
    # 4. BankAccount
    account = BankAccount("Алексей", 1000)
    account.deposit(500)
    account.add_interest()
    print("4. BankAccount:", f"Баланс: {account.balance:.2f}")
    
    # 5. Dog
    dog = Dog("Бобик", 3, "Лабрадор")
    dog.add_skill("сидеть")
    dog.add_skill("лежать")
    print("5. Dog:", f"{dog.name} - {dog.get_life_stage()}")
    
    # 6. Point2D
    p1 = Point2D(3, 4)
    p2 = Point2D(0, 0)
    print("6. Point2D:", f"Расстояние: {p1.distance_to(p2):.2f}")
    
    # 7. Lamp
    lamp = Lamp()
    lamp.switch_on()
    lamp.set_brightness(75)
    lamp.create_effect("reading")
    print("7. Lamp:", lamp.status())
    
    # 8. SocialProfile
    profile = SocialProfile("user123")
    profile.add_post("Мой первый пост!")
    profile.like_post(0)
    profile.add_follower("friend1")
    print("8. SocialProfile:", profile.get_activity_summary())
    
    # 9. CoffeeMachine
    coffee_machine = CoffeeMachine()
    coffee_machine.add_water(500)
    coffee_machine.add_coffee(100)
    print("9. CoffeeMachine:", coffee_machine.make_coffee())
    
    # 10. GameCharacter
    hero = GameCharacter("Артур")
    hero.add_to_inventory("Стальной меч")
    hero.add_to_inventory("Кожаная броня")
    hero.equip_item("Стальной меч")
    hero.add_experience(120)
    print("10. GameCharacter:", hero.get_character_info())