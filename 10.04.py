name = input()
cena = int(input())
ves = int(input())
many = int(input())
itog = cena * ves
itog = int(itog)
has = many - itog
has = int(has)
bri = str(ves) + 'кг * ' + str(cena) + 'руб/кг'
print("================Чек================")
print(f'Товар: {name:>28}')
print(f"Цена: {bri:>29}")
print(f"Итого: {itog:25}руб")
print(f"Внесено: {many:23}руб")
print(f"Сдача: {has:25}руб")
print('===================================')