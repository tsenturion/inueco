def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

closure = outer_function(10)
result = closure(5)
print(result)

# global
global_var = 30
def example():
    global global_var
    global_var += 10
    print(global_var)

example()
print(global_var)

# nonlocal
def outer():
    nonlocal_var = 40

    def inner():
        nonlocal nonlocal_var
        nonlocal_var += 10
        print(nonlocal_var)

    inner()
    print(nonlocal_var)

outer()

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter1 = counter()
print(counter1())
print(counter1())
print(counter1())

def multiplier(n):
    def multiply(x):
        return  x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))


"""
def возвращает словарь счетчика с методами
+1
-1
текущее
сброс к начальному
история изменений
откат к предыдущему
"""
"""
def smart_counter(initial_value=0):
    value = initial_value
    history_list = [initial_value]

    def increment():
        nonlocal value
        pass

    def decrement():
        nonlocal value
        value -= 1
        history_list.append(value)
    def get_value():
        return value
    def history():
        return history_list
    def undo():
        nonlocal value
        if len(history_list) > 1:
            history_list.pop()
            value = history_list[-1]
    return {
        "increment": increment,
        "decrement": decrement,
        "get_value": get_value,
        #reset
        "history": history,
        "undo": undo,
    }

counter = smart_counter(5)
counter['history']()
counter['undo']()
counter['decrement']()
"""
"""def add(a, b):
    return a + b

def add_curried(a):
    def inner(b):
        def inner2(c):
            return a + b + c
        return inner2
    return inner

result = add_curried(2)(3)(4)
print(result)

from functools import partial
add_two = partial(add, 2)
result = add_two(3)
print(result)

def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *more_args: curried(*(args + more_args))
    return curried

@curry
def add(a, b, c):
    return a + b + c

result = add(1)(2)(3)
print(result)"""

"""
add
subtract
multiply
divide"""

from functools import partial

"""
def operation(a):
    def inner(b):
        def oper(op):
            try:
                if op == 'add':
                    return a + b
                elif op == "subtract":
                    return a - b
                elif op == "divide":
                    if b == 0:
                        raise ZeroDivisionError('нельзя делеить на 0')
                    return a / b
                elif op == 'multiply':
                    return a * b
                else:
                    raise ValueError('текст который будет напечатан при ошибке')
            except ValueError as e:
                return str(e)
            except ZeroDivisionError as e:
                return str(e)
            except Exception as ex:
                return ex
        return oper
    return inner
"""
"""result = operation(10)(5)('add')
print(result)
result = operation(10)(0)('divide')
print(result)
print(result is None)
result = operation(10)(5)('adde')
print(result)
print(result is None)"""

def operation(a, b, operation):
    try:
        if operation == 'add':
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "divide":
            if b == 0:
                raise ZeroDivisionError('123')
            return a / b
        elif operation == 'multiply':
            return a * b
        else:
            raise ValueError('1234')
    except ValueError as e:
        return str(e)
    except ZeroDivisionError as e:
        return str(e)
    except Exception as ex:
        return ex

add = partial(operation, op='add')
my_add = partial(operation, op='add', a=10)
add_10 = partial(partial(operation, a=10), op='add')
divide = partial(operation, op='divide')
divide2 = partial(operation, op='d3ivide')
"""print(add(10, 2))
print(add_10(b=2))
print(divide(10, 2))
print(divide(10, 0))
print(divide2(10, 2))
"""
print(add_10(b=5))
print(my_add(b=5))
