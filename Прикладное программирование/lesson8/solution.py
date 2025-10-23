class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_available = True
        self._ratings = []

    def get_info(self):
        status = "доступна" if self._is_available else "недоступна"
        return f"Книга: '{self.title}'. Автор: {self.author}. Статус: {status}"

    def borrow_book(self):
        if not self._is_available:
            return False
        self._is_available = False
        return True

    def return_book(self):
        self._is_available = True

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self._ratings.append(rating)

    def get_average_rating(self):
        if not self._ratings:
            return 0
        return round(sum(self._ratings) / len(self._ratings), 1)


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

    def mark_attendance(self, date, status):
        self.attendance[date] = status

    def get_attendance_rate(self):
        if not self.attendance:
            return 0
        present_days = sum(1 for status in self.attendance.values() if status)
        return present_days / len(self.attendance) * 100

    def get_performance(self):
        avg_grade = self.get_average()
        attendance_rate = self.get_attendance_rate()
        if avg_grade >= 4.5 and attendance_rate >= 90:
            return "Отличник"
        elif avg_grade >= 3.5 and attendance_rate >= 80:
            return "Хорошист"
        elif avg_grade >= 2.5 and attendance_rate >= 70:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()

    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()

    def __le__(self, other):
        return self.calculate_area() <= other.calculate_area()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            self.transaction_history.append("Неудачная попытка снятия")
            return False
        self.balance -= amount
        self.transaction_history.append(f"Снятие: -{amount}")
        return True

    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        self.transaction_history.append(f"Начислены проценты: +{interest:.2f}")

    def get_transaction_history(self):
        return self.transaction_history


class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.skills = []

    def bark(self):
        print("Гав!")

    def human_age(self):
        return self.age * 7

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_life_stage(self):
        if self.age <= 2:
            return "Щенок"
        elif 2 < self.age <= 8:
            return "Взрослый"
        else:
            return "Пожилой"


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5

    def distance_to_point(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_coordinates(self):
        return (self.x, self.y)


class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on
        self.brightness = 50
        self.color = "белый"

    def switch_on(self):
        self.is_on = True

    def switch_off(self):
        self.is_on = False

    def status(self):
        if self.is_on:
            print(f"Яркость: {self.brightness}%, Цвет: {self.color}")
        else:
            print("Светильник выключен")

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level

    def set_color(self, color):
        self.color = color

    def strobe_effect(self, duration=5):
        if self.is_on:
            print(f"Стробоскоп работает {duration} секунд")


class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.likes = 0
        self.followers = set()

    def add_post(self, text):
        self.posts.append(text)

    def show_posts(self):
        for post in self.posts:
            print(post)

    def like_post(self):
        self.likes += 1

    def add_follower(self, user):
        self.followers.add(user)

    def remove_follower(self, user):
        self.followers.discard(user)

    def get_engagement_rate(self):
        if not self.posts:
            return 0
        return self.likes / len(self.posts) * 100

    def get_activity_summary(self):
        return {
            'posts': len(self.posts),
            'likes': self.likes,
            'followers': len(self.followers),
            'engagement': self.get_engagement_rate()
        }


class CoffeeMachine:
    def __init__(self, water_level=0):
        self.water_level = water_level
        self.coffee_level = 0
        self.maintenance_needed = False

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def make_coffee(self):
        if self.water_level >= 200 and self.coffee_level >= 20:
            self.water_level -= 200
            self.coffee_level -= 20
            self.maintenance_needed = True
            return True
        else:
            print("Недостаточно воды или кофе")
            return False

    def perform_maintenance(self):
        self.maintenance_needed = False
        print("Обслуживание выполнено")

    def get_resources_status(self):
        return {
            'water': self.water_level,
            'coffee': self.coffee_level,
            'maintenance': self.maintenance_needed
        }


class GameCharacter:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = 1
        self.inventory = []
        self.equipped = {}

    def attack(self, other_character):
        other_character.health -= self.damage

    def heal(self, amount):
        self.health = min(100, self.health + amount)

    def level_up(self):
        self.level += 1
        self.damage += 5
        self.health = 100

    def add_item(self, item):
        self.inventory.append(item)

    def equip_item(self, item, slot):
        if item in self.inventory:
            self.equipped[slot] = item
            self.inventory.remove(item)

    def get_character_status(self):
        return {
            'name': self.name,
            'level': self.level,
            'health': self.health,
            'damage': self.damage,
            'inventory': self.inventory,
            'equipped': self.equipped
        }
