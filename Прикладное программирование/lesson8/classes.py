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

from datetime import datetime, date
from math import sqrt
from enum import Enum

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
        """Взять книгу в аренду"""
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False
    
    def return_book(self):
        """Вернуть книгу"""
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
    
    def is_available(self):
        """Проверить доступность"""
        return self.available_copies > 0
    
    def add_rating(self, rating):
        """Добавить оценку книге"""
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            self.average_rating = sum(self.ratings) / len(self.ratings)
            return True
        return False
    
    def get_rating_info(self):
        """Получить информацию об оценках"""
        if not self.ratings:
            return "Нет оценок"
        return f"Средняя оценка: {self.average_rating:.1f} (всего оценок: {len(self.ratings)})"


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
    
    def mark_attendance(self, date_str=None, present=True):
        """Отметить посещаемость"""
        if date_str is None:
            date_str = datetime.now().strftime("%Y-%m-%d")
        self.attendance[date_str] = present
    
    def get_attendance_rate(self):
        """Получить процент посещаемости"""
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
        """Сравнение на равенство по площади"""
        return self.calculate_area() == other.calculate_area()
    
    def __lt__(self, other):
        """Сравнение по площади (меньше)"""
        return self.calculate_area() < other.calculate_area()
    
    def __gt__(self, other):
        """Сравнение по площади (больше)"""
        return self.calculate_area() > other.calculate_area()


class BankAccount:
    def __init__(self, owner, balance=0, interest_rate=0.01):
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
        self.transaction_history.append(f"Начисление процентов: +{interest:.2f}")
        return interest
    
    def get_transaction_history(self):
        """Получить историю операций"""
        return self.transaction_history
    
    def get_balance_with_projection(self, months=12):
        """Получить прогноз баланса с учетом процентов"""
        projected_balance = self.balance
        for _ in range(months):
            projected_balance *= (1 + self.interest_rate)
        return projected_balance


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
    
    def perform_skill(self, skill):
        """Выполнить навык"""
        if skill in self.skills:
            print(f"{self.name} выполняет: {skill}")
            return True
        print(f"{self.name} не умеет: {skill}")
        return False
    
    def get_life_stage(self):
        """Определить жизненный этап"""
        if self.age <= 1:
            return "Щенок"
        elif self.age <= 7:
            return "Взрослая собака"
        else:
            return "Пожилая собака"
    
    def get_skills_info(self):
        """Получить информацию о навыках"""
        if not self.skills:
            return f"{self.name} не имеет навыков"
        return f"{self.name} умеет: {', '.join(self.skills)}"


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to(self, other_point):
        """Вычислить расстояние до другой точки"""
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
    def move(self, dx=0, dy=0):
        """Переместить точку"""
        self.x += dx
        self.y += dy
    
    def set_coordinates(self, x, y):
        """Установить новые координаты"""
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        """Получить координаты"""
        return (self.x, self.y)
    
    def __str__(self):
        return f"Point2D({self.x}, {self.y})"


class Lamp:
    def __init__(self, is_on=False, brightness=50, color="white"):
        self.is_on = is_on
        self.brightness = max(0, min(100, brightness))  # 0-100%
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
        """Установить яркость"""
        self.brightness = max(0, min(100, level))
    
    def set_color(self, color):
        """Установить цвет"""
        self.color = color
    
    def create_effect(self, effect_name):
        """Создать световой эффект"""
        effects = {
            "романтика": {"brightness": 30, "color": "красный"},
            "работа": {"brightness": 80, "color": "белый"},
            "вечеринка": {"brightness": 100, "color": "разноцветный"},
            "расслабление": {"brightness": 20, "color": "синий"}
        }
        
        if effect_name in effects:
            effect = effects[effect_name]
            self.set_brightness(effect["brightness"])
            self.set_color(effect["color"])
            self.switch_on()
            return f"Эффект '{effect_name}' активирован"
        return "Неизвестный эффект"


class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.likes = 0
        self.followers = set()
        self.following = set()
    
    def add_post(self, text):
        self.posts.append({"text": text, "timestamp": datetime.now(), "likes": 0})
    
    def show_posts(self):
        for post in self.posts:
            print(f"{post['timestamp'].strftime('%Y-%m-%d %H:%M')}: {post['text']} (лайков: {post['likes']})")
    
    def like_post(self, post_index):
        """Поставить лайк посту"""
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]["likes"] += 1
            self.likes += 1
    
    def add_follower(self, username):
        """Добавить подписчика"""
        self.followers.add(username)
    
    def follow(self, username):
        """Подписаться на пользователя"""
        self.following.add(username)
    
    def analyze_activity(self):
        """Проанализировать активность"""
        total_posts = len(self.posts)
        total_likes = self.likes
        avg_likes_per_post = total_likes / total_posts if total_posts > 0 else 0
        
        activity_level = "высокая" if total_posts > 10 else "средняя" if total_posts > 5 else "низкая"
        popularity = "популярный" if avg_likes_per_post > 5 else "средний" if avg_likes_per_post > 2 else "начинающий"
        
        return {
            "total_posts": total_posts,
            "total_likes": total_likes,
            "avg_likes_per_post": avg_likes_per_post,
            "followers_count": len(self.followers),
            "following_count": len(self.following),
            "activity_level": activity_level,
            "popularity": popularity
        }


class CoffeeMachine:
    def __init__(self, water_level=0, coffee_level=0, mode="standby"):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.mode = mode
        self.maintenance_count = 0
    
    def add_water(self, amount):
        self.water_level += amount
    
    def add_coffee(self, amount):
        self.coffee_level += amount
    
    def make_coffee(self, coffee_type="эспрессо"):
        """Приготовить кофе"""
        recipes = {
            "эспрессо": {"water": 30, "coffee": 20},
            "американо": {"water": 100, "coffee": 20},
            "латте": {"water": 200, "coffee": 20}
        }
        
        if coffee_type not in recipes:
            return f"Неизвестный тип кофе: {coffee_type}"
        
        recipe = recipes[coffee_type]
        
        if self.water_level < recipe["water"]:
            return "Недостаточно воды"
        if self.coffee_level < recipe["coffee"]:
            return "Недостаточно кофе"
        
        self.water_level -= recipe["water"]
        self.coffee_level -= recipe["coffee"]
        self.mode = "brewing"
        
        return f"Приготовлен {coffee_type}! Осталось воды: {self.water_level}мл, кофе: {self.coffee_level}г"
    
    def set_mode(self, mode):
        """Установить режим работы"""
        valid_modes = ["standby", "brewing", "cleaning", "maintenance"]
        if mode in valid_modes:
            self.mode = mode
            return True
        return False
    
    def perform_maintenance(self):
        """Выполнить обслуживание"""
        self.maintenance_count += 1
        self.mode = "maintenance"
        return f"Обслуживание выполнено. Всего обслуживаний: {self.maintenance_count}"
    
    def get_status(self):
        """Получить статус аппарата"""
        return {
            "water_level": self.water_level,
            "coffee_level": self.coffee_level,
            "mode": self.mode,
            "maintenance_count": self.maintenance_count
        }


class GameCharacter:
    def __init__(self, name, health=100, damage=10, level=1):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.level = level
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
        self.damage += 5
        self.health = self.max_health  # полное исцеление при повышении уровня
    
    def add_to_inventory(self, item):
        """Добавить предмет в инвентарь"""
        self.inventory.append(item)
    
    def equip_item(self, item_name):
        """Экипировать предмет"""
        for item in self.inventory:
            if item["name"] == item_name:
                slot = item["slot"]
                self.equipped_items[slot] = item
                
                # Применить бонусы от предмета
                if "health_bonus" in item:
                    self.max_health += item["health_bonus"]
                if "damage_bonus" in item:
                    self.damage += item["damage_bonus"]
                
                return f"Экипирован: {item_name}"
        return "Предмет не найден в инвентаре"
    
    def get_character_info(self):
        """Получить информацию о персонаже"""
        return {
            "name": self.name,
            "level": self.level,
            "health": f"{self.health}/{self.max_health}",
            "damage": self.damage,
            "inventory_size": len(self.inventory),
            "equipped_items": list(self.equipped_items.keys())
        }
