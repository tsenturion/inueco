from pprint import pprint

number = 5
print(1, 1, 1, 1, 1)
print(1, 1, 1, 1, 1, sep="-", end="")
print(1, 1, 1, 1, 1, sep=",", end="")

person = {
    'name': 'alice',
    'age': 24,
    'address': {
        'city': 'new york',
        'zip': '10101'
    },
    'phones': [
        88005553535,
        88005553536,
    ],
}

print(person)
pprint(person, indent=4)