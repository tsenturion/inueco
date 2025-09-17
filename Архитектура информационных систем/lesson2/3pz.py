# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
# 5. Повторять все заново с использованием while
# 6. Завершить программу если пользователь введет 'exit'
while True:
    try:
        input1 = input("Введите первое число (или 'exit' для выхода): ")
        if input1.lower() == 'exit':
            print("Программа завершена.")
            break
        num1 = float(input1)
        
        input2 = input("Введите второе число: ")
        if input2.lower() == 'exit':
            print("Программа завершена.")
            break
        num2 = float(input2)
        
        operation = input("Введите операцию (+, -, *, /): ")
        if operation.lower() == 'exit':
            print("Программа завершена.")
            break
        
        result = None
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Ошибка: деление на ноль!")
                continue
            result = num1 / num2
        else:
            print("Ошибка: неизвестная операция! Используйте +, -, *, /")
            continue
        
        print(f"Результат: {result}")
        print(f"Тип результата: {type(result)}")
        print("-" * 30)
        
    except ValueError:
        print("Ошибка: введите корректное число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")