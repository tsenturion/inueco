# BEGIN (write your solution here)
print(f'Do you want to eat, {stark}?')
# END

#Яндекс Python 2.1

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
