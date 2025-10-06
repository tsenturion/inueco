"""
методы и функции list
"""
zero_list = []

list1 = [1, 2, 3]
list1.append(1)  # добавление в конец
# list1 = [1, 2, 3, 1]

#print(list1.append(1)) - не сработает

list1.extend([5, 5])  # увеличение списка, list1 += [5, 5]
# list1 = [1, 2, 3, 1, 5, 5]

list1.insert(1, 9)  #вставка на позицию | insert(index, value)
# list1 = [1, 9, 2, 3, 1, 5, 5]

list1.remove(1)  # удаление первого вхождения
# list1 = [9, 2, 3, 1, 5, 5]

list1.pop(0)  # удаление по индексу
# list1 = [2, 3, 1, 5, 5]

number = list1.index(1)  # находит индекс первого вхождения
# number = 2 - тк 2 индекс

number = list1.count(5)  # количество вхождений
# number = 2 - тк 2 пятерки

list1.sort()  # сортировка
sorted(list1)  # сортировка
# list1 = [1, 2, 3, 5, 5]

list1.reverse()  # переворачивает
list1 = list1[::-1]  # переворачивает
# list1 = [5, 5, 3, 2, 1]

list1.clear()  # очищает
print(list1)

print([i for i in range(100)])
print([i**2 for i in range(10)])
print([i for i in range(100) if i % 2 == 0])
print([i for i in range(100) if i % 2 == 0 if i % 3 == 0])
print([None if x % 2 == 0 else x for x in range(100)])
print([i+j for i in range(10) for j in range(10)])
# кубы чисел кратных 14

print([i**3 for i in range(100) if i % 14 == 0])
def c14(limit):
    for i in range(14, limit, 14):
        yield i**3
g = c14(14)
print(list(g))
def gen(n):
    for i in range(1, n + 1):
        yield i
def fibgen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
g = list(gen(5))
print(g)
g = fibgen()
for _ in range(10):
    print(next(g))

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        raise Exception
    return fib(n - 1) + fib(n - 2)

print(fib(6))
print(fact(3))

def fast_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = fast_power(base, exponent // 2)
        return half_power * half_power
    else:
        return base * fast_power(base, exponent - 1)

print(fast_power(10, 5))
