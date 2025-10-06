"""
help
len
max
min
sum
sorted
enumerate
zip
abs
round
isinstance
id
all
any
pow
hash
bin
oct
hex

int
"""

my_list = [1, 2, 3, 4, 5]
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sorted(my_list, reverse=True))

for index, value in enumerate(my_list):
    print(f"индекс {index} значение {value}")

names = ["ivan", "petr", "anna"]
ages = [20, 22, 18]
cities = ["moscow", "spb", "kazan"]

for name, age, city in zip(names, ages, cities):
    print(f"имя {name} возраст {age} город {city}")

zipped = zip(names, ages, cities)
print(list(zipped))

print(abs(-100))
print(round(6.567, 2))

print(isinstance(100, int))

print(id(my_list))

help(len)

print(any([False, '', [], 1]))
print(all([False, '', [], 1]))

print(pow(2, 3))