flag = True
fl2 = False
result = 5 < 7
"""
>
<
>=
<=
!=
==

and
or
not

False:
0
""
0.0
''
None
()
set()
frozenset()
{}
"""
count = 0
while count < 50:
    print(count)
    count += 1
else:
    print('Цикл завершен по событию False')

count = 0
while True:
    if count == 50:
        print('сработал break')
        break

    if count % 2 == 0:
        count += 1
        print('четное число, пропускаем')
        continue

    print(count)
    count += 1


"""
str
tuple
list
set()
frozenset()
"""

list1 = [1, 2, 3, 4, 5]
str1 = '213'

#для элементов в  последовательности
#for e         in list1: 
for e in list1:
    print(e)
else:
    print('цикл закончился корректно')