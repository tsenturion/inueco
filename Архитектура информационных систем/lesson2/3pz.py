<<<<<<< HEAD
# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
# 5. Повторять все заново с использованием while
# 6. Завершить программу если пользователь введет 'exit'
def custom_input(is_operation: bool = None):
    if is_operation:
        operation = input("Введите операцию: ")
        if operation != "exit":
            return operation
    
    number = input("Введите число: ")
    if number != "exit":
        return int(number)
    raise Exception("exit")

while True:
    try:
        n1 = custom_input()
        n2 = custom_input()
        operation = custom_input(True)
        if operation == "+":
            print(n1 + n2)
        elif operation == "-":
            print(n1 - n2)
        elif operation == "*":
            print(n1 * n2)
        elif operation == '/':
            print(n1 / n2)
        else:
            raise Exception('invalid operation')

    except Exception as e:
        print(e)
        break
=======
while (1):
    num1 = int(input("Введите первое число:"))
    num2 = int(input("Введите второе число:"))
    oper = input("Введите оперецию (+ - * / ** // % exit):")
    if (oper == "exit"):
        print("Выход из системы")
        break
    else:
        match oper:
            case "+":
                fin = num1 + num2
            case "-":
                fin = num1 - num2
            case "*":
                fin = num1 * num2
            case "/":
                if (num2 == 0):
                    print("нельзя делить на 0")
                    continue
                else:
                    fin = num1 / num2
            case "**":
                fin = num1 ** num2
            case "//":
                fin = num1 // num2
            case "%":
                fin = num1 % num2
            case _:
                print("не известная команда")
                continue
        print(f"Результат: {fin}")
        print(f"Тип данных: {type(fin)}")
>>>>>>> ee9f5f84db47acea417509ae078d67e1e17e0541
