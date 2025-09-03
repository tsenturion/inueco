p = int(input("Введите первое число: "))
s = int(input("Введите второе число: "))

operation = input("Введите операцию (+,-,*,/): ")

if operation =='+':
    result = p + s
elif operation == '-':
    result = p - s
elif operation == '*':
    result = p * s
elif operation == '/':
    result = p / s
else:
    result = "Неизвестная операция"

print("Результат:", result)
print("Тип результата:", type (result))