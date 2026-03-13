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