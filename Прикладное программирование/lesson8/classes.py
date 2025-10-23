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
    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False
    def return_book(self):
        self.available = True
    def is_available(self):
        return self.available
    def rate(self, value):
        if value < 0 or value > 5:
            return False
        self.ratings.append(value)
        return True
    def average_rating(self):
        if len(self.ratings) == 0:
            return 0
        s = 0
        for r in self.ratings:
            s = s + r
        return s / len(self.ratings)


class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
        self.attendance = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    def mark_attendance(self, present=True):
        if present:
            self.attendance.append('P')
        else:
            self.attendance.append('A')
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    def attendance_rate(self):
        if len(self.attendance) == 0:
            return 0
        present = 0
        for a in self.attendance:
            if a == 'P':
                present = present + 1
        return present / len(self.attendance)
    def is_passing(self):
        avg = self.get_average()
        att = self.attendance_rate()
        if avg >= 3 and att >= 0.6:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def set_size(self, length, width):
        self.length = length
        self.width = width
    def scale(self, factor):
        self.length = self.length * factor
        self.width = self.width * factor
    def area(self):
        return self.calculate_area()
    def compare_area(self, other):
        a1 = self.area()
        a2 = other.area()
        if a1 > a2:
            return 1
        if a1 < a2:
            return -1
        return 0


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    
    def deposit(self, amount):
        #Так будет лучше, ну не знаю
        self.balance = self.balance + amount
        self.history.append(("deposit", amount))
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.history.append(("withdraw", amount))
        return True
    def get_history(self):
        h = []
        for item in self.history:
            h.append(item)
        return h

    def accrue_interest(self, rate):
        if rate <= 0:
            return False
        change = self.balance * rate
        self.balance = self.balance + change
        self.history.append(("interest", change))
        return True


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.breed = ''
        self.skills = []
    
    def bark(self):
        print("Гав!")
    
    def human_age(self):
        return self.age * 7
    def set_breed(self, breed):
        self.breed = breed
    def add_skill(self, skill):
        found = False
        for s in self.skills:
            if s == skill:
                found = True
        if not found:
            self.skills.append(skill)

    def has_skill(self, skill):
        for s in self.skills:
            if s == skill:
                return True
        return False
    def life_stage(self):
        if self.age < 2:
            return 'puppy'
        elif self.age < 8:
            return 'adult'
        else:
            return 'senior'

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5
    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx*dx + dy*dy)**0.5
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy


class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on
        self.brightness = 100
        self.color = 'white'
    # яркость в процентах (0-100)
    def switch_on(self):
        self.is_on = True
    def switch_off(self):
        self.is_on = False
    def set_brightness(self, value):
        v = int(value)
        if v < 0:
            v = 0
        if v > 100:
            v = 100
        self.brightness = v

    def set_color(self, color):
        self.color = color
    def effect(self, name):
        return "Эффект " + name + " (on=" + str(self.is_on) + ", b=" + str(self.brightness) + ", c=" + self.color + ")"


class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.likes = 0
        self.followers = 0
    
    def add_post(self, text):
        self.posts.append(text)
    
    def show_posts(self):
        for post in self.posts:
            print(post)
    def add_like(self, n=1):
        self.likes = self.likes + n
    def add_follower(self, n=1):
        self.followers = self.followers + n
    def engagement(self):
        if len(self.posts) == 0:
            return 0
        return self.likes / len(self.posts)


class CoffeeMachine:
    def __init__(self, water_level=0):
        self.water_level = water_level
        self.coffee_level = 0
        self.service_log = []
    
    def add_water(self, amount):
        self.water_level += amount
    
    def make_coffee(self):
        return self.make_by_mode('default')
    def make_by_mode(self, mode):
        need = 200
        if mode == 'espresso':
            need = 50
        elif mode == 'americano':
            need = 150
        if self.water_level >= need:
            self.water_level = self.water_level - need
            self.coffee_level = self.coffee_level + 1
            self.service_log.append(('make', mode, need))
            return True
        else:
            print('Недостаточно воды')
            return False
    def service(self, note=''):
        self.service_log.append(('service', note))
    def get_service_log(self):
        log = []
        for x in self.service_log:
            log.append(x)
        return log


class GameCharacter:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = 1
        self.inventory = []
        self.equipped = []
    
    def attack(self, other_character):
        other_character.health -= self.damage
    def heal(self, amount):
        self.health = self.health + amount
    def level_up(self):
        self.level = self.level + 1
        self.health = self.health + 10
        self.damage = self.damage + 2
    def add_item(self, item):
        self.inventory.append(item)
    def equip(self, item):
        found = False
        for it in self.inventory:
            if it == item:
                found = True
        if found:
            already = False
            for e in self.equipped:
                if e == item:
                    already = True
            if not already:
                self.equipped.append(item)