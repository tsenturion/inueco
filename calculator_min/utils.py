#поправить по pep8 (flake8), по pylance, по sonarqube, по pylint
#python -m pylint calculator_min\utils.py
#python -m flake8 calculator_min\utils.py
import math


def degrees_to_radians(degrees: int) -> float:
    """Преобразование градусов в радианы"""
    return degrees * (math.pi / 180.0)


def radians_to_degrees(radians):
    """Преобразование радианов в градусы"""
    return radians * (180.0 / math.pi)

def format_operation(operation_name, operands, result):
    """Форматирование операции для красивого вывода"""
    if len(operands) == 1:
        return f"{operation_name}({operands[0]}) = {result}"
    else:
        return f"{operands[0]} {operation_name} {operands[1]} = {result}"

def format_result(operation, result):
    """Форматирование результата вычисления"""
    return f"Результат: {result}"

def is_integer(number):
    """Проверка, является ли число целым"""
    return isinstance(number, int) or (isinstance(number, float) and number.is_integer())

def is_positive(number):
    """Проверка, является ли число положительным"""
    return number > 0