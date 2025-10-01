someStr = '123z121saf253'
length1 = len([1, 2, 3])
length2 = len(someStr)

sorted1 = sorted(someStr)
print(sorted1)
print(''.join(sorted1))
msg = ' 3 4 456  456456    6 5'
print(msg.split())
print(msg.strip())

# 0x00 - 0
#someStr.replace()

msg = 'qakhbqvbhf'
msg_encoded = msg.encode('utf-8')
msg_decoded = msg_encoded.decode('utf-8')

print(msg_encoded)
print(msg_decoded)

print(type(1))

print(id(msg))

msg.capitalize()  # перевод первого сивола строки в верхний регистр
print(msg)
print(msg.capitalize())
msg = 'qakhbqvbhf'
msg = 'Qakhbqvbhf'
msg.upper() # все в верхний регистр
msg = 'все заглавные'

print(msg.upper())
msg.lower()  # все в нижний регистр
print(msg.upper().lower())

new_msg = msg.upper()
print(new_msg)

msg = 'rt  rttt rttrrtrt куаукаук уккуак укукаку'

print(msg.title()) # первые буквы слов в верхний регистр

print(msg.swapcase()) # меняет в обе стороны

print(msg.count('r', 5, 10))
#считает количество вхождений подстроки
print(msg.find('r', 5, 10)) # возвращает индекс первого вхожденич подстроки
msg = 'rt  rttt rttrrtrt куаукаук уккуак укукаку'
msg = 'rt  rttt Rttrrtrt куаукаук уTкуак укукаку'
#print(msg.index('r', 5, 10))
# аналогично .fing, но возвращает ValueError, если подстроки нет
print(msg.rindex('r', 2, 20)) # r - с конца
print(msg.rfind('к', 2, 20)) # r - с конца

#проверка конца и начала
print(msg.startswith('rt  '))
print(msg.endswith('аку'))

#проверка строк"""
msg = 'Rt  rttt rttrrtrt куаукаук уккуак укукаку'

print(msg.isupper()) # все ли из заглавных
print(msg.islower()) # все ли из строчных
print(msg.isalnum()) # все ли из букв и цифр
print(msg.isalpha()) # все ли из букв
print(msg.isdigit()) # все ли из цифр
print(msg.isspace()) # все ли из пробелов ("" "\n" "\t")
print("Msg Rt".istitle()) # первая - заглавная

#форматирование

print(msg.center(len(msg) + 11, '*')) #дополняет символами слева и справа
print(msg.ljust(len(msg) + 11))
print(msg.rjust(len(msg) + 11, '*'))
msg = '123'
print(msg.zfill(9))
msg = '+123'
print(msg.zfill(9))
msg = '-0.123'
print(msg.zfill(9))

print('frffr', 'ererferfer', 'erfr', sep='\n')
print('frffr', 'ererferfer', 'erfr', sep='\t')
print('frffr', 'ererferfer', 'erfr', sep=' ')
print('frffr', 'ererferfer', 'erfr', sep='??')
print('frffr', 'ererferfer', 'erfr', end='\n')
print('frffr', 'ererferfer', 'erfr', end='\t')
print('frffr', 'ererferfer', 'erfr', end=' ')
print('frffr', 'ererferfer', 'erfr', end='??')

msg = 'Rt  rttt rttrrtrt куаукаук уккуак укукаку'
"""
:b - двоичная форма
:с - преобразование в юникод
:d - десятичный
:о - восьмеричный
:х - шеснадцатеричный, нижний
:+ - отображает + только для положительных
:- - отображает - только для отрицательных
:(пробел) - дополнительный пробел перед положительными и отрицательными
:< - выравнивние по левому краю
:> - по правому краю
:^ - по центру

"""
some_number = 104
print(f'erfger {some_number} = {some_number:b} в двоичной')
print(f'erfger {some_number} = {some_number:b} в двоичной')
print(f'erfger {some_number:c} ')
print(f'erfger {some_number:-} ')
print(f'erfger {some_number:+} ')
print(f'erfger {some_number: } ')
print(f'erfger {some_number:^} ')
print(f'erfger {some_number:<} ')
print(f'erfger {some_number:>} ')
print(f'erfger {some_number:.2f} ') #округление до двух знаков