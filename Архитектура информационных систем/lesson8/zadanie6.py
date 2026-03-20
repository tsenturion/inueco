print(f'Do you want to eat, {stark}?')
# END

#Яндекс Python 2.1
#Яндекс Python 

# Ввод и вывод данных. Операции с числами, строками. Форматирование 2.1

#Привет, Яндекс!
print("Привет, Яндекс!")

for i in range(n):
    print("Купи слона!")
#Наказание
n = int(input())
punishment_text = input()

for i in range(n):
    print(f'Я больше никогда не буду писать "{punishment_text}"!')
#Деловая колбаса
n = int(input())
m = int(input())

print(n * m // 2)
#Детский сад — штаны на лямках
name = input()
locker = input()

group = locker[0]
number_in_list = locker[2]
bed = locker[1]

print(f"Группа №{group}.")
print(f"{number_in_list}. {name}.")
print(f"Шкафчик: {locker}.")
print(f"Кроватка: {bed}.")
#Автоматизация игры
num = input()
print(num[1] + num[0] + num[3] + num[2])
#Интересное сложение
a = input().zfill(3)
b = input().zfill(3)

res = ''
for i in range(3):
    res += str((int(a[i]) + int(b[i])) % 10)

print(int(res))
#Дед Мороз и конфеты
n = int(input())
m = int(input())

print(m // n)
print(m % n)
#Шарики и ручки
red = int(input())
green = int(input())
blue = int(input())

print(red + blue + 1)