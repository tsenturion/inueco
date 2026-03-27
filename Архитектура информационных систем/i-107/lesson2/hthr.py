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
red = int(input())
green = int(input())
blue = int(input())
print(red + blue + 1)

#15
n = int(input())
m = int(input())
t = int(input())

total_minutes = (n * 60 + m + t) % (24 * 60)

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{hours:02}:{minutes:02}")






#STREPIK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 1 
print("Здравствуй, мир!")
# 2
print(4, 8, 15, 16, 23, 42)
# 3
print(4)
print(8)
print(15)
print(16)
print(23)
print(42)
# 4
n = 7
for i in range(1, n + 1):
    print('*' * i)
# 5
name = input()
print(f"Привет, {name}")
# 6
team_name = input()
print(team_name + ' - чемпион!')
# 7
line1 = input()
line2 = input()
line3 = input()
print(line1)
print(line2)
print(line3)
# 8
line1 = input()
line2 = input()
line3 = input()
print(line3)
print(line2)
print(line1)
# 9
print('I', '*'*3, 'like', '*'*3, 'Python', sep='')
# 10
username = input()
print(f"Привет, {username}!")
# 11
separator = input()
first_string = input()
second_string = input()
third_string = input()
print(first_string, second_string, third_string, sep=separator)
# 12
number = int(input())
print(number)
print(number + 1)
print(number + 2)
# 13
a = int(input())
b = int(input())
c = int(input())
summa = a + b + c
print(summa)
# 14
monitor_price = int(input())
system_unit_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())
computer_cost = monitor_price + system_unit_price + keyboard_price + mouse_price
total_cost = computer_cost * 3
print(total_cost)
# 15
a = int(input())
b = int(input())
sum_ab = a + b    
cube_sum_ab = sum_ab * sum_ab * sum_ab 
square_b = b * b   
result = 3 * cube_sum_ab + 275 * square_b - 127 * a - 41
print(result)
# 16
num = int(input())
next_num = num + 1
prev_num = num - 1
print(f"Следующее за числом {num} число: {next_num}")
print(f"Для числа {num} предыдущее число: {prev_num}")
# 17
a = int(input())
volume = a * a * a
surface_area = 6 * a * a
print("Объем =", volume)
print("Площадь полной поверхности =", surface_area)
# 18
a = int(input())
b = int(input())
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
print(f"{a} + {b} = {sum_ab}")
print(f"{a} - {b} = {diff_ab}")
print(f"{a} * {b} = {prod_ab}")
# 19
a1 = int(input())
d = int(input())  
n = int(input()) 
an = a1 + d * (n - 1)
print(an)
# 20
x = int(input())
sequence = [i * x for i in range(1, 6)]
result = '---'.join(map(str, sequence))
print(result)
# 21
b1 = int(input()) 
q = int(input()) 
n = int(input()) 
bn = b1 * (q ** (n - 1))
print(bn)
# 22
cm = int(input())
meters = cm // 100
print(meters)
# 23
n = int(input())
k = int(input())
mandarins_per_student = k // n
remaining_mandarins = k % n
print(mandarins_per_student)
print(remaining_mandarins)
# 24
population = int(input())
survivors = population // 2 + (population % 2)
print(survivors)
# 25
minutes = int(input())
hours = minutes // 60  
remainder_minutes = minutes % 60 
if hours > 0 and remainder_minutes > 0:
    print(f'{minutes} мин - это {hours} час {remainder_minutes} минут.')
elif hours > 0 and remainder_minutes == 0:
    print(f'{minutes} мин - это {hours} час 0 минут.')
else:
    print(f'{minutes} мин - это 0 час {remainder_minutes} минут.')
# 26
place_number = int(input())
coupe_number = (place_number + 3) // 4
print(coupe_number)
# 27
number = int(input())
hundreds = number // 100      
tens = (number // 10) % 10  
units = number % 10            
digit_sum = hundreds + tens + units
digit_product = hundreds * tens * units
print(f"Сумма цифр = {digit_sum}")
print(f"Произведение цифр = {digit_product}")
# 28
number = input()
a = number[0]
b = number[1]
c = number[2]
print(a+b+c)
print(a+c+b)
print(b+a+c)
print(b+c+a)
print(c+a+b)
print(c+b+a)
# 29
number = int(input())
thousands = number // 1000         
hundreds = (number // 100) % 10  
tens = (number // 10) % 10    
units = number % 10           
print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции десятков равна {tens}")
print(f"Цифра в позиции единиц равна {units}")
# 30
password1 = input()
password2 = input()
if password1 == password2:
    print("Пароль принят")
else:
    print("Пароль не принят")
# 31
age = int(input())
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
# 32
first_number = int(input())
second_number = int(input())
min_value = min(first_number, second_number)
print(min_value)
# 33
a = int(input())
b = int(input())
c = int(input())
if b - a == c - b:
    print("YES")
else:
    print("NO")
# 34
n = int(input())

a = n // 1000 
b = (n % 1000) // 100 
c = (n % 100) // 10
d = n % 10 
if a + d == b - c:
    print('ДА')
else:
    print('НЕТ')
# 35
num1 = int(input())
num2 = int(input())
num3 = int(input())
sum_positive = 0
if num1 > 0:
    sum_positive += num1
if num2 > 0:
    sum_positive += num2
if num3 > 0:
    sum_positive += num3
print(sum_positive)
# 36
age = int(input())
if age <= 13:
    group = 'детство'
elif 14 <= age <= 24:
    group = 'молодость'
elif 25 <= age <= 59:
    group = 'зрелость'
else:
    group = 'старость'
print(group)
# 37
a = int(input())
b = int(input())
c = int(input())
d = int(input())
minimum_value = min(a, b, c, d)
print(minimum_value)
# 38
x = int(input())
if -1<x<17:
    print("Принадлежит")
else:
    print("Не принадлежит")
# 39
x = int(input())
if x <= -3 or x >= 7:
    print("Принадлежит")
else:
    print("Не принадлежит")
# 40
x = int(input())
if (-30 < x <= -2) or (7 < x <= 25):
    print("Принадлежит")
else:
    print("Не принадлежит")
# 41
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
# 42
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
# 43
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
# 44
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")
# 45 
def string_or_not(value):
    if isinstance(value, str):
        return 'yes'
    return 'no'
# 46
def normalize_url(url):
    """
    Приводит адрес сайта к нормализованному виду с https:// в начале.
    
    Args:
        url: Адрес сайта (может быть без протокола, с http:// или https://)
        
    Returns:
        str: Адрес сайта с https:// в начале
    """
    # Проверяем, начинается ли адрес с http://
    if url[:7] == 'http://':
        # Если да, заменяем http:// на https://
        return 'https://' + url[7:]
    # Проверяем, начинается ли адрес с https://
    elif url[:8] == 'https://':
        # Если адрес уже нормализован, возвращаем его без изменений
        return url
    else:
        # Если протокол не указан, добавляем https:// в начало
        return 'https://' + url
# Тестирование функции
print(normalize_url('https://ya.ru'))  # => 'https://ya.ru'
print(normalize_url('google.com'))     # => 'https://google.com'
print(normalize_url('http://ai.fi'))   # => 'https://ai.fi'
print(normalize_url('http://example.com'))  # => 'https://example.com'
print(normalize_url('example.org'))         # => 'https://example.org'
