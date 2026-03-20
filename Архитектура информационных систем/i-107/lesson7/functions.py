#def - определение функции, имя функции, скобки, двоеточие, тело функции
def greet():
    print("Hello")
    
greet()

#в скобоках - аргументы функции
def add(a, b):
    print(a + b)
    print(a + b)
    print(a + b)
    print(a + b)

add(1, 2)

def hello(name):
    print('hello', name)

hello('world')

# функция может не возвращать значение
print(1)

# функция может возвращать значение
a = int('123')
#b = input()

# в def функциях используется return
def add(a, b):
    return a + b

a = add(78, 2)
print(a)