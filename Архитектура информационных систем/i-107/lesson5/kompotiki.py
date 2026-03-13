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

#Яндекс
#1 ссылка

#1
print('Hello, World!')
#2
# You know nothing, Jon Snow!
#3
print('Robert')
print('Stannis')
print('Renly')
#4
print('10')
#5
print('What Is Dead May Never Die')
#6
print(81/9)
#7
a = 6
b = -81
print(a - b)
#8
print(3**5)
print(-8/-4)
#9
a = (8/2 + 5)
b = (-3/2)
print(a-b)
#10
print(70 *(3 + 4) / (8+2))
#11
print(0.39 * 0.22)
#12
print((5 ** 2) - (3 * 7))
#13
print('"Khal Drogo\'s favorite word is "athjahakar""')

#14
print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

#15
print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

#16
print(chr(126))
print(chr(94))
print(chr(37))

#17
motto = 'What Is Dead May Never Die!'
print(motto)

#18
name = "Brienna"

# BEGIN (write your solution here)
name = "anneirB"
# END


print(name)

#19
brothers = 2
print(brothers)

#20
euros_count = 100
# BEGIN (write your solution here)
dollars_count= euros_count* 1.25
yuans_count = dollars_count * 6.91
print(dollars_count)
print(yuans_count)
# END

#21
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = "Joffrey"
greeting = "Hello"

# BEGIN (write your solution here)
print(greeting + "," + " " + first_name + "!")
print(intro + "\n" + info)
# END


#22
first_number = 20
second_number = -100

cifra = first_number * second_number
print(cifra)
#23
king = "Rooms in King Balon's Castles:"

# BEGIN (write your solution here)
print(king + "\n" + "102")
# END

#24
DRAGONS_BORN_COUNT = 3

#25
stark = 'Arya'
print(f'Do you want to eat, {stark}?')
# Output: Do you want to eat, Arya?
#END




