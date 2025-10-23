"""
Модуль utils.py - Вспомогательные утилиты
Содержит функции для преобразования единиц измерения, форматирования вывода
и проверки данных.
"""

import math


# Утилиты преобразования единиц измерения
def degrees_to_radians(degrees):
    """Преобразование градусов в радианы"""
    if not isinstance(degrees, (int, float)):
        raise ValueError("Аргумент должен быть числом")
    return math.radians(degrees)


def radians_to_degrees(radians):
    """Преобразование радианов в градусы"""
    if not isinstance(radians, (int, float)):
        raise ValueError("Аргумент должен быть числом")
    return math.degrees(radians)


# Утилиты форматирования вывода
def format_operation(operation_name, operands, result):
    """Форматирование математических операций для красивого вывода"""
    if isinstance(operands, (list, tuple)):
        operands_str = ", ".join(str(op) for op in operands)
    else:
        operands_str = str(operands)
    
    return f"{operation_name}({operands_str}) = {result}"


def create_result_string(operation, result, error=None):
    """Создание строки с результатом вычисления"""
    if error:
        return f"{operation}: ОШИБКА - {error}"
    else:
        return f"{operation}: {result}"


def format_number(number, precision=6):
    """Форматирование числа с заданной точностью"""
    if isinstance(number, float):
        # Убираем незначащие нули
        formatted = f"{number:.{precision}f}".rstrip('0').rstrip('.')
        return formatted if formatted else '0'
    return str(number)


# Утилиты для работы с данными
def is_integer(value):
    """Проверка числа на целость"""
    if isinstance(value, int):
        return True
    if isinstance(value, float):
        return value.is_integer()
    try:
        float_val = float(value)
        return float_val.is_integer()
    except (ValueError, TypeError):
        return False


def is_positive(value):
    """Проверка числа на положительность"""
    try:
        num_val = float(value)
        return num_val > 0
    except (ValueError, TypeError):
        return False


def is_valid_number(value):
    """Проверка на корректное число"""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def safe_float(value, default=0.0):
    """Безопасное преобразование в float"""
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def truncate_result(result, max_length=15):
    """Усечение результата для отображения в интерфейсе"""
    result_str = str(result)
    if len(result_str) > max_length:
        try:
            # Для очень больших или очень маленьких чисел используем научную нотацию
            float_result = float(result)
            if abs(float_result) > 1e10 or (0 < abs(float_result) < 1e-4):
                return f"{float_result:.3e}"
            else:
                return f"{float_result:.6g}"
        except (ValueError, OverflowError):
            return result_str[:max_length] + "..."
    return result_str