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
    

"""
ТЕСТ КЛАССОВ
"""
print("ТЕСТИРОВАНИЕ КЛАССА BOOK")
book1 = Book("Война и мир", "Толстой")
book2 = Book("Преступление и наказание", "Достоевский")

print(book1.get_info())
print(book2.get_info())

print("\nСтатус доступности книги:")
print(f"Книга доступна: {book1.is_available()}")
book1.set_available(False)
print(f"После изменения: {book1.is_available()}")

print("\nОценки книг:")
book1.add_rating(5)
book1.add_rating(4)
book1.add_rating(3)
book2.add_rating(5)
book2.add_rating(5)

print(f"Средний рейтинг книги 1: {book1.get_average_rating()}")
print(f"Средний рейтинг книги 2: {book2.get_average_rating()}")

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА STUDENT")
student1 = Student("Иван Петров")
student2 = Student("Мария Сидорова", [4, 5, 3])

student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(5)
student2.add_grade(4)

print(f"Средний балл {student1.name}: {student1.get_average()}")
print(f"Средний балл {student2.name}: {student2.get_average()}")

print("\nПосещаемость:")
student1.mark_attendance("2024-01-01", True)
student1.mark_attendance("2024-01-02", True)
student1.mark_attendance("2024-01-03", False)
student1.mark_attendance("2024-01-04", True)

student2.mark_attendance("2024-01-01", True)
student2.mark_attendance("2024-01-02", False)

print(f"Процент посещаемости {student1.name}: {student1.get_attendance_rate():.1%}")
print(f"Процент посещаемости {student2.name}: {student2.get_attendance_rate():.1%}")

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА RECTANGLE")
rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)
rect3 = Rectangle(2, 10)

print(f"Площадь прямоугольника 1: {rect1.calculate_area()}")
print(f"Периметр прямоугольника 1: {rect1.calculate_perimeter()}")

print(f"\nСравнение прямоугольников:")
print(f"rect1 > rect2: {rect1.is_larger(rect2)}")
print(f"rect1 = rect3: {rect1.is_equal(rect3)}")

print("\nИзменение размеров:")
rect1.resize(8, 2)
print(f"После изменения - площадь: {rect1.calculate_area()}")

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА BANKACCOUNT")
account1 = BankAccount("Иван Иванов", 1000)
account2 = BankAccount("Петр Петров")

print(f"Баланс {account1.owner}: {account1.balance}")
print(f"Баланс {account2.owner}: {account2.balance}")

print("\nОперации:")
account1.deposit(500)
account1.withdraw(200)
account2.deposit(1000)
account2.withdraw(1500)  # Не должно сработать

print(f"\nБаланс после операций:")
print(f"{account1.owner}: {account1.balance}")
print(f"{account2.owner}: {account2.balance}")

print("\nНачисление процентов:")
account1.add_interest(5)
print(f"После начисления 5%: {account1.balance}")

print("\nИстория операций:")
account1.show_history()

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА DOG")
dog1 = Dog("Бобик", 3, "овчарка")
dog2 = Dog("Шарик", 1, "дворняжка")
dog3 = Dog("Рекс", 8, "ротвейлер")

print(f"Собака: {dog1.name}, Порода: {dog1.breed}, Возраст: {dog1.age}")
print(f"Возраст в человеческих годах: {dog1.human_age()}")

print("\nНавыки собак:")
dog1.add_skill("сидеть")
dog1.add_skill("лежать")
dog1.add_skill("голос")
dog2.add_skill("сидеть")

print(f"Навыки {dog1.name}: {dog1.show_skills()}")
print(f"Навыки {dog2.name}: {dog2.show_skills()}")

print("\nЖизненные этапы:")
print(f"{dog1.name}: {dog1.life_stage()}")
print(f"{dog2.name}: {dog2.life_stage()}")
print(f"{dog3.name}: {dog3.life_stage()}")

dog1.bark()

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА POINT2D")
point1 = Point2D(3, 4)
point2 = Point2D(0, 0)
point3 = Point2D(1, 1)

print(f"Координаты точки 1: {point1.get_coords()}")
print(f"Координаты точки 2: {point2.get_coords()}")

print(f"\nРасстояние от точки 1 до нуля: {point1.distance_to_zero()}")
print(f"Расстояние между точкой 1 и точкой 3: {point1.distance_to(point3)}")

print("\nПеремещение точки:")
point1.move(2, -1)
print(f"После перемещения: {point1.get_coords()}")

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА LAMP")
lamp1 = Lamp()
lamp2 = Lamp(True)

print("Статус ламп:")
lamp1.status()
lamp2.status()

print("\nНастройка лампы 1:")
lamp1.switch_on()
lamp1.set_brightness(75)
lamp1.set_color("синий")
lamp1.status()

print("\nСветовые эффекты:")
lamp1.effect_blink()
lamp2.effect_blink()

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА SOCIALPROFILE")
profile1 = SocialProfile("user123")
profile2 = SocialProfile("cool_girl")

print("Добавление постов:")
profile1.add_post("Мой первый пост!")
profile1.add_post("Сегодня отличный день!")
profile1.add_post("Изучаю Python")
profile2.add_post("Привет всем!")

print("\nПосты пользователя 1:")
profile1.show_posts()

print("\nЛайки и подписчики:")
profile1.like_post()
profile1.like_post()
profile1.like_post()
profile2.like_post()

profile1.add_follower("friend1")
profile1.add_follower("friend2")
profile1.add_follower("friend3")
profile2.add_follower("friend1")

print(f"Лайков у {profile1.username}: {profile1.get_likes_count()}")
print(f"Подписчиков у {profile1.username}: {profile1.get_followers_count()}")
print(f"Лайков у {profile2.username}: {profile2.get_likes_count()}")

print("\nАнализ активности:")
print(profile1.analyze_activity())
print(profile2.analyze_activity())

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА COFFEEMACHINE")
coffee_machine = CoffeeMachine()

print("Начальное состояние:")
print(f"Уровень воды: {coffee_machine.water_level}")
print(f"Уровень кофе: {coffee_machine.coffee_level}")

print("\nЗаполнение:")
coffee_machine.add_water(1000)
coffee_machine.add_coffee(200)
coffee_machine.set_mode("эспрессо")

print(f"После заполнения - вода: {coffee_machine.water_level}, кофе: {coffee_machine.coffee_level}")

print("\nПриготовление кофе:")
result1 = coffee_machine.make_coffee()
result2 = coffee_machine.make_coffee()
result3 = coffee_machine.make_coffee()  # Должно хватить
result4 = coffee_machine.make_coffee()  # Должно не хватить

print(f"Результаты: {result1}, {result2}, {result3}, {result4}")
print(f"Остаток - вода: {coffee_machine.water_level}, кофе: {coffee_machine.coffee_level}")

print("\nОбслуживание:")
coffee_machine.maintenance()
print(f"После обслуживания - вода: {coffee_machine.water_level}, кофе: {coffee_machine.coffee_level}")

print("\n")
print("ТЕСТИРОВАНИЕ КЛАССА GAMECHARACTER")
hero = GameCharacter("Артур", health=120, damage=15)
enemy = GameCharacter("Дракон", health=200, damage=20)

print(f"Персонаж: {hero.name}, Здоровье: {hero.health}, Урон: {hero.damage}, Уровень: {hero.level}")
print(f"Враг: {enemy.name}, Здоровье: {enemy.health}, Урон: {enemy.damage}")

print("\nИнвентарь:")
hero.add_item("меч")
hero.add_item("щит")
hero.add_item("зелье здоровья")
enemy.add_item("кости")

print(f"Инвентарь героя: {hero.show_inventory()}")
print(f"Инвентарь врага: {enemy.show_inventory()}")

print("\nЭкипировка:")
hero.equip_item("меч", "правая рука")
hero.equip_item("щит", "левая рука")
enemy.equip_item("кости", "пасть")

print(f"Экипировка героя: {hero.show_equipped()}")
print(f"Экипировка врага: {enemy.show_equipped()}")

print("\nБой:")
print(f"Здоровье врага до атаки: {enemy.health}")
hero.attack(enemy)
print(f"Здоровье врага после атаки: {enemy.health}")

print("\nЛечение и повышение уровня:")
hero.heal(30)
hero.level_up()
print(f"После лечения: {hero.health}")
print(f"После повышения уровня: урон={hero.damage}, уровень={hero.level}")

print("\n")
print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
