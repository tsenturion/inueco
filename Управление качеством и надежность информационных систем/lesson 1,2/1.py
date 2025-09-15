"""
int - целочисленный 10 123 12312  21 321 321 21321321321321
float - числа с плавающей точкой 123.123  23423423423.23423434

str - "eewfew%^&(%^&*(%     \t&))"
str - '123drfeswrrere'
str - "123"
str '12-12-2012 Количество кликов: 21'
str - неизменяемый тип данных

bool - True False

list
dict
tuple
set
frozenset
"""
PI = 3.14

number = 5
amount_click = 21

float1 = 3.15435434543
name = 'Alice'

flag = True
flag2 = False

# print = 5
# type = 8
"""
print()
type()
input()
"""
print(type(number).__name__)
print(type(amount_click).__name__)
print(type(float1).__name__)
print(type(name).__name__)
print(type(flag).__name__)
print(type(flag2).__name__)

'''
многострочный
комментарий
'''
# комментарий

print(123)
print("123")
print(PI)
print(flag)

some_int = 1 + 2 / 3 * 5 - 5 - PI + number
"""
** - степень
//
%

+=
/=
*=
-=
**=
//=
%=

"""

print(some_int)
print(1 + 2 / 3 * 5 - 5 - PI + number)

print(10 % 3)  # = 1
print(10 // 3) # = 3

print(10 * 0.1)
print()

number = 5 
number += 6

print(number)

amount_click = 5
amount_click = "23424"

print(amount_click)

list1 = [1, 2]
str1 = "asd" ###

list1.append(3)
print(list1)

str1 = str1.capitalize()
print(str1)

