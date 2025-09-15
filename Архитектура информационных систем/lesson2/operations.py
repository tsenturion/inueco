"""
int целочисленный 1 234  45352314214
float 1.234 1.2345678901
str "123456789012345678901234567890"
str "text"
str '12-12-2012 Количество кликов: 21'
str ''
str ""
str ' '

bool True False

list
set
dict
tuple
frozenset
"""

print(1123)
str1 = '''
длинная 
строка
'''

amount_click = 12
float1 = 1.234
date = '12-12-2012'
register_date = '12-12-2012'
number = amount_click

print(type(date))
print(type(amount_click).__name__)
print(type(register_date).__name__)

flag = True
flag2 = False

"""
функция с ()
print() - для вывода на консоль
type() - узнать тип данных
"""

print()
print()
print()
print(2)
"""
\n - перенос строки
\t - таб
"""
print(number)

number = 12 + amount_click / 5 * 2 - 1

"""
+
-
*
/
** - возведение в степень
% - остаток от деления
// - целочисленное деление
"""

number = 12 % 5
print(number)

number = 14 // 5
print(number)

amount_click = amount_click + 1
print(amount_click)

"""
+=
-=
*=
/=
**=
%=
//=
"""

amount_click += 1
print(amount_click)

amount_click += 1
print(amount_click)

amount_click += 1
print(amount_click)