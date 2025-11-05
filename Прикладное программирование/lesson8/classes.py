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
import math
import time

class Book:
    def init(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.ratings = []

    def get_info(self):
        return f"Книга: '{self.title}'. Автор: {self.author}."

    def set_availability(self, status):
            #Статус доступных книг
        self.is_available = status
        status_text = "доступна" if status else "недоступна"
        print(f"Книга '{self.title}' теперь {status_text}.")

    def add_rating(self, rating):
            #Оценка книги
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            print(f"Для книги '{self.title}' добавлена оценка: {rating}.")
        else:
            print("Ошибка: Оценка должна быть в диапазоне от 1 до 5.")

    def get_average_rating(self):
            #Средняя оценка книги
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class Student:
    def init(self, name, grades=None):
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
            #Посещаемость
        self.attendance[date] = status
        print(f"Студент {self.name} на дату {date}: {status}.")

    def get_performance(self):
            #Успеваемость на основе средней оценки
        avg_grade = self.get_average()
        if avg_grade >= 4.5:
            return "Отлично"
        elif avg_grade >= 3.5:
            return "Хорошо"
        elif avg_grade >= 2.5:
            return "Удовлетворительно"
        else:
            return "Неудовлетворительно"

class Rectangle:
    def init(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def resize(self, new_length, new_width):
            #Размер прямоугольника
        self.length = new_length
        self.width = new_width
        print(f"Размеры прямоугольника изменены на {self.length}x{self.width}.")

    def eq(self, other):
            #Сравние двух прямоугольников по площади
        return self.calculate_area() == other.calculate_area()

    def lt(self, other):
            #Сравние двух прямоугольников по площади
        return self.calculate_area() < other.calculate_area()

    def gt(self, other):
            #Сравние двух прямоугольников по площади
        return self.calculate_area() > other.calculate_area()

class BankAccount:
    def init(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Пополнение: +{amount}")
            print(f"Счет пополнен на {amount}. Текущий баланс: {self.balance}")
        else:
            print("Сумма пополнения должна быть положительной.")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Снятие: -{amount}")
            print(f"Со счета снято {amount}. Текущий баланс: {self.balance}")
            return True
        else:
            print("Недостаточно средств или неверная сумма для снятия.")
            return False

    def get_history(self):
            #История операций
        return self.history

    def apply_interest(self, rate):
            #Проценты на баланс
        interest = self.balance * (rate / 100)
        self.deposit(interest)
        print(f"Начислены проценты в размере {interest} по ставке {rate}%.")

class Dog:
    def init(self, name, age, breed="неизвестна"):
        self.name = name
        self.age = age
        self.breed = breed
        self.skills = []

    def bark(self):
        print("Гав!")

    def human_age(self):
        return self.age * 7

    def add_skill(self, skill):
            #Новый навык собаки
        self.skills.append(skill)
        print(f"Собака {self.name} научилась новому навыку: {skill}.")

    def get_life_stage(self):
            #Жизненный этап собаки
        if self.age < 1:
            return "Щенок"
        elif self.age < 7:
            return "Взрослая собака"
        else:
            return "Пожилая собака"

class Point2D:
    def init(self, x, y):
        self.x = x
        self.y = y

    def distance_to_zero(self):
        return (self.x2 + self.y2)**0.5

    def distance_to(self, other_point):
            #Вычисление расстояние до второй точки
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

    def set_coordinates(self, x, y):
            #Координаты для точки
        self.x = x
        self.y = y
        print(f"Координаты точки изменены на ({self.x}, {self.y}).")

class Lamp:
    def init(self, is_on=False):
        self.is_on = is_on
        self.brightness = 100 
        self.color = "белый"

    def switch_on(self):
        self.is_on = True

    def switch_off(self):
        self.is_on = False

    def set_brightness(self, level):
            #Яркость светильника
        if 0 <= level <= 100:
            self.brightness = level
            print(f"Яркость установлена на {self.brightness}%.")
        else:
            print("Ошибка: Уровень яркости должен быть от 0 до 100.")

    def set_color(self, color):
            #Цвет свечения
        self.color = color
        print(f"Цвет изменен на {self.color}.")

    def status(self):
        if self.is_on:
            return f"Светильник включен. Яркость: {self.brightness}%, Цвет: {self.color}."
        else:
            return "Светильник выключен."

    def blink_effect(self, times=3, delay=0.5):
            #Эффект мигания
        print("Активирован эффект мигания...")
        initial_state = self.is_on
        for _ in range(times):
            self.switch_off()
            print(self.status())
            time.sleep(delay)
            self.switch_on()
            print(self.status())
            time.sleep(delay)
        self.is_on = initial_state 
        print("Эффект мигания завершен.")

class SocialProfile:
    def init(self, username, posts=None):
        self.username = username
        self.posts = posts if posts is not None else []
        self.followers = 0
        self.likes = 0

    def add_post(self, text):
        self.posts.append({"text": text, "likes": 0})

    def show_posts(self):
        for i, post in enumerate(self.posts):
            print(f"{i}: {post['text']} (Лайки: {post['likes']})")

    def add_follower(self):
            #Увеличивает количество подписчиков
        self.followers += 1
        print(f"У {self.username} теперь {self.followers} подписчиков.")

    def like_post(self, post_index):
            #Лайк на пост
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]["likes"] += 1
            self.likes += 1
            print(f"Пост {post_index} получил лайк!")
        else:
            print("Ошибка: Такого поста не существует.")

def get_activity_analysis(self):
            #Активность профиля
        total_post_likes = sum(post['likes'] for post in self.posts)
        if self.followers == 0:
            engagement_rate = 0
        else:
            engagement_rate = (total_post_likes / self.followers) * 100 if self.followers > 0 else 0
        return {
            "posts_count": len(self.posts),
            "total_likes": total_post_likes,
            "followers_count": self.followers,
            "engagement_rate_per_follower": f"{engagement_rate:.2f}%"
        }

class CoffeeMachine:
    def init(self, water_level=1000, coffee_level=500):
        self.water_level = water_level  
        self.coffee_level = coffee_level 
        self.current_mode = "эспрессо"

    def add_water(self, amount):
        self.water_level += amount
        print(f"Добавлено {amount} мл воды. Текущий уровень: {self.water_level} мл.")

    def add_coffee(self, amount):
        self.coffee_level += amount
        print(f"Добавлено {amount} г кофе. Текущий уровень: {self.coffee_level} г.")

    def set_mode(self, mode):
        """Устанавливает режим приготовления ('эспрессо', 'капучино')."""
        self.current_mode = mode
        print(f"Режим изменен на '{self.current_mode}'.")

    def make_coffee(self):
        water_needed = 200 if self.current_mode == "капучино" else 100
        coffee_needed = 20 if self.current_mode == "капучино" else 15

        if self.water_level >= water_needed and self.coffee_level >= coffee_needed:
            self.water_level -= water_needed
            self.coffee_level -= coffee_needed
            print(f"Ваш {self.current_mode} готов!")
            return True
        else:
            print("Недостаточно ингредиентов для приготовления кофе.")
            self.check_service_needed()
            return False

    def check_service_needed(self):
        if self.water_level < 200:
            print("Требуется долить воды.")
        if self.coffee_level < 20:
            print("Требуется досыпать кофе.")


class GameCharacter:
    def init(self, name, health=100, damage=10, level=1):
        self.name = name
        self.health = health
        self.damage = damage
        self.level = level
        self.inventory = []
        self.equipment = {} 

    def attack(self, other_character):
        print(f"{self.name} атакует {other_character.name} и наносит {self.damage} урона.")
        other_character.health -= self.damage
        if other_character.health <= 0:
            print(f"{other_character.name} побежден!")

    def heal(self, amount):
            #Лечит персонажа
        self.health += amount
        print(f"{self.name} восстановил {amount} здоровья. Текущее здоровье: {self.health}.")

    def level_up(self):
            #Повышает уровень персонажа
        self.level += 1
        self.damage += 5 
        self.health += 20 
        print(f"{self.name} достиг {self.level} уровня!")

    def add_to_inventory(self, item):
            #Предмет в инвентарь
        self.inventory.append(item)
        print(f"В инвентарь {self.name} добавлен предмет: {item}.")

    def equip_item(self, item_name, item_type):
        if item_name in self.inventory:
            self.equipment[item_type] = item_name
            self.inventory.remove(item_name)
            print(f"{self.name} экипировал '{item_name}' как {item_type}.")
        else:
            print(f"У {self.name} нет предмета '{item_name}' в инвентаре.")