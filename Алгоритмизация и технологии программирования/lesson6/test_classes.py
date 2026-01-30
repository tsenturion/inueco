import pytest
import math
from io import StringIO
import sys
from classes import Book, Student, Rectangle, BankAccount, Dog, Point2D, Lamp, SocialProfile, CoffeeMachine, GameCharacter


class TestBook:
    def test_book_initialization(self):
        book = Book("Война и мир", "Лев Толстой")
        assert book.title == "Война и мир"
        assert book.author == "Лев Толстой"
    
    def test_get_info(self):
        book = Book("1984", "Джордж Оруэлл")
        expected = "Книга: '1984'. Автор: Джордж Оруэлл."
        assert book.get_info() == expected
    
    def test_get_info_with_unicode(self):
        book = Book("Мастер и Маргарита", "Михаил Булгаков")
        info = book.get_info()
        assert "Мастер и Маргарита" in info
        assert "Михаил Булгаков" in info


class TestStudent:
    def test_student_initialization(self):
        student = Student("Иван")
        assert student.name == "Иван"
        assert student.grades == []
    
    def test_student_with_initial_grades(self):
        student = Student("Мария", [5, 4, 5])
        assert student.grades == [5, 4, 5]
    
    def test_add_grade(self):
        student = Student("Петр")
        student.add_grade(5)
        student.add_grade(4)
        assert student.grades == [5, 4]
    
    def test_get_average_empty(self):
        student = Student("Анна")
        assert student.get_average() == 0
    
    def test_get_average(self):
        student = Student("Сергей")
        student.add_grade(5)
        student.add_grade(4)
        student.add_grade(3)
        assert student.get_average() == 4.0
    
    def test_get_average_precise(self):
        student = Student("Ольга", [5, 4, 4])
        assert abs(student.get_average() - 4.333333) < 0.001


class TestRectangle:
    def test_rectangle_initialization(self):
        rect = Rectangle(5, 3)
        assert rect.length == 5
        assert rect.width == 3
    
    def test_calculate_area(self):
        rect = Rectangle(10, 5)
        assert rect.calculate_area() == 50
    
    def test_calculate_perimeter(self):
        rect = Rectangle(10, 5)
        assert rect.calculate_perimeter() == 30
    
    def test_square(self):
        square = Rectangle(4, 4)
        assert square.calculate_area() == 16
        assert square.calculate_perimeter() == 16
    
    def test_float_dimensions(self):
        rect = Rectangle(3.5, 2.5)
        assert rect.calculate_area() == 8.75
        assert rect.calculate_perimeter() == 12.0


class TestBankAccount:
    def test_account_initialization(self):
        account = BankAccount("Иван Петров")
        assert account.owner == "Иван Петров"
        assert account.balance == 0
    
    def test_account_with_initial_balance(self):
        account = BankAccount("Мария Сидорова", 1000)
        assert account.balance == 1000
    
    def test_deposit(self):
        account = BankAccount("Петр Иванов")
        account.deposit(500)
        assert account.balance == 500
        account.deposit(300)
        assert account.balance == 800
    
    def test_withdraw_success(self):
        account = BankAccount("Анна Смирнова", 1000)
        result = account.withdraw(500)
        assert result is not False
        assert account.balance == 500
    
    def test_withdraw_failure(self):
        account = BankAccount("Сергей Козлов", 100)
        result = account.withdraw(200)
        assert result == False
        assert account.balance == 100
    
    def test_withdraw_exact_amount(self):
        account = BankAccount("Ольга Попова", 500)
        account.withdraw(500)
        assert account.balance == 0


class TestDog:
    def test_dog_initialization(self):
        dog = Dog("Шарик", 5)
        assert dog.name == "Шарик"
        assert dog.age == 5
    
    def test_bark(self, capsys):
        dog = Dog("Бобик", 3)
        dog.bark()
        captured = capsys.readouterr()
        assert "Гав!" in captured.out
    
    def test_human_age(self):
        dog = Dog("Рекс", 2)
        assert dog.human_age() == 14
    
    def test_human_age_older_dog(self):
        dog = Dog("Тузик", 10)
        assert dog.human_age() == 70


class TestPoint2D:
    def test_point_initialization(self):
        point = Point2D(3, 4)
        assert point.x == 3
        assert point.y == 4
    
    def test_distance_to_zero(self):
        point = Point2D(3, 4)
        assert point.distance_to_zero() == 5.0
    
    def test_distance_to_zero_origin(self):
        point = Point2D(0, 0)
        assert point.distance_to_zero() == 0.0
    
    def test_distance_to_zero_negative(self):
        point = Point2D(-3, -4)
        assert point.distance_to_zero() == 5.0
    
    def test_distance_to_zero_float(self):
        point = Point2D(1.0, 1.0)
        expected = math.sqrt(2)
        assert abs(point.distance_to_zero() - expected) < 0.0001


class TestLamp:
    def test_lamp_initialization_default(self):
        lamp = Lamp()
        assert lamp.is_on == False
    
    def test_lamp_initialization_on(self):
        lamp = Lamp(True)
        assert lamp.is_on == True
    
    def test_switch_on(self):
        lamp = Lamp()
        lamp.switch_on()
        assert lamp.is_on == True
    
    def test_switch_off(self):
        lamp = Lamp(True)
        lamp.switch_off()
        assert lamp.is_on == False
    
    def test_status_on(self, capsys):
        lamp = Lamp(True)
        lamp.status()
        captured = capsys.readouterr()
        assert "Светильник включен" in captured.out
    
    def test_status_off(self, capsys):
        lamp = Lamp()
        lamp.status()
        captured = capsys.readouterr()
        assert "Светильник выключен" in captured.out


class TestSocialProfile:
    def test_profile_initialization(self):
        profile = SocialProfile("user123")
        assert profile.username == "user123"
        assert profile.posts == []
    
    def test_profile_with_initial_posts(self):
        profile = SocialProfile("user456", ["Первый пост"])
        assert len(profile.posts) == 1
    
    def test_add_post(self):
        profile = SocialProfile("user789")
        profile.add_post("Мой первый пост")
        profile.add_post("Второй пост")
        assert len(profile.posts) == 2
        assert profile.posts[0] == "Мой первый пост"
    
    def test_show_posts(self, capsys):
        profile = SocialProfile("user000")
        profile.add_post("Пост 1")
        profile.add_post("Пост 2")
        profile.show_posts()
        captured = capsys.readouterr()
        assert "Пост 1" in captured.out
        assert "Пост 2" in captured.out
    
    def test_show_posts_empty(self, capsys):
        profile = SocialProfile("user111")
        profile.show_posts()
        captured = capsys.readouterr()
        assert captured.out == ""


class TestCoffeeMachine:
    def test_machine_initialization(self):
        machine = CoffeeMachine()
        assert machine.water_level == 0
    
    def test_machine_with_initial_water(self):
        machine = CoffeeMachine(500)
        assert machine.water_level == 500
    
    def test_add_water(self):
        machine = CoffeeMachine()
        machine.add_water(300)
        assert machine.water_level == 300
        machine.add_water(200)
        assert machine.water_level == 500
    
    def test_make_coffee_success(self):
        machine = CoffeeMachine(300)
        result = machine.make_coffee()
        assert result is not False
        assert machine.water_level == 100
    
    def test_make_coffee_insufficient_water(self, capsys):
        machine = CoffeeMachine(100)
        result = machine.make_coffee()
        captured = capsys.readouterr()
        assert result == False
        assert machine.water_level == 100
        assert "Недостаточно воды" in captured.out or "воды" in captured.out.lower()
    
    def test_make_coffee_exact_amount(self):
        machine = CoffeeMachine(200)
        machine.make_coffee()
        assert machine.water_level == 0


class TestGameCharacter:
    def test_character_initialization_default(self):
        char = GameCharacter("Герой")
        assert char.name == "Герой"
        assert char.health == 100
        assert char.damage == 10
    
    def test_character_initialization_custom(self):
        char = GameCharacter("Воин", 150, 20)
        assert char.health == 150
        assert char.damage == 20
    
    def test_attack(self):
        hero = GameCharacter("Герой", 100, 15)
        enemy = GameCharacter("Враг", 100, 10)
        hero.attack(enemy)
        assert enemy.health == 85
    
    def test_multiple_attacks(self):
        hero = GameCharacter("Герой", 100, 20)
        enemy = GameCharacter("Враг", 100, 10)
        hero.attack(enemy)
        hero.attack(enemy)
        assert enemy.health == 60
    
    def test_attack_reduces_to_negative(self):
        hero = GameCharacter("Герой", 100, 150)
        enemy = GameCharacter("Враг", 100, 10)
        hero.attack(enemy)
        assert enemy.health == -50


if __name__ == "__main__":
    pytest.main([__file__, "-v"])