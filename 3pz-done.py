def read_number(prompt: str):
    while True:
        s = input(prompt).strip()
        if s.lower() == 'exit':
            return None
        try:
            # Пробуем целое, затем float
            if '.' in s or 'e' in s.lower():
                val = float(s)
            else:
                val = int(s)
            return val
        except ValueError:
            print("Ошибка: введите число или 'exit' для выхода.")

def perform_operation(a, b, op: str):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if (isinstance(b, (int, float)) and b == 0):
            print("Ошибка: деление на ноль.")
            return None
        return a / b
    else:
        print("Ошибка: неизвестная операция. Используйте +, -, *, /.")
        return None

def main():
    print("Калькулятор. Введите 'exit' в любом запросе, чтобы завершить программу.")
    while True:
        a = read_number("Введите первое число (или 'exit' для выхода): ")
        if a is None:
            print("Выходим из программы.")
            break

        b = read_number("Введите второе число (или 'exit' для выхода): ")
        if b is None:
            print("Выходим из программы.")
            break

        op = input("Введите операцию (+, -, *, /): ").strip()
        if op.lower() == 'exit':
            print("Выходим из программы.")
            break

        result = perform_operation(a, b, op)
        if result is None:
            # ошибка в операции, повторяем цикл
            continue

        # Определяем тип результата
        result_type = type(result).__name__

        print(f"Результат: {result} (тип: {result_type})")

if __name__ == "__main__":
    main()