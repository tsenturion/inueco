"""
list - список, хранит разные типы данных, изменяемая структура данных
"""
list1 = []
print(list1)

list1 = [0, 1, 2, 3, 4]
print(list1)
"""
индексация начинается с 0
"""
list1 = [3, 1.1, "asd", True, None, [1, 2]]
#        0   1    2     3      4      5

print(list1)

for e in list1:
    print(e)

list1 = list(range(10))
print(range(10))
print(list1)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[0])
print(list1[1])
print(list1[5])
print(list1[8])

print()

str1 = "asd"
# asd
# 012
print(str1[0])
print(str1[1])
print(str1[2])

print()
"""
внутри [i] - i индекс, если 1 элемент
[i:j:k] - срез списка с начиная i по j не включительно с шагом k
i - начало/start
j - конец/stop
k - шаг/step
"""
list1 = list(range(10))
print(list1)
print(list1[2:5])
print('первая половина:', list1[5:])
print('вторая половина:', list1[:5])

print()

print(list(range(2, 20)))
print(list(range(6, 10)))

print()

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[2:9:2])
# [2, 4, 6, 8]

print(list(range(60, 8061, 250)))