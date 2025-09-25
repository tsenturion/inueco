# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип
# 5. Повторять все заново с использованием while
# 6. Завершить программу если пользователь введет 'exit'
<<<<<<< HEAD
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
=======
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
>>>>>>> 4a72d194ee8f8843c8c56d34c386b527a3a24cae
