number1 = int(input())
number2 = int(input())

operation = input()

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
        print("Делить на 0 нельзя")

print("Результат:", result)
print("Тип результата:", type(result))