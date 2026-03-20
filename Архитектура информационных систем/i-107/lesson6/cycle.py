"""
>
<
>=
<=
!=
==
"""

print(10 > 5)
print(10 < 5)
print(10 >= 5)
print(10 <= 5)
print(10 != 5)
print(10 == 5)
print(type(True))
print(type(False))

number = 10
if number > 0:
    print('положительное')
elif number < 0:
    print('отрицательное')
else:
    print('ноль')

count = 0

while count < 10:
    print(f'count < 10 {count}')
    count += 1
else:
    print('end')


count = 0
# break
while True:
    print(f'while True {count}')
    count += 1
    if count == 10:
        break
else:
    print('end')


count = 0
# continue
while True:
    if count == 10:
        break
    
    if count % 2 != 0:
        count += 1
        continue
    
    print(f'continue {count}')
    count += 1
    
else:
    print('end')
    
str1 = '1234567890'
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#индексация с 0
print(str1[1])
print(list1[1])

print(str1[0])
print(list1[0])

print('start')
#для элементов в последовательности
#для элементов в строке
for i in str1:
    print(i, end=' ')
    
print('\n', 'end', sep='')

#для элементов в списке
for i in list1:
    print(i, end=' ')
    
print('\n','end', sep='')

#range()
print(range(10))
print(list(range(10)))

for i in range(10):
    print(i, 'hello')
    
print(list(range(20)))
print(list(range(5, 20)))
# начало, конец, шаг
print(list(range(5, 20, 2)))

# начало, конец, шаг
print('-' * 50)
str1 = '0123456789'
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(str1)
print(list1)

#индексация с 0, вывести элемент по индексу
print(str1[1])
print(list1[1])

# срез по 4 элемент не включая
print(str1[:4])
print(list1[:4])

# срез c 2 по 7 элемент не включая
print(str1[2:7])
print(list1[2:7])

# с шагом 2
print(str1[2:7:2])
print(list1[2:7:2])