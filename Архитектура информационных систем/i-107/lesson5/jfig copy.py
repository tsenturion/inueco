#1
print("Привет, Яндекс!")

#2
a = input("Как Вас зовут?\n")
print("Привет,", a)
#3
a = input()
print(a)
print(a)
print(a)
#4
a = int(input())
b = 38 * 5 // 2
c = (a - b)
print(c)
#5
a = int(input())
b = int(input())
c = int(input())
print(c - (a * b))
#6

a = input()
b = int(input())
c = int(input())
d = int(input())
total = b * c
change = d - total
print("Чек")
print(f"{a} - {c}кг - {b}руб/кг")
print(f"Итого: {total}руб")
print(f"Внесено: {d}руб")
print(f"Сдача: {change}руб")
#7
n = int(input())
for i in range(n):
    print("Купи слона!")