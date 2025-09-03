a = int(input("Первое число: "))
b = int(input("Второе число: "))

op = input("Операция (+, -, *, /): ")

if op == '+':
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b
else:
    result = "Неизвестная операция"

print("Результат:", result)
print("Тип результата:", type(result))

