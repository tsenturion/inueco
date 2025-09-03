# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип20





try:
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка! Пожалуйста, вводите только числа.")
    exit()

operation = input("Введите операцию (+, -, *, /): ")

result = None

if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        print("Ошибка! Деление на ноль нельзя.")
        exit()
else:
    print("Ошибка! Невозможная операция.")
    exit()

print(f"\nРезультат: {result}")
print(f"Тип результата: {type(result)}")
