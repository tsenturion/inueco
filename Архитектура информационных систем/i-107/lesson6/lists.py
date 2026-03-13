a = 1
b = 1.1
c = "1"
d = True

list1 = [1, 2, 3, 4, 5]
print(list1)
print(type(list1))

list1 = [1, 1.1, '1', True, [1], []]
print(list1)

list1 = [1]
print(list1)

list1 = []
print(list1)

list1.append(1)
print(list1)

count = 0
list1 = []
print(list1)
while count < 10:
    list1.append(count)
    count += 1
    print(list1)
else:
    print('данные загружены')

print(list1)