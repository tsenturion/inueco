"""
while - цикл пока, с условием
break - полностью прерывает цикл
continue - пропускает итерацию
также как в if пробел, двоеточие, отступы
"""

count = 0
while count < 10:
    print(count)
    count += 1
else:
    print("цикл завершен")
print("-" * 10)

count = 0
while True:
    if count == 10:
        break

    if count % 2 == 0:
        print("четное число, пропускаем")
        count += 1
        continue
        
    print(count)
    count += 1
else:
    print("цикл завершен")