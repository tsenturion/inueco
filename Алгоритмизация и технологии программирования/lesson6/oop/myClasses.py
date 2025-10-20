"""
экземпляр класса - объект построенный по шаблону классу
атрибуты (свойства/поля/переменные) - данные в классе
    атрибуты класса - общие для всех объектов
    атрибуты экземпляра класса - принадлежат конкретному объекту
методы - функции в классе
    обычные - say_hello - метод экземпляра класса
    классовые - @classmethod - получают cls первым аргументов, сам класс, а не объект
    статические @staticmethod - не получает ни self ни cls, просто функции внутри класса
магические методы () - переопределяют стандартное поведение
наследование
    super() - функция, вызывать методы родителя
    mro - method resolution order - порядок разрешения методов
    isinstance() - проверяет, является ли объект экземпляром класса или его потомка
    issubclass() - проверяет, является ли один класс подклассом другого
    object - корневой класс

mixins - миксы - небольшие классы, добавляющие одну конкретную функцию
абстрактный класс - шаблон - базовый класс - интерфейс (в питоне интерфейсом
является абстрактный класс без реализации), нельзя создать экземпляр, содержит абстрактные методы

    абстрактные методы - методы без реализации @abstactmethod
pass - подразумевает что далее что-то может быть добавлено
... - не подразумевает что далее что-то может быть добавлено
композиция - один класс содержит экземпляр другого, а не наследует его

инкапсуляция
    _ protected
    __ private
    name mangling - переименование

полиформизм - один и тот же метод может делать разное в зависимости от объекта


"""
import math


class MyClass:
    pass

#класс/шаблон
class Person:
    #атрибуты класса
    isHuman = True

    def __init__(self, name, age, high=None):
        #атрибуты экземпляра класса
        self.name = name
        self.age = age
        self.high = high

    def say_hello(self):
        print(f"привет я {self.name} мне {self.age}")

    def birthDay(self):
        self.age += 1

    #плохо
    @staticmethod
    def unHuman():
        Person.isHuman = False

    @classmethod
    def toHuman(cls):
        cls.isHuman = True

#p1 - экземпляр класс
p1 = Person("иван", 20)
#атрибуты (свойства/поля/переменные) - данные в классе
"""
p1
name = "иван"
age = 20
"""

p1.say_hello()
print(p1.age)
p1.birthDay()
print(p1.age)
p1.age = 10
print(p1.age)

print(p1.high)
p1.high = 200
print(p1.high)


print(Person.isHuman)
Person.unHuman()
print(Person.isHuman)

#наследование

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def move(self):
        print(f"{self.name} двигается")

class Dog(Animal):
    def __init__(self, name: str, age: int):
        self.age = age
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} гав")

class Cat(Animal):
    def __init__(self, name: str, age: int):
        self.age = age
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} мяу")

animals = [Dog('1', 1), Cat('1', 1)]
for animal in animals:
    animal.make_sound()
class BlackDog(Dog):
    def __init__(self, name, age, color='black'):
        self.color = color
        super().__init__(name, age)

blackDog = BlackDog('dog', 1)
print(blackDog.color)

class Flyer:
    def action(self):
        print('летит')

class Swimmer:
    def action(self):
        print('плывет')

class Duck(Flyer, Swimmer):
    def action(self):
        print('утра начинает действие')
        super().action()
        
d = Duck()
d.action()

#mro
print()
print(Duck.__mro__)
print()

a = Duck.__mro__
for i in a:
    print(i.__name__)


class A:
    def do(self):
        print("A")

class B:
    def do(self):
        print("B")

class C(A):
    def do(self):
        print("C")

class D(B, C):
    pass

d = D()
d.do()

print(D.__mro__)
"""
isinstance() - проверяет, является ли объект экземпляром класса или его потомка
issubclass() - проверяет, является ли один класс подклассом другого"""
"""print(isinstance(d, D))
print(isinstance(d, B))
print(isinstance(d, C))
print(isinstance(d, A))
print(isinstance(d, object))
print(d is D)
print(d is A)
print(d is object)
print(D is D)
print(D is A)"""

"""print(issubclass(D, B))
print(issubclass(D, A))
print(issubclass(B, C))
print(issubclass(D, object))"""
#mixins - миксы - небольшие классы, добавляющие одну конкретную функцию
class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Service(LoggerMixin, object):
    def process(self):
        self.log("обработка данных начата")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

print(bool(Shape.__abstractmethods__))  # проверка на абстрактность

"""
True

False:
""
''
[]
{}
frozenset()
set()
None
0
0.0

if []:
    print(1)
else:
    print(2)

"""

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self) -> float | int:
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

c = Circle(5)
print(c.area())

s = Square(5)
print(s.area())

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Base(ABC):
    @abstractmethod
    def hello(self):
        print("привет из Base")

class Product(ABC):
    @property
    @abstractmethod
    def price(self):
        pass

class Report(ABC):
    def print_header(self):
        print("отчет")

    @abstractmethod
    def generate(self):
        pass


class Printable:
    def my_print(self):
        print("печатаю")

class Document(ABC, Printable):
    @abstractmethod
    def get_content(self):
        pass

#mixins - миксы - небольшие классы, добавляющие одну конкретную функцию
"""
нет __init__() и отрибутов
предназначен для наследования совместно с другими
заканчивается на Mixin
"""

class LoggerMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class Worker:
    def work(self):
        print('работаю')

class LogginWorker(LoggerMixin, Worker):
    pass

lw = LogginWorker()
lw.work()
lw.log('готово')


#композиция - один класс содержит экземпляр другого, а не наследует его

class EngineV6:
    def start(self):
        print('двигатель запущен')

class EngineV4:
    def start(self):
        print('двигатель запущен')

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        self.engine.start()
        print("машина едет")



class A:
    def do(self):
        print("A")

class B(A):
    def do(self):
        print("B")

class C(A):
    def do(self):
        print("C")

class D(B, C):
    pass

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def move(self):
        print(f"{self.name} двигается")

class Dog(Animal):
    def __init__(self, name: str, age: int):
        self.age = age
        super().__init__(name)

    def bark(self):
        print(f"{self.name} гав")

    def move(self):
        #хорошо
        super().move()

        #плохо
        Animal.speak(self)

        print()

#super(CurrentClass, self)

class Parent:
    def greet(self):
        print('hi от родителя')

class Child(Parent):
    def greet(self):
        super(Child, self).greet()
        print("hi от ребенка")
        
class A:
    def do(self):
        print("A")

class B(A):
    def do(self):
        print("B")
        super().do()

class C(A):
    def do(self):
        print("C")
        super().do()

class D(B, C):
    def do(self):
        print("D")
        super().do()

d = D()
d.do()

#super(ClassName, instance).method()

#обычные - публичные - по умолчанию
"""class Person:
    def __init__(self, name):
        self.name = name"""

#protected защищенные
"""class Person:
    def __init__(self, name):
        self._name = name"""

#private приватные
"""class Person:
    def __init__(self, name):
        self.__name = name

person = Person("анна")
#print(person.__name)
print(person._Person__name)"""

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(100)
account.deposit(100)
account.__balance = 0
print(account.get_balance())
print(account.__balance)

class Car:
    def __init__(self, model, fuel):
        self.__model = model
        self.__fuel = fuel

    def drive(self):
        if self.__fuel > 0:
            self.__fuel -= 1
            print(f"{self.__model} поехала. Топливо {self.__fuel}")
        else:
            print(f"{self.__model} не может ехать")

    def get_fuel(self):
        return self.__fuel

car = Car('car', 4)
car.drive()
car.drive()
car.drive()
car.drive()
car.drive()

#type()

class Person:
    def greet(self):
        print("я человек")

def greet(self):
    print("я человек")

Person = type("Person", (object, ), {'greet': greet})

p = Person()
p.greet()

#type(class_name, bases, class_dict)

attrs = {
    'name': 'иван',
    'age': 30,
    'greet': lambda self: print(f"привет, я {self.name}")
}

Person = type('Person', (object, ), attrs)

p = Person()
p.greet()

def __init__(self, name, age):
    self.name = name
    self.age = age

def greet(self):
    print(f"привет, я {self.name}")

attrs = {
    '__init__': __init__,
    'greet': greet
}

Person = type('Person', (object, ), attrs)

class Animal:
    def speak(self):
        print('hi animal')

Dog = type('Dog', (Animal,), {'bark': lambda self: print("гав")})

d = Dog()
d.speak()
d.bark()

class MyClass:
    pass

MyClass = type('MyClass', (object,), {})

#метакласс

x = 5
print(type(x))
print(type(int))

class MyClass:
    def method(self):
        return 'привет'

print(MyClass.__name__)
print(MyClass.mro())
print(MyClass.__bases__)
print(MyClass.__dict__)
print(type(MyClass))

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"создание класса {name}")
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    pass

f = MyClass()

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f'создание нового класса {name}')
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f'инициализация класса {name}')
        super().__init__(name, bases, dct)

print(type(type))
print(type(object))
print(isinstance(type, type))
print(issubclass(type, object))
print(issubclass(object, type))

"""
x = 5
class MyClass:
"""

class MyClass(metaclass=MyMeta):
    attr = 10

MyMeta.__new__(MyMeta, "MyClass", (object, ), {'attr': 10})

class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        uppercase_attrs = {}
        for key, value in dct.items():
            if not key.startswith('__'):
                uppercase_attrs[key.upper()] = value
            else:
                uppercase_attrs[key] = value
        return super().__new__(cls, name, bases, uppercase_attrs)

class MyClass(metaclass=UpperAttrMeta):
    foo = 'bar'
    def method(self):
        return 'hello'

print(hasattr(MyClass, 'foo'))
print(hasattr(MyClass, 'FOO'))
print(MyClass.FOO)

registry = {}

class AutoRegisterMeta(type):
    def __init__(cls, name, bases, dct):
        registry[name] = cls
        super().__init__(name, bases, dct)

class Animal(metaclass=AutoRegisterMeta):
    pass

class Dog(Animal):
    pass

print(registry)

class Meta1(type): pass
class Meta2(type): pass

class Base1(metaclass=Meta1): pass
class Base2(metaclass=Meta2): pass

# class Child(Base1, Base2): pass
class Book:
    pass

b1 = Book
print(b1)
"""
str()
len()
+
==
"""

"""
__init__
__str__
__repr__
__new__
"""

"""
== __eq__
!= __ne__
< __lt__
<= __le__
> __gt__
>= __ge__
"""

"""
+ __add_
- __sub__
* __mul__
/ __truediv__
"""
"""
int __int__
float __float__
bool __bool__
"""

"""
доступ по индексу __getitem__
итерация for x in obj __iter__
получение следующего элемента  __next__
= __setitem__
удаление __delitem__

"""

class Quotes:
    def __init__(self, quotes):
        self.quotes = quotes

    def __getitem__(self, index):
        return self.quotes[index]

    def __len__(self):
        return len(self.quotes)

    def __iter__(self):
        return iter(self.quotes)

q = Quotes(['мир', ['труд']])
print(q[1])
for quote in q:
    print(quote)

"""
__enter__
__exit__
"""
"""
__getattr__ если атрибут не найден
__getattribute__ всегда при доступе к атрибуту
__setattr__ при присваивании
__delattr__ при удалении
"""

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} стр.)"

    def __repr__(self):
        return f"Book {self.title}, {self.pages}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.title == other.title

    def __add__(self, other):
        return Book(f"{self.title} + {other.title}", self.pages + other.pages)


b1 = Book("python", 900)
b2 = Book('sky', 700)
print(b1)
print(len(b2))
print(b1 == b2)
b3 = b1 + b2
print(b3)

print(b1 + 3)