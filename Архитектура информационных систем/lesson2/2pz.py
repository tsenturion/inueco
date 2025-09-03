# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
number = int 
print(number)
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
message = ''' Выберете математическую операцию:

+ : Сложение
- : Вычитание
/ : Деление
* : Умножение

Ваш выбор:
'''
operation = input(message)
if operation == '+':
    print('Сложение')
    result = num1 + num2
elif operation == '-':
    print('Вычитание')
    result = num1 - num2
elif operation == '/':
    print('Деление')
    result = num1 / num2
elif operation == '*':
    print('Умножение')
    result = num1 * num2
else:
    print('Неизвестная операция')


print("Результат:", result)