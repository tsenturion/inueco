#Операторы
print(6-(-81))
#Коммутативная операция
print(3**5)
print((-8)/(-4))
#Композиция операций
print(8/2+5-(-3)/2)
#Приоритет
print(70*(3+4)/(8+2))
#Числа с плавающей точкой
print(0.39*0.22)
#Линтер
print( (5 **2)-(3* 7))
#Кавычки
print('"Khal Drogo\'s favorite word is "athjahakar""')
#Экранированные последовательности
print("- Did Joffrey agree?\n- He did. He also said \"I love using \\n\".")
#Конкатенация
print('Winter' + ' ' + 'came' + ' ' + 'for' + ' ' + 'the' + ' ' + 'House' + ' ' + 'of' + ' ' + 'Frey.')
#Кодировка
print(chr(126))
print(chr(94))
print(chr(37))
#Что такое переменная
motto = 'What Is Dead May Never Die!'
print(motto)
#Изменение переменной
name = "Brienna"

# BEGIN (write your solution here)
name = name[::-1]
# END

print(name)
#Выбор имени переменной 
brothers_count = 2
print(brothers_count)
#Выражения в определениях
euros_count = 100  # Исходное количество евро

# BEGIN (write your solution here)
dollars_count = euros_count * 1.25
print(dollars_count)

yuans_count = dollars_count * 6.91
print(yuans_count)
# END
#Переменные и конкатенация
first_name = 'Joffrey'
greeting = 'Hello'
info = 'Here is important information about your account security.'
intro = 'We couldn\'t verify your mother\'s maiden name.'

# BEGIN (write your solution here)
print(greeting + ', ' + first_name + '!')
print(info + '\n' + intro)
# END
#Именование переменных 
first_number = 20
second_number = -100
print(first_number * second_number)
#Магические числа
king = "Rooms in King Balon's Castles:"
print(king)

# BEGIN (write your solution here)
rooms_per_castle = 6
castles_count = 17
total_rooms = rooms_per_castle * castles_count
print(total_rooms)
# END
# Константы
DRAGONS_BORN_COUNT = 3
#Интерполяция
stark = 'Arya'

# BEGIN (write your solution here)
print(f'Do you want to eat, {stark}?')
# END

#Яндекс Python 

# Ввод и вывод данных. Операции с числами, строками. Форматирование 2.1

#Привет, Яндекс!
print("Привет, Яндекс!")
#Привет, всем!
name = input()
print("Как Вас зовут?")
print(f"Привет, {name}")
#Излишняя автоматизация 
text = input()
print(text)
print(text)
print(text)
#Сдача
bill = int(input())
price_per_kg = 38
weight = 2.5
cost = price_per_kg * weight
change = bill - int(cost)  # Преобразуем в int, так как ответ должен быть натуральным числом
print(change)
#Магазин
price = int(input())
weight = int(input())
money = int(input())

cost = price * weight
change = money - cost

print(change)
#Чек
product = input()
price = int(input())
weight = int(input())
money = int(input())

total_cost = price * weight
change = money - total_cost

print("Чек")
print(f"{product} - {weight}кг - {price}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")
#Делу — время, потехе — час
n = int(input())

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

