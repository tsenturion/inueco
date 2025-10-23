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
        self.available = True
        self.ratings = []
    
    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."
    
    def set_available(self, status):
        self.available = status

    def is_available(self):
        return self.available
    
    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
        self.attendance = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    def mark_attendance(self, date, present=True):
        self.attendance.append((date, present))

    def get_attendance_rate(self):
        if not self.attendance:
            return 0
        present_count = sum(1 for _, p in self.attendance if p)
        return present_count / len(self.attendance)


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

    def is_larger(self, other):
        return self.calculate_area() > other.calculate_area()

    def is_equal(self, other):
        return self.calculate_area() == other.calculate_area()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.history.append(f"Снятие: -{amount}")
        return True

    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        self.history.append(f"Начислены проценты: +{interest}")

    def show_history(self):
        for record in self.history:
            print(record)


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

    def show_skills(self):
        return self.skills

    def life_stage(self):
        if self.age < 2:
            return "Щенок"
        elif self.age < 7:
            return "Взрослый"
        else:
            return "Пожилой"


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_coords(self):
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
            print("Светильник включен")
        else:
            print("Светильник выключен")

    def set_brightness(self, level):
        self.brightness = level

    def set_color(self, color):
        self.color = color

    def effect_blink(self):
        if self.is_on:
            print(f"Мигание цветом {self.color}")


class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.likes = 0
        self.followers = []
    
    def add_post(self, text):
        self.posts.append(text)

    def show_posts(self):
        for post in self.posts:
            print(post)

    def like_post(self):
        self.likes += 1

    def add_follower(self, user):
        self.followers.append(user)

    def remove_follower(self, user):
        if user in self.followers:
            self.followers.remove(user)

    def get_likes_count(self):
        return self.likes

    def get_followers_count(self):
        return len(self.followers)

    def analyze_activity(self):
        post_count = len(self.posts)
        like_ratio = self.likes / post_count if post_count > 0 else 0
        return f"Постов: {post_count}, Лайков: {self.likes}, Соотношение: {like_ratio:.2f}"


class CoffeeMachine:
    def __init__(self, water_level=0, coffee_level=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.mode = "обычный"

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def make_coffee(self):
        if self.water_level >= 200 and self.coffee_level >= 20:
            self.water_level -= 200
            self.coffee_level -= 20
            return True
        else:
            print("Недостаточно воды или кофе")
            return False

    def set_mode(self, mode):
        self.mode = mode

    def maintenance(self):
        self.water_level = 0
        self.coffee_level = 0
        print("Обслуживание завершено")


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
        self.health += amount

    def level_up(self):
        self.level += 1
        self.damage +=5

    def add_item(self, item):
        self.inventory.append(item)

    def equip_item(self, item, slot):
        self.equipped[slot] = item

    def show_inventory(self):
        return self.inventory
    
    def show_equipped(self):
        return self.equipped