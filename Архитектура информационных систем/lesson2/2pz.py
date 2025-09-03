# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип

a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))

operation = input("Введите операцию (+, -, *, /): ")

result = None

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        print("Ошибка: деление на ноль!")
        result = None
else:
    print("Ошибка: неизвестная операция!")
    result = None

if result is not None:
    print(f"Резудьтат: {result}")
    print(f"Тип результата: {type(result)}")