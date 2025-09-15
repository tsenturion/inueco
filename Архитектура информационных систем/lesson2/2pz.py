# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
try:
    number1 = float(input("Введите первое число: "))
    number2 = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка! Пожалуйста, вводите только числа.")
    exit(1)

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

n1 = int(input("Введи первое число: "))
n2 = int(input("Введи второе число: "))
operation = input("Какую операцию хочешь выполнить? [+, -, *, /]: ")

if operation in ['+', '-', '*', '/']:
    if operation == "+":
        answer = n1 + n2
    elif operation == "-":
        answer = n1 - n2
    elif operation == "*":
        answer = n1 * n2
    elif operation == "/":
        if n2 == 0:
            answer = 0
        else:
            answer = n1 / n2
    print(answer)
    print(type(answer))
else:
    print(">> [ОШИБКА] Указана некорректная операция")

    num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))

op = input("Введите операцию (+, -, *, /): ")

result = None

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Ошибка: деление на ноль!")
else:
    print("Ошибка: неизвестная операция!")

if result is not None:
    print(f"Резудьтат: {result}")
    print(f"Тип результата: {type(result)}")
else:
    print('Ошибка!')