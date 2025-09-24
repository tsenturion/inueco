# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип

print("Welcome to calculator")
number_1 = int(input("Введите число:     ")) 
oper = input("ВВедите оператор:     ")
number_2 = int(input("Введите число:    ")) 

if oper == '-':
    res = number_1 - number_2
elif oper == '+':
    res = number_1 + number_2
elif oper == '*':
    res = number_1 * number_2
elif oper == '/':
    res = number_1 / number_2
else: 
    res = 0
    print("Неизвестный оператор")
    exit()

print("Результат: " + str(res))
print(type(res))
