class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.ratings = []
    
    def get_info(self):
        status = "доступна" if self.is_available else "недоступна"
        avg = sum(self.ratings)/len(self.ratings) if self.ratings else 0
        return f"'{self.title}', {self.author}. Статус: {status}, Рейтинг: {avg:.1f}"
    
    def borrow(self): 
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self): 
        self.is_available = True
    
    def rate(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.attendance = {}
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def get_average(self):
        return sum(self.grades)/len(self.grades) if self.grades else 0
    
    def mark_attendance(self, date):
        self.attendance[date] = True
    
    def get_attendance_rate(self):
        present = sum(self.attendance.values())
        return (present/len(self.attendance))*100 if self.attendance else 0
    
    def get_performance(self):
        avg = self.get_average()
        attendance = self.get_attendance_rate()
        if avg >= 4.5 and attendance >= 90: return "Отличная"
        elif avg >= 3.5 and attendance >= 80: return "Хорошая"
        elif avg >= 3.0 and attendance >= 70: return "Удовлетворительная"
        return "Неудовлетворительная"


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def resize(self, length=None, width=None):
        if length: self.length = length
        if width: self.width = width
    
    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"+{amount}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"-{amount}")
            return True
        return False
    
    def add_interest(self, rate=0.02):
        interest = self.balance * rate
        self.balance += interest
        self.history.append(f"+{interest:.2f}%")
    
    def get_history(self):
        return self.history


class Dog:
    def __init__(self, name, age, breed="неизвестна"):
        self.name = name
        self.age = age
        self.breed = breed
        self.skills = []
    
    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)
    
    def get_stage(self):
        if self.age <= 1: return "Щенок"
        elif self.age <= 3: return "Молодая"
        elif self.age <= 8: return "Взрослая"
        return "Пожилая"


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def __str__(self):
        return f"({self.x}, {self.y})"


class Lamp:
    def __init__(self):
        self.is_on = False
        self.brightness = 50
        self.color = "белый"
    
    def toggle(self):
        self.is_on = not self.is_on
    
    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
    
    def set_color(self, color):
        self.color = color
    
    def get_status(self):
        if self.is_on:
            return f"Включен, {self.brightness}%, {self.color}"
        return "Выключен"


class SocialProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.likes = 0
        self.followers = set()
    
    def add_post(self, text):
        self.posts.append({"text": text, "likes": 0})
    
    def like_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts[index]['likes'] += 1
            self.likes += 1
    
    def add_follower(self, user):
        self.followers.add(user)
    
    def get_stats(self):
        engagement = (self.likes/len(self.posts)/len(self.followers)*100) if self.posts and self.followers else 0
        return {
            "posts": len(self.posts),
            "likes": self.likes,
            "followers": len(self.followers),
            "engagement": f"{engagement:.1f}%"
        }


class CoffeeMachine:
    def __init__(self):
        self.water = 0
        self.coffee = 0
        self.drinks_made = 0
    
    def add_water(self, amount):
        self.water += amount
    
    def add_coffee(self, amount):
        self.coffee += amount
    
    def make_coffee(self):
        if self.water >= 200 and self.coffee >= 20:
            self.water -= 200
            self.coffee -= 20
            self.drinks_made += 1
            return "Готово!"
        return "Недостаточно ресурсов"
    
    def needs_service(self):
        return self.drinks_made >= 10
    
    def service(self):
        if self.needs_service():
            self.drinks_made = 0
            return "Обслужено"
        return "Не требуется"


class GameCharacter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.max_health = 100
        self.damage = 10
        self.level = 1
        self.exp = 0
        self.inventory = []
        self.equipped = {}
    
    def attack(self, target):
        target.health -= self.damage
    
    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
    
    def add_exp(self, amount):
        self.exp += amount
        if self.exp >= self.level * 100:
            self.level += 1
            self.max_health += 20
            self.health = self.max_health
            self.damage += 5
            self.exp = 0
            return f"Уровень {self.level}!"
    
    def equip(self, item, slot):
        if item in self.inventory:
            self.equipped[slot] = item
            self.inventory.remove(item)
            if "броня" in item: self.max_health += 10
            elif "оружие" in item: self.damage += 5


if __name__ == "__main__":
    book = Book("1984", "Оруэлл")
    book.rate(5)
    book.rate(4)
    print(book.get_info())
    
    student = Student("Иван")
    student.add_grade(5)
    student.mark_attendance("2024-01-01")
    print(student.get_performance())
    
    dog = Dog("Бобик", 2)
    dog.add_skill("сидеть")
    print(dog.get_stage())
    
    lamp = Lamp()
    lamp.toggle()
    lamp.set_brightness(75)
    print(lamp.get_status())
    
    profile = SocialProfile("user")
    profile.add_post("Привет!")
    profile.like_post(0)
    print(profile.get_stats())
    
    hero = GameCharacter("Воин")
    hero.add_exp(150)
    print(hero.level)