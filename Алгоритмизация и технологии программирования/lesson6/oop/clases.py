from abc import ABC

"""экземпляр - конкретный объект созданный на основе класса
атрибут(поле) класса - принадлежит самому классу и разделяется всеми экземплярами
атрибут(поле) экземпляра - принадлежит конкретному объекту  и уникален для каждого экземпляра
метод экземпляра def - функция конкретного объекта
метод класса @classmethod- работает с классом в целом
метод статический @staticmethod- не зависит от класса или объекта, нет доступа, но относится
конструктор __init__- вызывается при создании объекта
наследование - новый класс на основе существующего
полиморфизм - возможность использовать один и тот же интерфейс (метод) для объектов разных классов
инкапсуляция __ - скрытие деталей
свойство - атрибут поволяющий управлять доступом к данным через гет сет дел
дескриптор - объект который оперделяет поведение атрибутов класса __гет__ __сет__ __удалить__
магические методы - __???__ для перегрузки операторов
абстрактный класс - используется как шаблон, указываются методы для реализации
метакласс - определяет поведение других классов
множественное наследование
MRO - порядок поиска методов в иерархии наследования
перегрузка - переопределение поведения операторов и функций
сеттер - устанавливает значение атрибута
геттер - возвращает значение атрибута
делитер - метод удаляет атрибут
приватный атрибут - не предназначен для доступа извне
декораторы - через @
миксины - классы с доп функционалом, не предназначены для самостоятельного использования
"""

class Person:

    health = 100

    def __init__(self, name, age, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student
        self.gender = None

    def invert_is_student(self):
        self.is_student = not self.is_student

    @staticmethod
    def to_learn():
        print('im learning')

    @classmethod
    def print_health(cls):
        print(cls.health)

Person.print_health()
print(Person.health)

num = 1
Matvey = Person('name', 18)
Matvey2 = Person('name', 18)
Matvey2 = Person('name', 18)
print(Matvey.is_student)
Matvey.invert_is_student()
print(Matvey.is_student)
Matvey.to_learn()


# создать математический класс с атрибутом количества
# несколько методов cls которые возвращают генератор
# init принимает список строк с желаемыми функциями
# метод который их выводит

class MClass:
    length = 5

    def __init__(self, func):
        self.func = func

    def print_func(self):
        print(self.func)

    @classmethod
    def gen1(cls):
        return [i for i in range(cls.length)]

    @classmethod
    def gen2(cls):
        return [i**2 for i in range(cls.length)]

print(MClass.length)
print(MClass.gen1())
print(MClass.gen2())
MyMath = MClass(['sum', 'pow'])
MyMath.print_func()
# MClass от него унаследовать в тригонометрию
# в триг мат функции
# иниц предыдущее и 1 новое
# из триг вызвать методы MClass
from math import *
class Trig(MClass):

    def __init__(self, func, inp):
        super().__init__(func)
        self.inp = inp

    def trig_sin(self):
        return sin(self.inp)

    def trig_cos(self):
        return cos(self.inp)

    def greet(self):
        super().print_func()

import collections

from abst import Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.__owner = 'me'

    def make_voice(self):
        print(f'{self.name} maked voice')

    def walk(self):
        print(f'{self.name} walked')

    def print_owner(self):
        print(self.__owner)

    @classmethod
    def info(cls):
        print(super().info)

MyCat = Cat('cat')
MyCat.make_voice()
MyCat.walk()
MyCat.print_owner()
Cat.info()
from abst import MClass
class Alg(MClass):
    @classmethod
    def add(cls):
        return 5
    @classmethod
    def substruct(cls):
        return 7

class Dog(Animal):
    pass