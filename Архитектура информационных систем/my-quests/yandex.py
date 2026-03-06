#1
print("Привет, Яндекс!")

#2
a = input("Как Вас зовут?\n")
print("Привет,", a)

#3
a = input()
for i in range(3):
    print(a)

#4
a = int(input())
b = 38 * 5 // 2
c = (a-b)
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
f = b * c
g = d - f
print(f"Чек\n{a} - {c}кг - {b}руб/кг\nИтого: {f}руб\nВнесено: {d}руб\nСдача: {g}руб")

#7
n = int(input())
print("Купи слона!\n" * n, end='')

#8
count = int(input())
words = input()
print(f'Я больше никогда не буду писать "{words}"!\n' * count, end='')

#9
a = int(input())
b = int(input())
print((a * b) // 2)

#10
name = input()
shelf = int(input())
print("Группа №" + str(shelf // 100) + '.')
print(str(shelf % 10) + '.', name + '.')
print("Шкафчик:", str(shelf)+ '.')
print('Кроватка:', str(shelf // 10 % 10) + '.')

#11
one = int(input())
a = str(one // 1000)
b = str(one // 100 % 10)
c = str(one // 10 % 10)
d = str(one % 10)
print(int(b + a + d + c))

#12
a = int(input())
b = int(input())
c = (a % 10 + b % 10) % 10
d = (a // 10 % 10 + b // 10 % 10) % 10
f = (a // 100 % 10 + b // 100 % 10) % 10
print(f * 100 + d * 10 + c)


#13
a = int(input())
b = int(input())
print(b // a)
print(b % a)

#14
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#15
n = int(input())
m = int(input())
t = int(input())
tm = n * 60 + m + t
fm = tm % 60
fn = (tm // 60) % 24
print(f"{fn:02}:{fm:02}")

#16
a = int(input())
b = int(input())
c = int(input())
print(round(abs(a - b) / c, 2))

#17
a = int(input())
b = input()
c = int(b, 2)
result = a + c
print(result)

#18
a = int(input(),2)
b = int(input())
print(a - b)

#19
a = input()
b = int(input())
c = int(input())
d = int(input())
t = b * c
ch = d - t
ps = f"{c}кг * {b}руб/кг"

print(f"{'Чек':=^35}")
print(f"Товар:{a:>29}")
print(f"Цена:{ps:>30}")
print(f"Итого:{t:>26}руб")
print(f"Внесено:{d:>24}руб")
print(f"Сдача:{ch:>26}руб")
print("=" * 35)

#20
n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())
x = (n * (m - k2)) // (k1 - k2)
y = n - x

print(x, y)

#21
print("Как Вас зовут?")
a = input()
print("Здравствуйте,", a + "!")
print("Как дела?")
b = input()
if b == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")

#22
