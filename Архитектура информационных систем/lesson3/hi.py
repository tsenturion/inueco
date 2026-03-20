# Просим пользователя ввести количество чисел
count = int(input("Сколько чисел хотите ввести? "))

total = 0

# Цикл для ввода чисел и подсчёта суммы
for i in range(count):
    num = float(input(f"Введите число {i + 1}: "))
    total += num

# Вычисляем среднее значение, если count > 0
if count > 0:
    average = total / count
    print(f"Сумма введённых чисел: {total}")
    print(f"Среднее значение: {average}")
else:
    print("Вы не ввели ни одного числа.")