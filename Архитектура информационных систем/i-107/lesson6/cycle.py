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
    
