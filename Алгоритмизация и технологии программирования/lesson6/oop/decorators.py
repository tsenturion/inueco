
"""def decorator(func):
    def wrapper():
        print("декоратор сработал до вызова функции")
        func()
        print("после вызова")
    return wrapper

@decorator
def say_hello():
    print('функция')

say_hello()"""
import time


"""def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"вызывается {func.__name__} с аргументами {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"функция {func.__name__} завершила выполнение")
        return result
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add(3, 5))"""
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print('hi')

say_hi()"""

"""def methor_decorator(func):
    def wrapper(self, *args, **kwargs):
        print(f"вызов метода {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Example:
    @methor_decorator
    def greet(self):
        print("привет от класса")

obj = Example()
obj.greet()
"""
"""from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("выполняетя декорированная функция")
        return func(*args, **kwargs)
    return wrapper

@decorator
def example():
    """"""эта функция возвращает hello""""""
    return "hello"

print(example.__name__)
print(example.__doc__)"""
"""
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))

class Counter:
    count = 0
    @classmethod
    def increment(cls):
        cls.count += 1

Counter.increment()
Counter.increment()
print(Counter.count)

""""""
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("")
        self._radius = value

    @radius.deleter
    def radius(self):
        raise AttributeError("")



c = Circle(5)
print(c.radius)
#c.radius = -3
del c.radius"""

"""from functools import lru_cache

class Fibonacci:
    @lru_cache(maxsize=None)
    def fib(self, n):
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

f = Fibonacci()
print(f.fib(50))

from contextlib import contextmanager

class FileHandler:
    @contextmanager
    def open_file(self, filename):
        file = open(filename, 'w')
        try:
            yield file
        finally:
            file.close()

handler = FileHandler()
with handler.open_file("test.txt") as f:
    f.write("hi")



from functools import singledispatchmethod

class Printer:
    @singledispatchmethod
    def show(self, value):
        raise NotImplementedError("")

    @show.register
    def _(self, value: int):
        print(f"целое число: {value}")

    @show.register
    def _(self, value: str):
        print(f"строка {value}")

printer = Printer()
printer.show(10)
printer.show("hi")

from functools import  cached_property

class ExpensiveComputation:
    def __init__(self, x):
        self.x = x

    @cached_property
    def compute(self):
        print("выполнение сложных вычислений")
        return self.x ** 2

obj = ExpensiveComputation(10)
print(obj.compute)
print(obj.compute)


from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p1 = Point(10, 20)
p2 = Point(10, 20)
print(p1)
print(p1 == p2)"""
"""
from functools import total_ordering

@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        if grade > 0:
            self.grade = grade
        else:
            throw Exception

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade

s1 = Student("q", 90)
s2 = Student("b", 85)

print(s1 > s2)
print(s1 <= s2)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return  get_instance

@singleton
class Database:
    def __init__(self):
        print("создали")

db1 = Database()
db2 = Database()

print(db1 is db2)


@classproperty
"""
"""аналог @propertry для класса"""

"""



@timing

@validate_args

@log_methods"""
"""# ----------------------------------------------------------------

def my_decorator(func):
    def wrapper():
        print("что-то перед")
        func()
        print("что-то после")
    return wrapper


@my_decorator
def say_hello():
    print("hello")
# ----------------------------------------------------------------

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print('hi')
# ----------------------------------------------------------------

def methor_decorator(func):
    def wrapper(self, *args, **kwargs):
        print(f"вызов метода {func.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class Example:
    @methor_decorator
    def greet(self):
        print("привет от класса")

obj = Example()
obj.greet()
# ----------------------------------------------------------------

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("что-то перед")
        result = self.func(*args, **kwargs)
        print("что-то после")
        return result

@MyDecorator
def say_hi():
    print('hi')

say_hi()
# ----------------------------------------------------------------"""

"""
1
logger - декоратор, для логирования вызова функций 
должен выводить
имя
аргументы
время вызова
import time
time()
"""
"""import time
def logger(func):
    def wrapper(*args, **kwargs):
        timestamp = time.time()
        print(f"[{timestamp}] вызов {func.__name__}")
        print(f"args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def add(x, y):
    return x + y

add(4, 5)
# ----------------------------------------------------------------"""

"""
timer / timing
будет замерять время выполнения функции и выводить
"""
"""def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"f{func.__name__} за {end_time - start_time}с.")
    return wrapper

@timer
def add(x, y):
    time.sleep(1)
    return x + y

add(3, 5)
# ----------------------------------------------------------------
"""
"""
current_user = "admin"
check_access
проверяет имеет ли пользователь доступ к функции
принимает уровень доступа
"""
"""current_user = "admin"

def check_access(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user == role:
                return func(*args, **kwargs)
            else:
                print('нет доступа')
        return wrapper
    return decorator

@check_access('admin')
def delete_db():
    print('удалено')

delete_db()
# ----------------------------------------------------------------"""

"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hi():
    print('hi')
    
retry
повторять вызов функции n раз, если она завершилась с ошибкой

random < 0.5
    raise ошибка
успех
"""
# ----------------------------------------------------------------
"""
def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attemp in range(1, n + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"попытка {attemp}: ошибка")
                    if attemp == n:
                        raise e
        return wrapper
    return decorator

@retry(3)
def risky_func():
    import random
    if random.random() < 0.5:
        raise ValueError("ошибка")
    return "успех"

print(risky_func())"""
# ----------------------------------------------------------------
"""
rate_limit
ограничивает частоту вызовов 
если вызывается чаще раз в 5 секунд, выводим предупреждение
"""
"""def rate_limit(interval):
    last_called = 0

    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal last_called
            elapsed = time.time() - last_called
            if elapsed < interval:
                print(f"слишком частые вызовы. Подождать {interval - elapsed:.3f} с.")
                return
            last_called = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(5)
def send_request():
    print("запрос отправлен")

send_request()
time.sleep(3)
send_request()
time.sleep(2)
send_request()"""
#----------------------------------------------------------------
"""
to_upper
преобразует результат ф в верх рег
"""
"""def to_upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper

@to_upper
def say_hi():
    return "hi"

print(say_hi())"""
#----------------------------------------------------------------

"""
validate_args
проверка что аргументы ф положительные
"""
"""
def validate_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg < 0:
                raise ValueError("")
        return func(*args, **kwargs)
    return wrapper

@validate_args
def multiply(a, b):
    return a * b

print(multiply(3, 5))
print(multiply(-3, 5))"""
#----------------------------------------------------------------

"""
count_calls
считает количество вызовов функции, выводит при каждом вызове
"""
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"f {func.__name__} вызвана {wrapper.call_count} р.")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def say_hi():
    print("hi")

say_hi()
say_hi()
say_hi()

