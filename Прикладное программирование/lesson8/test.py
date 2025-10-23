from classes import *

# Book
book1 = Book("Война и мир", "Толстой")
book1.set_available(False)
print(book1.is_available())
book1.add_rating(5)
book1.add_rating(4)
print(book1.get_average_rating())

# Student
student1 = Student("Иван")
student1.add_grade(5)
student1.add_grade(4)
student1.mark_attendance("2024-01-01", True)
student1.mark_attendance("2024-01-02", False)
print(student1.get_average())
print(student1.get_attendance_rate())

# Rectangle
rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)
print(rect1.is_larger(rect2))
rect1.resize(10, 2)
print(rect1.calculate_area())

# BankAccount
account = BankAccount("Петр")
account.deposit(1000)
account.withdraw(300)
account.add_interest(10)
account.show_history()
print(account.balance)

# Dog
dog = Dog("Бобик", 3, "овчарка")
dog.add_skill("сидеть")
dog.add_skill("лежать")
print(dog.show_skills())
print(dog.life_stage())

# Point2D
point1 = Point2D(3, 4)
point2 = Point2D(0, 0)
print(point1.distance_to(point2))
point1.move(1, 1)
print(point1.get_coords())

# Lamp
lamp = Lamp()
lamp.switch_on()
lamp.set_color("красный")
lamp.set_brightness(80)
lamp.effect_blink()
lamp.status()

# SocialProfile
profile = SocialProfile("user123")
profile.add_post("Мой первый пост")
profile.add_post("Отличная погода!")
profile.like_post()
profile.like_post()
profile.add_follower("friend1")
print(profile.get_likes_count())
print(profile.analyze_activity())

# CoffeeMachine
coffee_machine = CoffeeMachine()
coffee_machine.add_water(500)
coffee_machine.add_coffee(100)
coffee_machine.set_mode("эспрессо")
coffee_machine.make_coffee()
coffee_machine.maintenance()

# GameCharacter
hero = GameCharacter("Герой")
enemy = GameCharacter("Враг")
hero.add_item("меч")
hero.add_item("щит")
hero.equip_item("меч", "правая рука")
hero.level_up()
hero.attack(enemy)
print(hero.show_inventory())
print(hero.show_equipped())
print(enemy.health)