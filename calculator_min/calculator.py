import math

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Ошибка: деление на ноль невозможно")
    return a / b

def power(base, exponent):
    """Возведение в степень"""
    return math.pow(base, exponent)

def square_root(x):
    """Квадратный корень"""
    if x < 0:
        raise ValueError("Ошибка: нельзя извлечь корень из отрицательного числа")
    return math.sqrt(x)

def natural_logarithm(x):
    """Натуральный логарифм"""
    if x <= 0:
        raise ValueError("Ошибка: логарифм определен только для положительных чисел")
    return math.log(x)

def logarithm(x, base):
    """Логарифм по произвольному основанию"""
    if x <= 0 or base <= 0 or base == 1:
        raise ValueError("Ошибка: некорректные значения для логарифма")
    return math.log(x, base)

def sine(angle_rad):
    """Синус угла в радианах"""
    return math.sin(angle_rad)

def cosine(angle_rad):
    """Косинус угла в радианах"""
    return math.cos(angle_rad)

def tangent(angle_rad):
    """Тангенс угла в радианах"""
    return math.tan(angle_rad)

def factorial(n):
    """Факториал числа"""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Ошибка: факториал определен для неотрицательных целых чисел")
    return math.factorial(n)