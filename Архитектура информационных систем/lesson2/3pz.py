# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
# 5. Повторять все заново с использованием while
# 6. Завершить программу если пользователь введет 'exit'

while True:
    print("Используй exit для выхода! ")
    number1_input = input("Введите первое число: ")
    
    if number1_input == "exit":
        break

    number2_input = input("Введите второе число: ")

    if number2_input == "exit":
        break

    result: int = 0

    
    number1: int = int(number1_input)
    number2: int = int(number2_input)

    print("Доступные операции: +, -, /")

    operation = input("Операция: ")

    match operation:
        case '+':
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
        case "/":
            if (number2 != 0):
                result = number1 / number2
        
            else:
                print("Делить на ноль нельзя!")
                continue

        case _:
            print("Я не знаю такой операции")
            continue
        
    print(f"Результат: {result} тип данных: {type(result)}")