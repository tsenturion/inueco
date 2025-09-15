dict1 = {'name': 'alice', 'city': 'new york'}
print(type(dict1))

set1 = set()
zero_dict = {}
zero_dict['age'] = 30
zero_dict['name'] = 'bob'

dict1 = dict(name='bob', age=30)

# ----------------------------------------------------------------
num = 42
hash_value = hash(num)
print(hash_value)

"""my_list = [1, 2, 3, 4]
hash_value = hash(my_list)
print(hash_value)"""

str1 = '123'
hash_value = hash(str1)
print(hash_value)

my_list = [1, 2, 3, 4]
hash_value = hash(tuple(my_list))
print(hash_value)
# ----------------------------------------------------------------

print(zero_dict['age'])
print(zero_dict.get('name', None))
zero_dict['age'] = 31
del zero_dict['name']
print(zero_dict)
for key, value in zero_dict.items():
    print(f'{key}: {value}')

"""
keys() - список ключей
values() - значений
items() - пары
get(key, default) возвр значение по ключу и default если ключ отсутствует
pop(key, default) удаление и возвр значения
popitem() удаляет и возвр последнюю добавл пару
clear()
copy()
del удаление
"""

a = {
    "name": "alice",
    "age": 243,
    'address': {
        "city": "new york",
        "zip": '10101'
    }
}
basketball_players = {}

def add_player(name, height):
    if name in basketball_players:
        print(f"{name} уже есть")
    else:
        basketball_players[name] = height
        print(f'{name} добавлен')

def remove_player(name):
    if name in basketball_players:
        del basketball_players[name]
    else:
        print(f'{name} нет')

def find_player(name):
    if name in basketball_players:
        print(f'{name} {basketball_players[name]}')
    else:
        print(f'{name} нет')

def update_player(name, new_height):
    if name in basketball_players:
        basketball_players[name] = new_height
        print(f'{name} {basketball_players[name]}')
    else:
        print(f'{name} нет')

