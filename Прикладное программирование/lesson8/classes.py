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


from cmath import sqrt
import datetime


class Book:
    def __init__(self, title, author, total_copies=1):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.ratings = []
        self.average_rating = 0
    
    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."
    
    def borrow_book(self):
        """Взять книгу (уменьшить количество доступных копий)"""
        if self.is_available():
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        """Вернуть книгу (увеличить количество доступных копий)"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def is_available(self):
        """Проверить доступность книги"""
        return self.available_copies > 0
    
    def add_rating(self, rating):
        """Добавить оценку книге (от 1 до 5)"""
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            self.average_rating = sum(self.ratings) / len(self.ratings)
            return True
        return False
    
    def get_rating_info(self):
        """Получить информацию об оценках"""
        if not self.ratings:
            return "Нет оценок"
        return f"Средняя оценка: {self.average_rating:.1f} (оценок: {len(self.ratings)})"


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
        self.attendance = {}  # дата: присутствие
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def mark_attendance(self, date_str, present=True):
        """Отметить посещаемость"""
        self.attendance[date_str] = present
    
    def get_attendance_rate(self):
        """Рассчитать процент посещаемости"""
        if not self.attendance:
            return 0
        present_days = sum(1 for present in self.attendance.values() if present)
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
    
    def resize(self, new_length=None, new_width=None):
        """Изменить размеры прямоугольника"""
        if new_length is not None:
            self.length = new_length
        if new_width is not None:
            self.width = new_width
    
    def scale(self, factor):
        """Масштабировать прямоугольник"""
        self.length *= factor
        self.width *= factor
    
    def __eq__(self, other):
        """Проверка на равенство площадей"""
        return self.calculate_area() == other.calculate_area()
    
    def __lt__(self, other):
        """Сравнение по площади"""
        return self.calculate_area() < other.calculate_area()
    
    def __gt__(self, other):
        """Сравнение по площади"""
        return self.calculate_area() > other.calculate_area()


class BankAccount:
    def __init__(self, owner, balance=0, interest_rate=0.02):
        self.owner = owner
        self.balance = balance
        self.interest_rate = interest_rate
        self.transaction_history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Пополнение: +{amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            self.transaction_history.append(f"Попытка снятия: -{amount} (недостаточно средств)")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Снятие: -{amount}")
        return True
    
    def add_interest(self):
        """Начислить проценты"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Начислены проценты: +{interest:.2f}")
        return interest
    
    def get_transaction_history(self):
        """Получить историю операций"""
        return self.transaction_history
    
    def get_balance_statement(self):
        """Получить выписку с балансом"""
        return f"Баланс: {self.balance:.2f}"


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
    
    def add_skill(self, skill):
        """Добавить навык собаке"""
        if skill not in self.skills:
            self.skills.append(skill)
    
    def get_skills(self):
        """Получить список навыков"""
        return self.skills
    
    def get_life_stage(self):
        """Определить жизненный этап"""
        if self.age < 1:
            return "Щенок"
        elif self.age < 3:
            return "Молодая собака"
        elif self.age < 8:
            return "Взрослая собака"
        else:
            return "Пожилая собака"
    
    def change_breed(self, new_breed):
        """Изменить породу"""
        self.breed = new_breed


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to_point(self, other_point):
        """Вычислить расстояние до другой точки"""
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
    def move(self, dx, dy):
        """Переместить точку"""
        self.x += dx
        self.y += dy
    
    def get_coordinates(self):
        """Получить координаты"""
        return (self.x, self.y)
    
    def set_coordinates(self, x, y):
        """Установить новые координаты"""
        self.x = x
        self.y = y


class Lamp:
    def __init__(self, is_on=False, brightness=50, color="white"):
        self.is_on = is_on
        self.brightness = brightness  # 0-100
        self.color = color
    
    def switch_on(self):
        self.is_on = True
    
    def switch_off(self):
        self.is_on = False
    
    def status(self):
        if self.is_on:
            print(f"Светильник включен. Яркость: {self.brightness}%, Цвет: {self.color}")
        else:
            print("Светильник выключен")
    
    def set_brightness(self, level):
        """Установить уровень яркости (0-100)"""
        if 0 <= level <= 100:
            self.brightness = level
            return True
        return False
    
    def set_color(self, color):
        """Установить цвет"""
        self.color = color
    
    def create_light_effect(self, effect_type):
        """Создать световой эффект"""
        effects = {
            "радуга": "Режим радуги активирован",
            "пульсация": "Пульсирующий свет включен",
            "рассвет": "Эффект рассвета активирован",
            "закат": "Эффект заката активирован"
        }
        return effects.get(effect_type, "Неизвестный эффект")


class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.likes = 0
        self.followers = []
        self.following = []
    
    def add_post(self, text):
        self.posts.append({"text": text, "likes": 0, "timestamp": datetime.now()})
    
    def show_posts(self):
        for post in self.posts:
            print(f"{post['timestamp'].strftime('%Y-%m-%d %H:%M')}: {post['text']} (лайков: {post['likes']})")
    
    def like_post(self, post_index):
        """Поставить лайк посту"""
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]['likes'] += 1
            self.likes += 1
    
    def add_follower(self, username):
        """Добавить подписчика"""
        if username not in self.followers:
            self.followers.append(username)
    
    def follow(self, username):
        """Подписаться на другого пользователя"""
        if username not in self.following:
            self.following.append(username)
    
    def get_activity_analysis(self):
        """Анализ активности"""
        total_posts = len(self.posts)
        total_likes = self.likes
        avg_likes_per_post = total_likes / total_posts if total_posts > 0 else 0
        
        analysis = {
            "total_posts": total_posts,
            "total_likes": total_likes,
            "followers": len(self.followers),
            "following": len(self.following),
            "avg_likes_per_post": avg_likes_per_post,
            "engagement_rate": (total_likes / len(self.followers)) * 100 if self.followers else 0
        }
        return analysis


class CoffeeMachine:
    def __init__(self, water_level=0, coffee_level=0):
        self.water_level = water_level  # мл
        self.coffee_level = coffee_level  # г
        self.modes = ["эспрессо", "американо", "капучино"]
        self.current_mode = "эспрессо"
        self.maintenance_count = 0
    
    def add_water(self, amount):
        self.water_level += amount
    
    def add_coffee(self, amount):
        self.coffee_level += amount
    
    def make_coffee(self):
        water_needed = 200
        coffee_needed = 15
        
        if self.water_level >= water_needed and self.coffee_level >= coffee_needed:
            self.water_level -= water_needed
            self.coffee_level -= coffee_needed
            self.maintenance_count += 1
            return f"Кофе {self.current_mode} готов!"
        else:
            return "Недостаточно ингредиентов для приготовления кофе"
    
    def set_mode(self, mode):
        """Установить режим приготовления"""
        if mode in self.modes:
            self.current_mode = mode
            return True
        return False
    
    def get_ingredients_status(self):
        """Получить статус ингредиентов"""
        return f"Вода: {self.water_level}мл, Кофе: {self.coffee_level}г"
    
    def perform_maintenance(self):
        """Обслуживание аппарата"""
        self.maintenance_count = 0
        return "Обслуживание завершено"
    
    def needs_maintenance(self):
        """Проверить необходимость обслуживания"""
        return self.maintenance_count >= 10


class GameCharacter:
    def __init__(self, name, health=100, damage=10, level=1):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.level = level
        self.experience = 0
        self.inventory = []
        self.equipped_items = {}
    
    def attack(self, other_character):
        other_character.health -= self.damage
    
    def heal(self, amount):
        """Лечение персонажа"""
        self.health = min(self.max_health, self.health + amount)
    
    def level_up(self):
        """Повышение уровня"""
        self.level += 1
        self.max_health += 20
        self.health = self.max_health
        self.damage += 5
        self.experience = 0
    
    def add_experience(self, exp):
        """Добавить опыт"""
        self.experience += exp
        if self.experience >= self.level * 100:
            self.level_up()
    
    def add_to_inventory(self, item):
        """Добавить предмет в инвентарь"""
        self.inventory.append(item)
    
    def equip_item(self, item, slot):
        """Экипировать предмет"""
        self.equipped_items[slot] = item
        # Применить бонусы от предмета
        if 'health_bonus' in item:
            self.max_health += item['health_bonus']
        if 'damage_bonus' in item:
            self.damage += item['damage_bonus']
    
    def get_character_info(self):
        """Получить информацию о персонаже"""
        return {
            "name": self.name,
            "level": self.level,
            "health": f"{self.health}/{self.max_health}",
            "damage": self.damage,
            "experience": f"{self.experience}/{self.level * 100}",
            "inventory_size": len(self.inventory),
            "equipped_items": list(self.equipped_items.keys())
        }