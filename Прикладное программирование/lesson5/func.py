def minimum_function():
    pass

def minimum_function2():
    ...

def add(a, b):
    g = 9.8
    print(a + b)
    print(a + b)
    print(g)
    print(id(a))
    print(id(b))
    print()

    
def custom_print():
    print("Hello world")
    print("Hello world")
    print("Hello world")

a = 1
b = 2
print(id(a))
print(id(b))

add(a=a, b=b)
add(2, 5)
add(2, 5)
add(2, 5)

print(2, 3)
print(id(a))
print(id(b))
custom_print()

#print(g)

def summa(a, b=0, c=0, d=0):
    print(a + b + c + d)

summa(a=1)
summa(1, 2)
summa(1, 2, 3)

a = int(1.2)
a = summa(1)

print()

def add(a, b):
    return a + b

result = add(1, 2)
print(add(1, 2))


def return_function():
    return {'some': 'data'}

print(return_function())

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
