def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    else:
        return a / b

#добавить функцию для возведения в степень 

def pow(a, b):
    if  b == 0:
        return 1
    elif b < 0:
        return 1/(a ** abs(b))
    else:
        return a ** b
    