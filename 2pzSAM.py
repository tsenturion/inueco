# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип

num1 = int(input( ))
num2 = int(input( ))

oper = str(input("Операция + - * /" ))

if oper == "+":
    answ = num1 + num2
elif oper == "-":
    answ = num1 - num2
elif oper == "*":
    answ = num1 * num2
elif oper == "/":
    answ = num1 / num2
else: 
    answ = "ERROR"
print(answ)
print(type(answ))     