"""
while - цикл пока, с условием
break - полностью прерывает цикл
continue - пропускает итерацию
"""

count = 0
while True:
    if count == 10:
        break

    if count % 2 == 0:
        count += 1
        continue
        
    print(count)
    count += 1
else:
    print("цикл завершен")