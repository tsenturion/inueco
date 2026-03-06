#Яндекс Python 2.1
#A
print("Привет, Яндекс!")
#B
name = input()
print("Как Вас зовут?")
print("Привет, " + name)
#C
text = input()
for i in range(3):
    print(text)
#D
a = int(input())
b = 2.5 * 38
c = a - b
print(int(c))
#E
price_per_unit = int(input())
weight = int(input())
money = int(input())
total_cost = price_per_unit * weight
change = money - total_cost
print(change)
#F
product = input()          
price_per_kg = int(input()) 
weight = int(input())       
money = int(input())        
total_cost = price_per_kg * weight  
change = money - total_cost         
print("Чек")
print(f"{product} - {weight}кг - {price_per_kg}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money}руб")
print(f"Сдача: {change}руб")
#G
n = int(input())
for i in range(n):
    print("Купи слона!")
#H
n = int(input())
punishment = input()
for i in range(n):
    print(f'Я больше никогда не буду писать "{punishment}"!')
#I
n = int(input())
m = int(input())
result = (n * m) // 2
print(result)
#J
name = input()
locker_number = input()  
group = locker_number[0]      
child_number = locker_number[2]  
bed = locker_number[1]         
print(f"Группа №{group}.")
print(f"{child_number}. {name}.")
print(f"Шкафчик: {locker_number}.")
print(f"Кроватка: {bed}.")
#K
number = int(input())
a = number // 1000              
b = (number // 100) % 10        
c = (number // 10) % 10        
d = number % 10                 
result = b * 1000 + a * 100 + d * 10 + c
print(result)
#L
a = input()
b = input()
while len(a) < 3:
    a = '0' + a
while len(b) < 3:
    b = '0' + b
a1 = int(a[0])  
a2 = int(a[1])  
a3 = int(a[2])  
b1 = int(b[0])  
b2 = int(b[1]) 
b3 = int(b[2])  
r1 = (a1 + b1) % 10  
r2 = (a2 + b2) % 10  
r3 = (a3 + b3) % 10  
result = r1 * 100 + r2 * 10 + r3
print(result)
#M
n = int(input())  
m = int(input())  
candies_per_child = m // n
remaining_candies = m % n
print(candies_per_child)
print(remaining_candies)
#N
red = int(input())
green = int(input())
blue = int(input())
max_moves = red + blue + 1
print(max_moves)
#O
n = int(input())  
m = int(input())  
t = int(input())  
total_minutes = n * 60 + m + t
hours = (total_minutes // 60) % 24
minutes = total_minutes % 60
print(f"{hours:02d}:{minutes:02d}")
#P
a = int(input())  
b = int(input())  
c = int(input())  
distance = abs(a - b)
time = distance / c
print(f"{time:.2f}")
#Q
total = int(input())           
binary = input()                
last_purchase = int(binary, 2)
result = total + last_purchase
print(result)
#R
price_binary = input()     
money = int(input())       
price_decimal = int(price_binary, 2)
change = money - price_decimal
print(change)
#S
product = input()
price = int(input())
weight = int(input())
money = int(input())
total = price * weight
change = money - total
print("================Чек================")
print(f"Товар:{product:>29}")
print(f"Цена:{f'{weight}кг * {price}руб/кг':>30}")
print(f"Итого:{f'{total}руб':>29}")
print(f"Внесено:{f'{money}руб':>27}")
print(f"Сдача:{f'{change}руб':>29}")
print("===================================")
#T
n = int(input())      
m = int(input())     
k1 = int(input())     
k2 = int(input())     
x = n * (m - k2) // (k1 - k2)
y = n - x
print(x, y)
#Яндекс Python 2.2
#A
name = input()
mood = input()
print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if mood == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")
#B
petya_speed = int(input())
vasya_speed = int(input())
if petya_speed > vasya_speed:
    print("Петя")
else:
    print("Вася")
#C
petya = int(input())
vasya = int(input())
tolya = int(input())
if petya > vasya and petya > tolya:
    print("Петя")
elif vasya > petya and vasya > tolya:
    print("Вася")
else:
    print("Толя")
#D
petya = int(input())
vasya = int(input())
tolya = int(input())
if petya > vasya and petya > tolya:
    first = "Петя"
    if vasya > tolya:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif vasya > petya and vasya > tolya:
    first = "Вася"
    if petya > tolya:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
else:
    first = "Толя"
    if petya > vasya:
        second = "Петя"
        third = "Вася"
    else:
        second = "Вася"
        third = "Петя"

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")
#E
a = int(input())
b = int(input())
petya = 6 + a
vasya = 12 + b
if petya > vasya:
    print("Петя")
else:
    print("Вася")
#F
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
#G
number = input()
if number[0] == number[3] and number[1] == number[2]:
    print("YES")
else:
    print("NO")
#H
text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")
#I
n1 = input()
n2 = input()
n3 = input()
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)
#J
n = int(input())
h = n // 100
a = (n // 10) % 10
b = n % 10
sum1 = a + b        
sum2 = h + a     
if sum1 > sum2:
    print(f"{sum1}{sum2}")
else:
    print(f"{sum2}{sum1}")
#K
n = int(input())
a = n // 100          
b = (n // 10) % 10    
c = n % 10            
if a >= b and a >= c:
    maxi = a
elif b >= a and b >= c:
    maxi = b
else:
    maxi = c

if a <= b and a <= c:
    mini = a
elif b <= a and b <= c:
    mini = b
else:
    mini = c
middle = a + b + c - maxi - mini
if mini + maxi == middle * 2:
    print("YES")
else:
    print("NO")
#L
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
#M
n1 = input()
n2 = input()
n3 = input()
if n1[0] == n2[0] == n3[0]:
    print(n1[0])
elif n1[1] == n2[1] == n3[1]:
    print(n1[1])
#Q
n1 = input()
n2 = input()
a = int(n1[0])
b = int(n1[1])
c = int(n2[0])
d = int(n2[1])
if a >= b and a >= c and a >= d:
    maxi = a
elif b >= a and b >= c and b >= d:
    maxi = b
elif c >= a and c >= b and c >= d:
    maxi = c
else:
    maxi = d
if a <= b and a <= c and a <= d:
    mini = a
elif b <= a and b <= c and b <= d:
    mini = b
elif c <= a and c <= b and c <= d:
    mini = c
else:
    mini = d
total = a + b + c + d
sum = total - maxi - mini
middle = sum % 10
number = maxi * 100 + middle * 10 + mini
print(number)
#R
a = float(input())
b = float(input())
c = float(input())
if a >= b and a >= c:
    longest = a
    side1 = b
    side2 = c
elif b >= a and b >= c:
    longest = b
    side1 = a
    side2 = c
else:
    longest = c
    side1 = a
    side2 = b
if longest**2 < side1**2 + side2**2:
    print("крайне мала")
elif longest**2 > side1**2 + side2**2:
    print("велика")
else:
    print("100%")
#T
str1 = input()
str2 = input()
str3 = input()
result = []
if "зайка" in str1:
    result.append(str1)
if "зайка" in str2:
    result.append(str2)
if "зайка" in str3:
    result.append(str3)
result.sort()
print(result[0], len(result[0]))