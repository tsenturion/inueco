print("рассчет стоимости покупки")

price = int(input("введите цену товара: "))
count = int(input("введите количество товара: "))

total = price * count

if total > 1000:
    total = total * 0.9 # скидка 10%

print(f'Стоимость покупки: {total} рублей')