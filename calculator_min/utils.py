"""
Нужен был doctring, я сделяль
"""

import math


def degrees_to_radians(degrees: int) -> float:
    """Преобразование градусов в радианы"""
    return degrees * (math.pi / 180.0)


def radians_to_degrees(radians: int) -> float:
    """Преобразование радианов в градусы"""
    return radians * (180.0 / math.pi)


def format_operation(operation_name: str, operands: list[float], result: str):
    """Форматирование операции для красивого вывода"""
    if len(operands) == 1:
        return f"{operation_name}({operands[0]}) = {result}"
    else:
        return f"{operands[0]} {operation_name} {operands[1]} = {result}"


def format_result(result: str):
    """Форматирование результата вычисления"""
    return f"Результат: {result}"


def is_integer(number: float | int) -> bool:
    """Проверка, является ли число целым"""
    if isinstance(number, int):
        return True
    return number.is_integer()


def is_positive(number: float) -> float:
    """Проверка, является ли число положительным"""
    return number > 0
