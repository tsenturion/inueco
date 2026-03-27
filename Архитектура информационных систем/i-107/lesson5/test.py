#Тараканов Никита группа И-107

# 1 Привет, Мир
print('Hello, World!')

# 2 Комментарии
# You know nothing, Jon Snow!

# 3 Инструкции (Statements)
print('Robert')
print('Stannis')
print('Renly')

# 4 Как мы проверяем ваши решения
print(10)

# 5 Синтаксические ошибки
print('What Is Dead May Never Die')

# 6 Арифметические операции
print(81 / 9)

# 7 Оператор
print (6 + 81)

#8 Коммуникативная операция
print (3**5)
print (-8 / -4)

#9 Композиция операций
print ( 8/2+5--3/2)

#10 Приоритет
print (70*(3+4)/(8+2))

# 11  Числа с плавающей точкой
print (0.39*0.22)

#12 Линтер
print ((5 ** 2) - (3 * 7))

#13 Кавычки
print ('"Khal Drogo\'s favorite word is "athjahakar""')

#14 Экранированные последовательности
print ('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

# 15 Конкатенация
print ('Winter ' + "came " + "for " + " the " "House " + "of " + "Frey.")

# 16 Кодировка
print(chr(126))
print(chr(94))
print(chr(37))

#17 Что такое переменная
motto = 'What Is Dead May Never Die!'
print (motto)

#18 Изменение переменной
name = "Brienna"

# BEGIN (write your solution here)
name = "anneirB"
# END

print(name)

# 19 Выбор имени переменной
brothers = 2
print(brothers)

#20 Выражения в определениях
euros_count = 100
# BEGIN (write your solution here)
dollars_count = euros_count * 1.25
yuans_count = dollars_count * 6.91
print(dollars_count)
print(yuans_count)
# END

#21 Переменные и конкатенация
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = "Joffrey"
greeting = "Hello"

# BEGIN (write your solution here)
print(greeting + "," + " " + first_name + "!")
print(intro + "\n" + info)
# END

#22 Именование переменных
first_number = 20
second_number = -100

cifra = first_number * second_number
print(cifra)

#23 Магические числа
king = "Rooms in King Balon's Castles:"

# BEGIN (write your solution here)
print(king + "\n" + "102")
# END

#24 Константы
DRAGONS_BORN_COUNT = 3

#25 Интерполяция
stark = "Arya?"

# BEGIN (write your solution here)
print(f'Do you want to eat, {stark}')
# END

#26 Извлечение символов из строки
name = "Na\nharis"

# BEGIN (write your solution here)
print(name[7])
# END

#27 Срезы строк
value = "Hexlet"

# BEGIN (write your solution here)
print(value[2:5])
# END

#28 Multi-line строки
# BEGIN (write your solution here)
text = ''' Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground.'''
# END

print(text)

#29 Типы данных
print (-0.304)

#30 Сильная (или Строгая) типизация
print (7 - (-8 - -2))

#31 Неизменяемость примитивных типов
one = "\nNaharis"
two = "\nMormont"
three = "\nSand"

# BEGIN (write your solution here)
print (one[3] + two[2] + three[4] + two[5] + two[3])
# END

#32 Явное преобразование типов
value = 2.9

# BEGIN (write your solution here)
value = 2.9 - 0.9
a= int(value)
print(str(a) + " times")
# END

#33 Функции и их вызов
company1 = "Apple"
company2 = "Samsung"

# BEGIN (write your solution here)
print (len(company1 + company2))
# END

#34 Параметры по умолчанию
number = 10.1234

# BEGIN (write your solution here)
result= round(number, 2)
print (result)
# END

#35 Вызов функции — выражение
text = "Never forget what you are, for surely the world will not"

# BEGIN (write your solution here)
result = f'First: {text[0]}\nLast: {text[-1]}'
print (result)
# END

#36 Функции с переменным числом параметров
# BEGIN (write your solution here)
print (min(3,10,22,-3,0))
# END

#37 Детерминированность
# imports are studied on Hexlet
from random import random

# BEGIN (write your solution here)
print(round(random()*10))
# END

#38 Объекты
text = "a MIND needs Books as a Sword needS a WHETSTONE."

# BEGIN (write your solution here)
print (text.lower())
# END

#39 Неизменяемость
first_name = "  Grigor   \n"

# BEGIN (write your solution here)
print(first_name.strip())
# END

#40 Цепочка вызовов
text = "When \t\n you play a \t\n game of thrones you win or you die."

# BEGIN (write your solution here)
print(len(text[6:15].strip()))
# END

#41 Создание (определение) функций
def print_motto():
    motto= 'Winter is coming'
    print(motto)

#42 Возврат значений
def truncate(text, length):
    # BEGIN (write your solution here)
    result=f"{text[0:length]}..."
    return(result)
    # END

#43 Именованные аргументы
def trim_and_repeat (text, offset=0, repetitions=1):
    return text[offset:] * repetitions

#44
