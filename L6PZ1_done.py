# 1. Книга
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."


# 2. Студент
class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


# 3. Прямоугольник
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


# 4. Банковский счет
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Недостаточно средств на счете")


# 5. Собака
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Гав!")
    
    def human_age(self):
        return self.age * 7


# 6. Точка в 2D-пространстве
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5


# 7. Простой Светильник
class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on
    
    def switch_on(self):
        self.is_on = True
    
    def switch_off(self):
        self.is_on = False
    
    def status(self):
        if self.is_on:
            print("Светильник включен")
        else:
            print("Светильник выключен")


# 8. Профиль в социальной сети
class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
    
    def add_post(self, text):
        self.posts.append(text)
    
    def show_posts(self):
        for post in self.posts:
            print(post)


# 9. Кофе-машина (упрощенная)
class CoffeeMachine:
    def __init__(self, water_level=0):
        self.water_level = water_level
    
    def add_water(self, amount):
        self.water_level += amount
    
    def make_coffee(self):
        if self.water_level >= 200:
            self.water_level -= 200
            print("Кофе готов!")
        else:
            print("Ошибка: недостаточно воды для приготовления кофе")


# 10. Игровой персонаж
class GameCharacter:
    def __init__(self, name, health=100, damage=10):
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self, other_character):
        other_character.health -= self.damage