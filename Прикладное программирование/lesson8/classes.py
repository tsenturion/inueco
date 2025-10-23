"""
1. Класс Book
[+] Добавьте методы для работы с статусом доступности книги
[+] Реализуйте возможность оценивать книгу
"""
class Book:
    def __init__(self, title, author, available=False):
        self.title = title
        self.author = author
        self.available = available
        self.reviews = []
    
    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."

    # Доступность книги
    def set_availability(self, available: bool):
        self.available = available

    # Оценка
    def add_review(self, review: int):
        if review < 1 or review > 5:
            print("Оценка должна быть от 1 до 5")
            return False
        self.reviews.append(review)

    def get_average_rating(self):
        if not self.reviews:
            return 0
        return sum(self.reviews) / len(self.reviews)

"""
2. Класс Student
[+] Добавьте методы для работы с посещаемостью
[+] Реализуйте функционал для определения успеваемости
"""
class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []
        self.visits = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    # Посещаемость
    def check_visit(self, date, subject):
        self.visits.append((date, subject))

    def list_visits(self):
        print(f"Посещения студента:")
        for visit in self.visits:
            print(f"Дата: {visit[0]}, Предмет: {visit[1]}")
        return True

    # Успеваемость
    def is_passing(self):
        average = self.get_average()
        return average >= 2.75

"""
3. Класс Rectangle
[+] Добавьте методы для изменения размеров
[+] Реализуйте функционал для сравнения прямоугольников
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
    # Изменение размеров
    def resize(self, new_length, new_width):
        self.length = new_length
        self.width = new_width

    # Сравнение прямоугольников
    def is_equal(self, other_rectangle: 'Rectangle'):
        return self.length == other_rectangle.length and self.width == other_rectangle.width

"""
4. Класс BankAccount
[+] Добавьте методы для работы с историей операций
[+] Реализуйте функционал для начисления процентов
"""
from datetime import datetime
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append({"type": "deposit", "amount": amount, "time": datetime.now()})
        # Начисление процентов
        interest = amount * 0.055
        self.balance += interest
        self.history.append({"type": "interest", "amount": interest, "time": datetime.now()})
    
    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.history.append({"type": "withdraw", "amount": amount, "time": datetime.now()})
        return True

    # История операций
    def _action_type(self, type):
        match type:
            case "deposit":
                return "Пополнение"
            case "withdraw":
                return "Снятие"
            case "interest":
                return "Начисление процентов за депозит"
            case _:
                return None

    def get_history(self):
        print("История операций:")
        for record in self.history:
            print(f"* {self._action_type(record['type'])} на сумму {record['amount']} RUB ({record['time'].strftime('%Y-%m-%d %H:%M:%S')})")

"""
5. Класс Dog
[+] Добавьте методы для работы с породой и навыками собаки
[+] Реализуйте функционал для определения жизненного этапа
"""
class Dog:
    def __init__(self, name, age, sort):
        self.name = name
        self.age = age
        self.sort = sort # Порода собаки
        self.loud_bark = False # Громкость лая
        self.love_level = 1 # Процент любви к хозяину
    
    # Изменение породы собаки
    def set_sort(self, sort: str):
        self.sort = sort

    # Изменение уровня любви к хозяину
    def set_love_level(self, level: int):
        if 1 <= level <= 5:
            self.love_level = level
        else:
            print("Уровень любви должен быть от 1 до 5")
    
    def bark(self):
        bark_sound = f"Гав{"-гав" * (self.love_level - 1)}!"
        print(bark_sound.capitalize() if self.loud_bark else bark_sound)
    
    # Навык громкого лая
    def set_loud(self, loud: bool):
        self.loud_bark = loud

    def human_age(self):
        return self.age * 7

    # Жизненный этап
    def get_life_stage(self):
        if self.age < 1:
            return "Щенок"
        elif 1 <= self.age < 7:
            return "Взрослая собака"
        else:
            return "Пожилая собака"

"""
6. Класс Point2D
[+] Добавьте методы для вычисления расстояний между точками
[+] Реализуйте функционал для работы с координатами
"""
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_zero(self):
        return (self.x**2 + self.y**2)**0.5

    # Вычисление расстояния между точками
    def distance_to_point(self, other_point: 'Point2D'):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
    
    # Работа с координатами
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

"""
7. Класс Lamp
[+] Добавьте методы для работы с яркостью и цветом
[+] Реализуйте функционал для создания световых эффектов
"""
class Lamp:
    def __init__(self, is_on=False):
        self.is_on = is_on
        self.brightness = 100
        self.color = "white"
        self.color_effect = None

    def switch_on(self):
        self.is_on = True
    
    def switch_off(self):
        self.is_on = False
    
    # Управление яркостью
    def set_brightness(self, brightness: int):
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            print("Яркость должна быть от 0 до 100")
    
    # Управление цветом
    def set_color(self, color: str):
        allowed = {'white', 'red', 'green', 'blue', 'purple'}
        if color not in allowed:
            print("Недопустимый цвет")
        else:
            self.color = color
            print("Цвет светильника изменен на", color)

    def add_effect(self, effect_type: str):
        match effect_type:
            case "blink":
                self.color_effect = "blink"
                print("Светильник мигает")
            case "fade":
                self.color_effect = "fade"
                print("Светильник плавно меняет яркость")
            case _:
                print("Неизвестный эффект")

    def status(self):
        if self.is_on:
            print("Светильник включен")
        else:
            print("Светильник выключен")

"""
8. Класс SocialProfile
[+] Добавьте методы для работы с лайками и подписчиками
[+] Реализуйте функционал для анализа активности
"""
class SocialProfile:
    def __init__(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.subs = []
        self.likes = []
    
    def add_post(self, text):
        self.posts.append(text)
    
    def show_posts(self):
        for post in self.posts:
            print(post)
    
    # Лайки и подписчики
    def like(self, post_index):
        if 0 <= post_index < len(self.posts):
            self.likes.append(post_index)
        else:
            print("Пост не найден")
    
    def remove_like(self, post_index):
        if post_index in self.likes:
            self.likes.remove(post_index)
        else:
            print("Лайк не найден")

    def add_subscriber(self, subscriber_name):
        self.subs.append(subscriber_name)
    
    def remove_subscriber(self, subscriber_name):
        if subscriber_name in self.subs:
            self.subs.remove(subscriber_name)
        else:
            print("Подписчик не найден")
    
    def analyze_activity(self):
        total_posts = len(self.posts)
        total_likes = len(self.likes)
        total_subs = len(self.subs)
        print(f"Пользователь {self.username} имеет {total_posts} постов, {total_likes} лайков и {total_subs} подписчиков.")

"""
9. Класс CoffeeMachine
[+] Добавьте методы для работы с уровнем кофе и режимами
[+] Реализуйте функционал для обслуживания аппарата
"""
class CoffeeMachine:
    def __init__(self, water_level=0):
        self.water_level = water_level
        self.sizes = { 'small': 100, 'medium': 200, 'large': 300 }
        self.strengths = { 'weak': 25, 'normal': 50, 'strong': 75 }
        self.modes = { 'espresso': 50, 'americano': 100, 'latte': 150 }

    def add_water(self, amount):
        self.water_level += amount
    
    def clean_water_barrel(self):
        self.water_level = 0
    
    def use_water(self, water_amount):
        if self.water_level <= water_amount:
            print("Недостаточно воды")
            return False
        else:
            self.water_level -= water_amount
            return True
    
    def make_coffee(self, size, strength, mode):
        water_need_total = self.sizes[size] + self.strengths[strength] + self.modes[mode]
        is_done = self.use_water(water_need_total)
        if is_done:
            print(f"Приготовлен кофе: {mode}, размер: {size}, крепость: {strength}")

    # Сервисное обслуживание
    def service(self):
        print("Сливаем старую воду...")
        self.clean_water_barrel()
        print("Набираем чистую воду...")
        self.add_water(1000)
        print("Кофемашина обслужена и готова к использованию")


"""
10. Класс GameCharacter
[+] Добавьте методы для лечения и повышения уровня
[+] Реализуйте функционал для инвентаря и экипировки
"""
class GameCharacter:
    def __init__(self, name, health=100, max_health=100, damage=10):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.damage = damage
        self.inventory = []
        self.item_in_hand = None
    
    # Лечение
    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    # Повышение уровня
    def level_up(self):
        self.damage += 5
        self.max_health += 20

    # Инвентарь и экипировка
    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        if item in self.inventory and self.item_in_hand != item:
            self.inventory.remove(item)
        else:
            print("Предмет не найден в инвентаре или прямо сейчас используется")

    def equip_item(self, item):
        if item is None:
            self.item_in_hand = None
            print("Экипировка снята.")
            return

        if item in self.inventory:
            self.item_in_hand = item
            print(f"Предмет '{item}' экипирован.")
        else:
            print("Предмет не найден в инвентаре")

    def attack(self, other_character):
        other_character.health -= self.damage