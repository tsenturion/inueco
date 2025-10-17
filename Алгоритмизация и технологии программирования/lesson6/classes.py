# 1
class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."

# 2
class Student:
    def __init__(self, name, grades = None) -> None:
        self.name = name
        self.grades = grades if grades is not None else []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

# 3
class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.width * self.length

    def calculate_perimeter(self):
        return 2 * (self.width + self.length)

# 4
class BankAccount:
    def __init__(self, owner, balance = 0) -> None:
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount

# 5
class Dog:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print("Гав!")

    def human_age(self):
        return self.age * 7

# 6
class Point2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# 7
class Lamp:
    def __init__(self, is_on = False) -> None:
        self.is_on = is_on

    def switch_on(self):
        self.is_on = True

    def switch_off(self):
        self.is_on = False

    def status(self):
        print("Светильник включен" if self.is_on else "Светильник выключен")

# 8
class SocialProfile:
    def __init__(self, username, posts = None) -> None:
        self.username = username
        self.posts = posts if posts is not None else []

    def add_post(self, text):
        self.posts.append(text)
    
    def show_posts(self):
        for post in self.posts:
            print(post)

# 9
class CoffeeMachine:
    def __init__(self, water_level = 0) -> None:
        self.water_level = water_level

    def add_water(self, amount):
        self.water_level += amount

    def make_coffee(self):
        if self.water_level < 200:
            print("Недостаточно воды")
            return False

        self.water_level -= 200
        return True

# 10
class GameCharacter:
    def __init__(self, name, health = 100, damage = 10) -> None:
        self.name = name
        self.health = health
        self.damage = damage
    
    def attack(self, other_character):
        other_character.health -= self.damage