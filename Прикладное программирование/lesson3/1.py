"""
len() - количество элементов в последовательности
in - оператор вхождения
"""

for i in range(10):
    print(i)

if 10 in [1, 2, 3, 4, 5]:
    print(True)
else:
    print(False)

print()

forbidden_symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
login = "aoknfgG98yoi*&"
for letter in login:
    if letter in forbidden_symbols:
        print(letter)

print()

print(len(range(5)))
print(len("  "))
print(len([1, 2, 3, 4, 5]))