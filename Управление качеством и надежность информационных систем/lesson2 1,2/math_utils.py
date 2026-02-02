def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    else:
        return a / b

#добавить функцию для возведения в степень 
def power(a, b):
    return a ** b