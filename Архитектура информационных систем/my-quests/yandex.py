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
a = int(input())
b = int(input())
print((a * b) // 2)

#9
name = input()
shelf = int(input())
print("Группа №" + str(shelf // 100) + '.')
print(str(shelf % 10) + '.', name + '.')
print("Шкафчик:", str(shelf)+ '.')
print('Кроватка:', str(shelf // 10 % 10) + '.')

#10
one = int(input())
a = str(one // 1000)
b = str(one // 100 % 10)
c = str(one // 10 % 10)
d = str(one % 10)
print(int(b + a + d + c))

#11
a = int(input())
b = int(input())
c = (a % 10 + b % 10) % 10
d = (a // 10 % 10 + b // 10 % 10) % 10
f = (a // 100 % 10 + b // 100 % 10) % 10
print(f * 100 + d * 10 + c)


#12
a = int(input())
b = int(input())
print(b // a)
print(b % a)

#13
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#14
