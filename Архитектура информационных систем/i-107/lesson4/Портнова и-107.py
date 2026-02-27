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