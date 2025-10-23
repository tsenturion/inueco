
from datetime import datetime

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.ratings = []
        self.current_reader = None
    
    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."
    
    def borrow_book(self, reader_name):
        if self.is_available:
            self.is_available = False
            self.current_reader = reader_name
            return True
        return False
    
    def return_book(self):
        self.is_available = True
        self.current_reader = None
    
    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
    
    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
    
    def get_status(self):
        if self.is_available:
            return "Доступна"
        return f"Выдана читателю: {self.current_reader}"


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
    
    def mark_attendance(self, date, present=True):
        self.attendance[date] = present
    
    def get_attendance_rate(self):
        if not self.attendance:
            return 0
        present_days = sum(1 for present in self.attendance.values() if present)
        return (present_days / len(self.attendance)) * 100
    
    def get_performance(self):
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
        self.length = new_length
        self.width = new_width
    
    def scale(self, factor):
        self.length *= factor
        self.width *= factor
    
    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()
    
    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()
    
    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transaction_history = []
        self.interest_rate = 0.02
    
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
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Начисление процентов: +{interest:.2f}")
    
    def get_transaction_history(self):
        return self.transaction_history
    
    def set_interest_rate(self, rate):
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
    
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
    
    def get_skills(self):
        return self.skills
    
    def get_life_stage(self):
        if self.age <= 1:
            return "Щенок"
        elif self.age <= 7:
            return "Взрослый"
        else:
            return "Пожилой"
    
    def can_perform(self, skill):
        return skill in self.skills


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on
        self.brightness = 50
        self.color = "white"
        self.colors = ["white", "warm white", "red", "green", "blue", "yellow"]
    
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
        if 0 <= level <= 100:
            self.brightness = level
    
    def set_color(self, color):
        if color in self.colors:
            self.color = color
    
    def create_effect(self, effect_name):
        effects = {
            "романтика": {"brightness": 30, "color": "warm white"},
            "вечеринка": {"brightness": 100, "color": "blue"},
            "чтение": {"brightness": 80, "color": "white"},
            "ночник": {"brightness": 10, "color": "warm white"}
        }
        
        if effect_name in effects:
            effect = effects[effect_name]
            self.set_brightness(effect["brightness"])
            self.set_color(effect["color"])
            self.switch_on()
            return f"Эффект '{effect_name}' установлен"
        return "Эффект не найден"


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
            print(f"{post['text']} (Лайков: {post['likes']})")
    
    def like_post(self, post_index):
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]['likes'] += 1
            self.likes += 1
    
    def add_follower(self, username):
        self.followers.add(username)
    
    def follow(self, username):
        self.following.add(username)
    
    def get_engagement_rate(self):
        if not self.followers:
            return 0
        return (self.likes / len(self.followers)) * 100 if self.followers else 0
    
    def get_activity_summary(self):
        return {
            "posts": len(self.posts),
            "total_likes": self.likes,
            "followers": len(self.followers),
            "following": len(self.following),
            "engagement_rate": f"{self.get_engagement_rate():.1f}%"
        }


class CoffeeMachine:
    def __init__(self, water_level=0, coffee_level=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.modes = ["эспрессо", "американо", "латте"]
        self.current_mode = "эспрессо"
        self.maintenance_count = 0
    
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
            self.maintenance_count += 1
            return f"Кофе {self.current_mode} готов!"
        else:
            if self.water_level < water_needed:
                return "Недостаточно воды"
            return "Недостаточно кофе"
    
    def set_mode(self, mode):
        if mode in self.modes:
            self.current_mode = mode
    
    def needs_maintenance(self):
        return self.maintenance_count >= 10
    
    def perform_maintenance(self):
        self.maintenance_count = 0
        return "Обслуживание выполнено"
    
    def get_status(self):
        status = f"Вода: {self.water_level}мл, Кофе: {self.coffee_level}г"
        if self.needs_maintenance():
            status += " - Требуется обслуживание!"
        return status


class GameCharacter:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.level = 1
        self.experience = 0
        self.inventory = []
        self.equipped_items = {}
    
    def attack(self, other_character):
        other_character.health -= self.damage
    
    def heal(self, amount):
        self.health = min(self.health + amount, self.max_health)
    
    def level_up(self):
        self.level += 1
        self.max_health += 20
        self.damage += 5
        self.health = self.max_health
    
    def add_experience(self, exp):
        self.experience += exp
        if self.experience >= self.level * 100:
            self.level_up()
            self.experience = 0
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def equip_item(self, item_name):
        for item in self.inventory:
            if item['name'] == item_name:
                slot = item['slot']
                self.equipped_items[slot] = item
                if 'health_bonus' in item:
                    self.max_health += item['health_bonus']
                if 'damage_bonus' in item:
                    self.damage += item['damage_bonus']
                break
    
    def get_character_info(self):
        return {
            "name": self.name,
            "level": self.level,
            "health": f"{self.health}/{self.max_health}",
            "damage": self.damage,
            "experience": self.experience,
            "inventory_size": len(self.inventory),
            "equipped_items": list(self.equipped_items.keys())
        }