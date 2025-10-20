from calculator import *
from utils import *

def demonstrate_arithmetic_operations():
    """Демонстрация арифметических операций"""
    print("=" * 50)
    print("АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ")
    print("=" * 50)
    
    # Корректные операции
    test_cases = [
        ("+", add, 15, 3),
        ("-", subtract, 15, 3),
        ("×", multiply, 15, 3),
        ("÷", divide, 15, 3)
    ]
    
    for symbol, operation, a, b in test_cases:
        try:
            result = operation(a, b)
            print(format_operation(symbol, (a, b), result))
        except ValueError as e:
            print(f"{a} {symbol} {b} -> {e}")
    
    # Обработка ошибок
    print("\nОбработка ошибок:")
    try:
        divide(10, 0)
    except ValueError as e:
        print(f"10 ÷ 0 -> {e}")

def demonstrate_scientific_operations():
    """Демонстрация научных операций"""
    print("\n" + "=" * 50)
    print("НАУЧНЫЕ ОПЕРАЦИИ")
    print("=" * 50)
    
    # Операции с одним аргументом
    single_arg_operations = [
        ("√", square_root, 25),
        ("ln", natural_logarithm, math.e),
        ("√", square_root, -4),  # Ошибочный случай
        ("ln", natural_logarithm, -1)  # Ошибочный случай
    ]
    
    for symbol, operation, x in single_arg_operations:
        try:
            result = operation(x)
            print(format_operation(symbol, (x,), result))
        except ValueError as e:
            print(f"{symbol}({x}) -> {e}")
    
    # Операции с двумя аргументами
    print("\nОперации с двумя аргументами:")
    try:
        result = power(2, 8)
        print(format_operation("^", (2, 8), result))
    except ValueError as e:
        print(f"2 ^ 8 -> {e}")
    
    try:
        result = logarithm(100, 10)
        print(format_operation("log", (100, 10), result))
    except ValueError as e:
        print(f"log₁₀(100) -> {e}")

def demonstrate_trigonometric_operations():
    """Демонстрация тригонометрических операций"""
    print("\n" + "=" * 50)
    print("ТРИГОНОМЕТРИЧЕСКИЕ ОПЕРАЦИИ")
    print("=" * 50)
    
    angles_degrees = [0, 30, 45, 60, 90]
    angles_radians = [degrees_to_radians(angle) for angle in angles_degrees]
    
    print("Углы в градусах и радианах:")
    for deg, rad in zip(angles_degrees, angles_radians):
        print(f"{deg}° = {rad:.3f} рад")
    
    print("\nТригонометрические функции:")
    for deg, rad in zip(angles_degrees, angles_radians):
        sin_val = sine(rad)
        cos_val = cosine(rad)
        
        print(f"{deg}°: sin = {sin_val:.3f}, cos = {cos_val:.3f}", end="")
        
        try:
            tan_val = tangent(rad)
            print(f", tan = {tan_val:.3f}")
        except ValueError:
            print(f", tan = не определен")

def demonstrate_factorial_operations():
    """Демонстрация операций с факториалом"""
    print("\n" + "=" * 50)
    print("ОПЕРАЦИИ С ФАКТОРИАЛОМ")
    print("=" * 50)
    
    numbers = [0, 1, 5, 10]
    
    for n in numbers:
        try:
            result = factorial(n)
            print(format_operation("!", (n,), result))
        except ValueError as e:
            print(f"{n}! -> {e}")
    
    # Ошибочные случаи
    print("\nОбработка ошибок:")
    error_cases = [-1, 3.5, "5"]
    
    for case in error_cases:
        try:
            result = factorial(case)
            print(format_operation("!", (case,), result))
        except (ValueError, TypeError) as e:
            print(f"{case}! -> {e}")

def demonstrate_utility_functions():
    """Демонстрация вспомогательных функций"""
    print("\n" + "=" * 50)
    print("ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ")
    print("=" * 50)
    
    # Преобразование единиц
    test_degrees = [0, 90, 180, 270, 360]
    print("Преобразование градусов в радианы:")
    for deg in test_degrees:
        rad = degrees_to_radians(deg)
        deg_back = radians_to_degrees(rad)
        print(f"{deg}° = {rad:.3f} рад -> {deg_back:.1f}°")
    
    # Проверка свойств чисел
    print("\nПроверка свойств чисел:")
    test_numbers = [5, -3, 0, 7.0, 8.5]
    for num in test_numbers:
        int_check = "целое" if is_integer(num) else "не целое"
        pos_check = "положительное" if is_positive(num) else "не положительное"
        print(f"{num}: {int_check}, {pos_check}")

def main():
    """Основная функция программы"""
    print("НАУЧНЫЙ КАЛЬКУЛЯТОР")
    print("Демонстрация модульной архитектуры")
    print("=" * 50)
    
    try:
        demonstrate_arithmetic_operations()
        demonstrate_scientific_operations()
        demonstrate_trigonometric_operations()
        demonstrate_factorial_operations()
        demonstrate_utility_functions()
        
        print("\n" + "=" * 50)
        print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА УСПЕШНО")
        print("=" * 50)
        
    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()