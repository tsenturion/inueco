# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
x = int(input("введите первое число: "))
y = int(input("введите второе число: "))
math_operation = input('введите математическое действие(+ - * /): ')
if math_operation == "+":
    result = x + y
    print(result, type(result))
elif math_operation == "-":
    result = x - y
    print(result, type(result))
elif math_operation == "*":
    result = x * y
    print(result, type(result))
elif math_operation == "/":
    result = x / y
    print(result, type(result))
else:
    print("ошибка: операция не распознана")