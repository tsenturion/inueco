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