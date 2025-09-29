"""
Модуль calculator.py - Математическое ядро
Содержит все математические операции: базовые арифметические и научные функции.
"""

import math


class CalculatorError(Exception):
    """Базовый класс для ошибок калькулятора"""
    pass


class DivisionByZeroError(CalculatorError):
    """Исключение для деления на ноль"""
    pass


class InvalidInputError(CalculatorError):
    """Исключение для некорректных входных данных"""
    pass


# Базовые арифметические операции
def add(a, b):
    """Сложение двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    return a + b


def subtract(a, b):
    """Вычитание двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    return a - b


def multiply(a, b):
    """Умножение двух чисел"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    return a * b


def divide(a, b):
    """Деление двух чисел с проверкой деления на ноль"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    if b == 0:
        raise DivisionByZeroError("Деление на ноль невозможно")
    return a / b


# Научные операции
def power(base, exponent):
    """Возведение в степень"""
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    try:
        return math.pow(base, exponent)
    except (OverflowError, ValueError) as e:
        raise CalculatorError(f"Ошибка при возведении в степень: {e}")


def square_root(x):
    """Квадратный корень с проверкой отрицательного значения"""
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    if x < 0:
        raise InvalidInputError("Нельзя извлечь квадратный корень из отрицательного числа")
    return math.sqrt(x)


def natural_log(x):
    """Натуральный логарифм"""
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    if x <= 0:
        raise InvalidInputError("Логарифм определен только для положительных чисел")
    return math.log(x)


def logarithm(x, base):
    """Логарифм по произвольному основанию"""
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    if x <= 0:
        raise InvalidInputError("Логарифм определен только для положительных чисел")
    if base <= 0 or base == 1:
        raise InvalidInputError("Основание логарифма должно быть положительным и не равным 1")
    return math.log(x, base)


def sine(x):
    """Синус угла в радианах"""
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    return math.sin(x)


def cosine(x):
    """Косинус угла в радианах"""
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    return math.cos(x)


def tangent(x):
    """Тангенс угла в радианах"""
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    return math.tan(x)


def factorial(n):
    """Факториал числа с проверкой на неотрицательное целое число"""
    if not isinstance(n, int):
        raise InvalidInputError("Факториал определен только для целых чисел")
    if n < 0:
        raise InvalidInputError("Факториал определен только для неотрицательных чисел")
    return math.factorial(n)