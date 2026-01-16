def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль")
    else:
        return a / b

def power(base, exponent):
   
    return base ** exponent

print("=== Возведение числа в степень ===")

try:

    base = float(input("Введите число (основание): "))
    
    
    exponent = float(input("Введите степень: "))
    
    
    result = power(base, exponent)
    
    
    print(f"\nРезультат: {base} в степени {exponent} = {result}")
    
    
    if exponent == 0:
        print("Любое число в степени 0 равно 1")
    elif exponent == 1:
        print("Любое число в степени 1 равно самому себе")
    elif exponent == 2:
        print(f"Квадрат числа {base} = {result}")
    elif exponent == 0.5 or exponent == 1/2:
        print(f"Квадратный корень из {base} = {result}")
    elif exponent < 0:
        print(f"Обратная величина: 1/({base}^{abs(exponent)})")

except ValueError:
    print("Ошибка: пожалуйста, вводите только числа!")
except ZeroDivisionError:
    print("Ошибка: нельзя возвести 0 в отрицательную степень!")
except Exception as e:
    print(f"Произошла ошибка: {e}")