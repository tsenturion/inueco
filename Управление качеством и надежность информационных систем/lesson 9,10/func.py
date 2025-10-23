"""
def - ключевое слово для создания функции
после def пробел
далее любое имя функции
далее (...параметры):
    return для возврата значения
"""

def minimum_function():
    pass

def minimum_function2():
    ...

def add(a, b):
    print(a + b)

add(2, 5)
add(10, 20)
    
def custom_print():
    print("Hello world")
    print("Hello world")
    print("Hello world")

custom_print()

a = 1
b = 2
add(1, 2)
add(a, b)
add(b=a, a=b)

def summa(a, b=0, c=0, d=0):
    print(a + b + c + d)

summa(a=1)
summa(1, 2)
summa(1, 2, 3)
summa(d=4, c=3, a=1)

a = int(1.2)
a = summa(1)

print()
print("текс")
a = print("текст 2")
print(a)

def add(a, b):
    return a + b

result = add(30, 40)
print(result)
print(add(30, 40))


def return_function():
    return {'some': 'data'}

print(return_function())

a = 1
a: int = 1
a = '1'

def output_data(data):
    print(data)

def output_data(data: str) -> None | int:
    print(data)

def multi_return() -> tuple:
    return 1, "1"

a, b = multi_return()

print(multi_return())
print(a)
print(b)
