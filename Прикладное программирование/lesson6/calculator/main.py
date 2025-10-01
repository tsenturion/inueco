"""
Модуль main.py - Основная программа с GUI
Реализует интерфейс научного калькулятора используя tkinter.
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math

# Импорт модулей (в реальном проекте это будут отдельные файлы)
# from calculator import *
# from utils import *

# Для демонстрации включаем код модулей здесь
# === Код модуля calculator.py ===
class CalculatorError(Exception):
    """Базовый класс для ошибок калькулятора"""
    pass

class DivisionByZeroError(CalculatorError):
    """Исключение для деления на ноль"""
    pass

class InvalidInputError(CalculatorError):
    """Исключение для некорректных входных данных"""
    pass

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    return a + b

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    return a * b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    if b == 0:
        raise DivisionByZeroError("Деление на ноль невозможно")
    return a / b

def power(base, exponent):
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    try:
        return math.pow(base, exponent)
    except (OverflowError, ValueError) as e:
        raise CalculatorError(f"Ошибка при возведении в степень: {e}")

def square_root(x):
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    if x < 0:
        raise InvalidInputError("Нельзя извлечь квадратный корень из отрицательного числа")
    return math.sqrt(x)

def natural_log(x):
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    if x <= 0:
        raise InvalidInputError("Логарифм определен только для положительных чисел")
    return math.log(x)

def logarithm(x, base):
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise InvalidInputError("Аргументы должны быть числами")
    if x <= 0:
        raise InvalidInputError("Логарифм определен только для положительных чисел")
    if base <= 0 or base == 1:
        raise InvalidInputError("Основание логарифма должно быть положительным и не равным 1")
    return math.log(x, base)

def sine(x):
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    return math.sin(x)

def cosine(x):
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    return math.cos(x)

def tangent(x):
    if not isinstance(x, (int, float)):
        raise InvalidInputError("Аргумент должен быть числом")
    return math.tan(x)

def factorial(n):
    if not isinstance(n, int):
        raise InvalidInputError("Факториал определен только для целых чисел")
    if n < 0:
        raise InvalidInputError("Факториал определен только для неотрицательных чисел")
    return math.factorial(n)

# === Код модуля utils.py ===
def degrees_to_radians(degrees):
    if not isinstance(degrees, (int, float)):
        raise ValueError("Аргумент должен быть числом")
    return math.radians(degrees)

def radians_to_degrees(radians):
    if not isinstance(radians, (int, float)):
        raise ValueError("Аргумент должен быть числом")
    return math.degrees(radians)

def format_number(number, precision=6):
    if isinstance(number, float):
        formatted = f"{number:.{precision}f}".rstrip('0').rstrip('.')
        return formatted if formatted else '0'
    return str(number)

def is_valid_number(value):
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False

def safe_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def truncate_result(result, max_length=15):
    result_str = str(result)
    if len(result_str) > max_length:
        try:
            float_result = float(result)
            if abs(float_result) > 1e10 or (0 < abs(float_result) < 1e-4):
                return f"{float_result:.3e}"
            else:
                return f"{float_result:.6g}"
        except (ValueError, OverflowError):
            return result_str[:max_length] + "..."
    return result_str


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Научный калькулятор")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Переменная для хранения текущего выражения
        self.current_expression = ""
        self.result_var = tk.StringVar()
        self.expression_var = tk.StringVar()
        
        # Режим углов (градусы/радианы)
        self.angle_mode = tk.StringVar(value="degrees")
        
        self.setup_ui()
        
    def setup_ui(self):
        """Настройка пользовательского интерфейса"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Дисплей калькулятора
        self.create_display(main_frame)
        
        # Режим углов
        self.create_angle_mode_selector(main_frame)
        
        # Кнопки калькулятора
        self.create_buttons(main_frame)
        
    def create_display(self, parent):
        """Создание дисплея калькулятора"""
        display_frame = ttk.Frame(parent)
        display_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Поле для отображения выражения
        expression_entry = ttk.Entry(display_frame, textvariable=self.expression_var, 
                                   font=("Arial", 12), state="readonly")
        expression_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # Поле для отображения результата
        result_entry = ttk.Entry(display_frame, textvariable=self.result_var, 
                               font=("Arial", 16, "bold"), state="readonly")
        result_entry.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        display_frame.columnconfigure(0, weight=1)
        
    def create_angle_mode_selector(self, parent):
        """Создание селектора режима углов"""
        angle_frame = ttk.Frame(parent)
        angle_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(angle_frame, text="Режим углов:").grid(row=0, column=0, padx=(0, 10))
        
        ttk.Radiobutton(angle_frame, text="Градусы", variable=self.angle_mode, 
                       value="degrees").grid(row=0, column=1, padx=(0, 10))
        ttk.Radiobutton(angle_frame, text="Радианы", variable=self.angle_mode, 
                       value="radians").grid(row=0, column=2)
        
    def create_buttons(self, parent):
        """Создание кнопок калькулятора"""
        buttons_frame = ttk.Frame(parent)
        buttons_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Стиль кнопок
        button_style = {"width": 8, "height": 2, "font": ("Arial", 10)}
        
        # Ряд 1 - Функции очистки и специальные операции
        buttons_row1 = [
            ("C", self.clear_all), ("CE", self.clear_entry), ("⌫", self.backspace), ("±", self.toggle_sign)
        ]
        
        # Ряд 2 - Научные функции 1
        buttons_row2 = [
            ("x²", lambda: self.add_function("square")), ("x³", lambda: self.add_function("cube")), 
            ("xʸ", lambda: self.add_operator("**")), ("√", lambda: self.add_function("sqrt"))
        ]
        
        # Ряд 3 - Научные функции 2  
        buttons_row3 = [
            ("ln", lambda: self.add_function("ln")), ("log", lambda: self.add_function("log")), 
            ("sin", lambda: self.add_function("sin")), ("cos", lambda: self.add_function("cos"))
        ]
        
        # Ряд 4 - Научные функции 3
        buttons_row4 = [
            ("tan", lambda: self.add_function("tan")), ("n!", lambda: self.add_function("factorial")), 
            ("π", lambda: self.add_number(str(math.pi))), ("e", lambda: self.add_number(str(math.e)))
        ]
        
        # Ряд 5 - Числа и операции 1
        buttons_row5 = [
            ("(", lambda: self.add_operator("(")), (")", lambda: self.add_operator(")")), 
            ("/", lambda: self.add_operator("/")), ("*", lambda: self.add_operator("*"))
        ]
        
        # Ряд 6 - Числа 7,8,9 и вычитание
        buttons_row6 = [
            ("7", lambda: self.add_number("7")), ("8", lambda: self.add_number("8")), 
            ("9", lambda: self.add_number("9")), ("-", lambda: self.add_operator("-"))
        ]
        
        # Ряд 7 - Числа 4,5,6 и сложение
        buttons_row7 = [
            ("4", lambda: self.add_number("4")), ("5", lambda: self.add_number("5")), 
            ("6", lambda: self.add_number("6")), ("+", lambda: self.add_operator("+"))
        ]
        
        # Ряд 8 - Числа 1,2,3 и равно
        buttons_row8 = [
            ("1", lambda: self.add_number("1")), ("2", lambda: self.add_number("2")), 
            ("3", lambda: self.add_number("3")), ("=", self.calculate)
        ]
        
        # Ряд 9 - 0, точка и равно
        buttons_row9 = [
            ("0", lambda: self.add_number("0")), (".", lambda: self.add_operator(".")), 
            ("", None), ("=", self.calculate)
        ]
        
        all_buttons = [buttons_row1, buttons_row2, buttons_row3, buttons_row4, 
                      buttons_row5, buttons_row6, buttons_row7, buttons_row8, buttons_row9]
        
        for row_idx, row in enumerate(all_buttons):
            for col_idx, (text, command) in enumerate(row):
                if text and command:
                    if text == "=" and row_idx == 8:
                        btn = tk.Button(buttons_frame, text=text, command=command, **button_style)
                        btn.grid(row=row_idx, column=col_idx, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), padx=1, pady=1)
                    else:
                        btn = tk.Button(buttons_frame, text=text, command=command, **button_style)
                        btn.grid(row=row_idx, column=col_idx, sticky=(tk.W, tk.E, tk.N, tk.S), padx=1, pady=1)
        
        # Настройка весов столбцов и строк
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)
        for i in range(9):
            buttons_frame.rowconfigure(i, weight=1)
            
    def add_number(self, number):
        """Добавление числа к выражению"""
        self.current_expression += number
        self.update_display()
        
    def add_operator(self, operator):
        """Добавление оператора к выражению"""
        if operator in ["(", ")"]:
            self.current_expression += operator
        elif operator == ".":
            # Проверяем, что точка не дублируется в текущем числе
            if "." not in self.current_expression.split()[-1] if self.current_expression else True:
                self.current_expression += operator
        else:
            # Добавляем пробелы вокруг операторов для читаемости
            if self.current_expression and not self.current_expression.endswith(" "):
                self.current_expression += " "
            self.current_expression += operator + " "
        self.update_display()
        
    def add_function(self, func_name):
        """Добавление функции к выражению"""
        if func_name in ["square", "cube"]:
            if self.current_expression:
                if func_name == "square":
                    self.current_expression += "**2"
                else:  # cube
                    self.current_expression += "**3"
        else:
            self.current_expression += f"{func_name}("
        self.update_display()
        
    def clear_all(self):
        """Полная очистка"""
        self.current_expression = ""
        self.result_var.set("")
        self.update_display()
        
    def clear_entry(self):
        """Очистка текущего ввода"""
        self.current_expression = ""
        self.update_display()
        
    def backspace(self):
        """Удаление последнего символа"""
        if self.current_expression:
            self.current_expression = self.current_expression[:-1]
            self.update_display()
            
    def toggle_sign(self):
        """Изменение знака числа"""
        if self.current_expression:
            try:
                # Простая реализация: добавляем - в начало или убираем его
                if self.current_expression.startswith("-"):
                    self.current_expression = self.current_expression[1:]
                else:
                    self.current_expression = "-" + self.current_expression
                self.update_display()
            except:
                pass
                
    def update_display(self):
        """Обновление дисплея"""
        self.expression_var.set(self.current_expression)
        
    def calculate(self):
        """Вычисление результата"""
        if not self.current_expression:
            return
            
        try:
            # Подготовка выражения для вычисления
            expression = self.prepare_expression()
            result = eval(expression, self.get_safe_namespace())
            
            # Форматирование результата
            formatted_result = truncate_result(result)
            self.result_var.set(formatted_result)
            
            # Сохраняем результат как новое выражение
            self.current_expression = str(result)
            self.update_display()
            
        except Exception as e:
            error_msg = str(e)
            if isinstance(e, (DivisionByZeroError, InvalidInputError, CalculatorError)):
                error_msg = str(e)
            else:
                error_msg = "Ошибка вычисления"
            
            self.result_var.set(f"Ошибка: {error_msg}")
            messagebox.showerror("Ошибка", error_msg)
            
    def prepare_expression(self):
        """Подготовка выражения для вычисления"""
        expression = self.current_expression
        
        # Замена функций
        replacements = {
            "sqrt(": "square_root(",
            "ln(": "natural_log(",
            "log(": "logarithm(",
            "sin(": f"sine({'degrees_to_radians(' if self.angle_mode.get() == 'degrees' else ''}",
            "cos(": f"cosine({'degrees_to_radians(' if self.angle_mode.get() == 'degrees' else ''}",
            "tan(": f"tangent({'degrees_to_radians(' if self.angle_mode.get() == 'degrees' else ''}",
            "factorial(": "factorial(int("
        }
        
        for old, new in replacements.items():
            expression = expression.replace(old, new)
            
        # Добавляем дополнительные скобки для тригонометрических функций в режиме градусов
        if self.angle_mode.get() == "degrees":
            for func in ["sine", "cosine", "tangent"]:
                if f"{func}(degrees_to_radians(" in expression:
                    # Находим соответствующие скобки и добавляем закрывающую скобку
                    expression = self.fix_trig_brackets(expression, func)
                    
        # Добавляем закрывающую скобку для factorial(int(
        expression = expression.replace("factorial(int(", "factorial(int(") 
        if "factorial(int(" in expression:
            expression = self.fix_factorial_brackets(expression)
            
        return expression
        
    def fix_trig_brackets(self, expression, func_name):
        """Исправление скобок для тригонометрических функций"""
        pattern = f"{func_name}(degrees_to_radians("
        start = 0
        while True:
            pos = expression.find(pattern, start)
            if pos == -1:
                break
                
            # Найти соответствующую закрывающую скобку
            bracket_count = 2  # две открывающие скобки
            i = pos + len(pattern)
            while i < len(expression) and bracket_count > 0:
                if expression[i] == '(':
                    bracket_count += 1
                elif expression[i] == ')':
                    bracket_count -= 1
                i += 1
                
            if bracket_count == 0:
                # Добавить дополнительную закрывающую скобку
                expression = expression[:i] + ')' + expression[i:]
                
            start = pos + 1
            
        return expression
        
    def fix_factorial_brackets(self, expression):
        """Исправление скобок для factorial"""
        pattern = "factorial(int("
        start = 0
        while True:
            pos = expression.find(pattern, start)
            if pos == -1:
                break
                
            # Найти соответствующую закрывающую скобку для int(
            bracket_count = 1
            i = pos + len(pattern)
            while i < len(expression) and bracket_count > 0:
                if expression[i] == '(':
                    bracket_count += 1
                elif expression[i] == ')':
                    bracket_count -= 1
                i += 1
                
            if bracket_count == 0:
                # Добавить дополнительную закрывающую скобку для factorial
                expression = expression[:i] + ')' + expression[i:]
                
            start = pos + 1
            
        return expression
        
    def get_safe_namespace(self):
        """Получение безопасного пространства имен для eval"""
        return {
            # Математические функции из модуля calculator
            'add': add,
            'subtract': subtract,
            'multiply': multiply,
            'divide': divide,
            'power': power,
            'square_root': square_root,
            'natural_log': natural_log,
            'logarithm': logarithm,
            'sine': sine,
            'cosine': cosine,
            'tangent': tangent,
            'factorial': factorial,
            
            # Утилиты из модуля utils
            'degrees_to_radians': degrees_to_radians,
            'radians_to_degrees': radians_to_degrees,
            
            # Математические константы
            'pi': math.pi,
            'e': math.e,
            
            # Встроенные функции Python для математики
            'abs': abs,
            'int': int,
            'float': float,
            'round': round,
            'max': max,
            'min': min,
        }


def run_demo():
    """Демонстрация работы калькулятора с тестовыми сценариями"""
    print("=== ДЕМОНСТРАЦИЯ НАУЧНОГО КАЛЬКУЛЯТОРА ===\n")
    
    # Тестовые сценарии
    test_cases = [
        # Арифметические операции
        ("Арифметические операции", [
            (lambda: add(10, 5), "add(10, 5)"),
            (lambda: subtract(10, 3), "subtract(10, 3)"),
            (lambda: multiply(4, 6), "multiply(4, 6)"),
            (lambda: divide(15, 3), "divide(15, 3)"),
        ]),
        
        # Научные операции
        ("Научные операции", [
            (lambda: power(2, 3), "power(2, 3)"),
            (lambda: square_root(16), "square_root(16)"),
            (lambda: natural_log(math.e), "natural_log(e)"),
            (lambda: logarithm(100, 10), "logarithm(100, 10)"),
            (lambda: factorial(5), "factorial(5)"),
        ]),
        
        # Тригонометрические функции
        ("Тригонометрические функции", [
            (lambda: sine(degrees_to_radians(30)), "sin(30°)"),
            (lambda: cosine(degrees_to_radians(60)), "cos(60°)"),
            (lambda: tangent(degrees_to_radians(45)), "tan(45°)"),
            (lambda: sine(math.pi/2), "sin(π/2)"),
        ]),
        
        # Примеры с ошибками
        ("Обработка ошибок", [
            (lambda: divide(10, 0), "divide(10, 0)"),
            (lambda: square_root(-4), "square_root(-4)"),
            (lambda: natural_log(-5), "natural_log(-5)"),
            (lambda: factorial(-3), "factorial(-3)"),
        ]),
    ]
    
    for section_name, tests in test_cases:
        print(f"--- {section_name} ---")
        for test_func, description in tests:
            try:
                result = test_func()
                formatted_result = truncate_result(result)
                print(f"✓ {description} = {formatted_result}")
            except Exception as e:
                print(f"✗ {description} = ОШИБКА: {e}")
        print()


def main():
    """Главная функция"""
    print("Запуск научного калькулятора...")
    
    # Сначала запускаем демонстрацию
    run_demo()
    
    # Затем запускаем GUI
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    
    # Центрирование окна
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()