def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    else:
        return a / b

def power(base, exponent):
    """Возведение в степень"""
    if isinstance(exponent, int) and exponent >= 0:
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    return pow(base, exponent)