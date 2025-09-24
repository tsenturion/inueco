def sqr1(number):
    """docstring полное описание"""
    return number * number

sqr = lambda x : x * x

def printf(some_list, func):
    """docstring"""
    for i in some_list:
        print(func(i))


list1 = list(range(5))

printf(list1, sqr1)
printf(list1, lambda x : x * x)

print(sqr(5))
"""
map - применяем F ко всем элементам последовательности
map(функция, последовательность)
"""
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

def square(x):
    return x ** 2

squared = list(map(square, numbers))
print(squared)

for i in map(sqr1, list1):
    print(i)
list2 = list(map(sqr1, list1))
print(list2)


"""
filter - фильтрация, запишет те, для которых f возвращает True
filter(функция, последовательность)
f возвращает True False
"""

even_numbers = list(filter(lambda x : x % 2 == 0, numbers))

def is_even(x):
    return x % 2 == 0
for i in filter(lambda x : x % 2 == 0, list1):
    print(i)
list1 = list(filter(lambda x : x % 2 == 0, list1))
print(list1)
fib = lambda n : n if n <= 1 else fib(n - 1) + fib(n - 2)
fact = lambda n : 1 if n == 0 else n * fact(n - 1)

#vfact = lambda f: f(f, n)
#infact = lambda n :
fact2 = lambda f , x :  1 if x == 0 else x * f(f, x - 1)
ifact = lambda n : (lambda f: f(f, n))(fact2)

list1 = list(map(fib, range(10)))
list2 = list(map(fact, range(10)))
print(list1)
print(list2)


from functools import reduce

"""
reduce - 
reduce(функция, последовательность, начальное значение)
функция принимает два аргумента
"""
numbers = [1, 2, 3, 4, 5]

product = reduce(lambda  x, y : x * y, numbers)
"""
----------1-----------
x = 1 = numbers[0]
y = 2 = numbers[1]
lambda  x, y : x * y

1 * 2
= 2 - начальное накопительное значение

----------2-----------
x = 2 = накопительное
y = 3 = numbers[2]
lambda  x, y : x * y

2 * 3
= 6

6 * 4 = 24
24 * 5 = 120

"""

def multiply(x, y):
    return x * y

product2 = reduce(multiply, numbers)

"""

filter - оставить четные 
map - возвести в квадрат
reduce - сложить все квадраты
"""

# from functools import reduce
numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)






multuply = lambda x : lambda y : x * y
double = multuply(3)
print(double(5))

curried_function = lambda x : lambda y : lambda z : x + y + z
add_5 = curried_function(2)(3)
print(add_5(4))


def curried_add(x):
    return lambda y : x + y

def add(x, y):
    return x + y

add_3 = partial(add, 3)

#import logging

def log(level):
    return lambda message: f"[{level.upper()}] {message}"

info = log("INFO")
error = log("ERROR")

print(info("This is an info message"))

"""
Напишите каррированную функцию с lambda, которая умножает число на коэффициент и добавляет смещение
Функция должна принимать два параметра: коэффициент и смещение
Вернуть замыкание, которое принимает одно число и выполняет вычисление

результат=(число×коэффициент)+смещение
"""

def create_transformer(coefficient):
    return lambda offset : lambda number : (number * coefficient) + offset

transformer = create_transformer(2)

add_3 = transformer(3)
add_5 = transformer(5)

print(add_3(10))

print(add_5(10))






strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
"""сделать первые буквы заглавными map, lambda"""

strlist = list(map(lambda n : n.title(), strlist))

numlist = ['1 2 3 4', '1 2 3 4', '1 2 3 4', '1 2 3 4']
"""найти сумму элементов map, lambda, .split()numlist = [10, 10, 10, 10]"""
numlist = list(map(lambda s: sum(map(int, s.split())), numlist))

strlist = ['121', 'fsd1231', 'fsd1231', 'Rsd1231', 'Rsd1231']
"""список слов с заглавной буквы, сделать их прописными filter
strlist = ['rsd1231', 'rsd1231']"""
strlist = list(map(lambda x : x.lower(), filter(lambda x : x.istitle(), strlist)))

strlist = ['121', '123321', 'fsd1231', 'Rsd1231', 'Rsd1231']
"""одинаково слева направо strlist = ['121', '123321']"""

strlist = list(filter(lambda x : x == x[::-1], strlist))

strlist = ['a', '123321', 'fsd1231', 'ii', 'Rsd1231']
"""с любой гласной aeiouyAEIOUY"""
strlist = ['a', 'ii']
b = "aeiouyAEIOUY"
strlist = list(filter(lambda x: any(ch in b for ch in x), strlist))
print()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Удвойте каждый элемент списка чисел.
print(list(map(lambda x : x * 2, numbers)))

# Отфильтруйте чётные числа из списка.
print(list(filter(lambda x : x % 2 == 0, numbers)))

# Преобразуйте все строки в списке в верхний регистр.
strlist = ['fsd1231', 'fsd1231', 'fsd1231', 'fsd1231']
print(list(map(lambda s : s.upper(), strlist)))

# Отфильтруйте положительные числа из списка.
print(list(filter(lambda x : x > 0, numbers)))

# Вычислите квадраты всех чисел в списке.
print(list(map(lambda x : x ** 2, numbers)))

# Отфильтруйте чётные числа, а затем возведите их в квадрат. map filter
print(list(map(lambda x : x ** 2, filter(lambda x : x % 2 == 0, numbers))))