# 1. Запросите два числа
# 2. Запросите операцию (+, -, *, /)
# 3. Используя if/elif/else, выполните нужную операцию
# 4. Выведите результат и его тип

nu1 = int(input( ))
nu2 = int(input( ))

oper = str(input("Операция + - * /" ))

if oper == "+":
    answ = nu1 + nu2
elif oper == "-":
    answ = nu1 - nu2
elif oper == "*":
    answ = nu1 * nu2
elif oper == "/":
    answ = nu1 / nu2
else: 
    print("ERROR: WRONG SYNT.")
print(answ)
print(type(answ))     