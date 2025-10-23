print("Введите первое число")
a = int(input())
print("Введите второе число")
b = int(input())
print("Введите знак (+, -, *, /)")
c = input()
if (c == "+"):
    d = a + b
elif (c == "-"):
    d = a - b
elif (c == "*"):
    d = a * b 
elif (c == "/"):
    d = a / b
else:
    print("Вы что-то сделали не правильно")
print("Результат", d)
print("Тип результата", type(d))