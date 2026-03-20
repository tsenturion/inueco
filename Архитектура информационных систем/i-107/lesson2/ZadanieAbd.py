# 1 Привет, Мир
print('Hello, World!')
# 2 Комментарии
# You know nothing, Jon Snow!
# 3 Инструкции (Statements)
print('Robert')
print('Stannis')
print('Renly')
# 4 Как мы проверяем ваши решения
print(10)
# 5 Синтаксические ошибки
print('What Is Dead May Never Die')
# 6 Арифметические операции
print(81 / 9)
# 7 Операторы
print(6 - -81)
# 8 Коммутативная операция
print(3 ** 5)
print(-8 / -4) 
# 9 Композиция операций
print(8 / 2 + 5 - -3 / 2)
# 10 Приоритет
print(70 * (3 + 4) / (8 + 2))
# 11 Числа с плавающей точкой
print(0.39 * 0.22)
# 12 Линтер
print((5 ** 2)-(3 * 7))
# 13 Кавычки
print('"Khal Drogo\'s favorite word is "athjahakar""')
# 14 Экранированные последовательности
print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')
# 15 Конкатенация
print('Winter ' + 'came for the House of Frey.')
# 16 Кодировка
print(chr(126))
print(chr(94))
print(chr(37))
# 17 Что такое переменная
motto = 'What Is Dead May Never Die!'
print(motto)
# 18 Изменение переменной
name = 'anneirB'  
print(name) 
# 19 Выбор имени переменной
x = 'Father!'
x = 2
print(x)
# 20 Выражения в определениях
euros_count = 100 * 1.25
dollars_count = euros_count * 6.91
print(euros_count)
print(dollars_count)
# 21 Переменные и конкатенация
 first_name = 'Joffrey'
greeting = 'Hello'
info = 'Here is important information about your account security.'
intro = 'We couldn\'t verify your mother\'s maiden name.'
print(greeting + ', ' + first_name + '!')
print(info + '\n' + intro)
# 22 Именование переменных
first_number = 20
second_number = -100
print(first_number * second_number)
# 23 Магические числа
king = "Rooms in King Balon's Castles:"
number_of_castles = 6
rooms_per_castle = 17
print(king)
print(number_of_castles * rooms_per_castle)
# 24 Константы
DRAGONS_BORN_COUNT = 3
#25 Интерполяция
stark = " Arya"
what_is_it = 'Do you want to eat,' f'{stark}?'
print(what_is_it)
#26 Извлечение символов из строки
name = "Na\nharis"
print(name[7]) 
#27 Срезы строк
value = "Hexlet"
print(value[2:5])
#28 Multi-line строки
text = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground.'''
print(text)
#29 Типы данных
print(-0.304)
#30 Сильная (или Строгая) типизация
print(int('7') - (-8 - -2))
#31 Неизменяемость примитивных типов
one = "Naharis"
two = "Mormont"
three = "Sand"
result = f"{one[2]}{two[1]}{three[3]}{two[4]}{two[2]}"
print(result)
#32 Явное преобразование типов
value = 2.9
integer_value = int(value)
string_value = str(integer_value) 
output_string = string_value + ' times' 
print(output_string)
#33 Функции и их вызов
company1 = "Apple"
company2 = "Samsung"
length1 = len(company1)
length2 = len(company2)
combined_length = length1 + length2 
print(combined_length)
#34 Параметры по умолчанию
number = 10.1234
result = round(number, 2)
print(result)
#35 Вызов функции — выражение
text = "Never forget what you are, for surely the world will not"
output = f"First: {text[0]}\nLast: {text[-1]}"
print(output)
#36 Функции с переменным числом параметров
numbers = [3, 10, 22, -3, 0]
minimum_number = min(numbers)
print(minimum_number)
#37 Детерминированность
from random import random
import random
print(round(random.random() * 10))
#38 Объекты
text = "a MIND needs Books as a Sword needS a WHETSTONE."
lowered_text = text.lower()
print(lowered_text)
#39 Неизменяемость
first_name = "  Grigor   \n"
first_name = first_name.strip()
print(first_name)
#40 Цепочка вызовов
text = "When \t\n you play a \t\n game of thrones you win or you die."
result_length = len(text[5:15].strip())
print(result_length)
#41 Создание (определение) функций
def print_motto():
    print('Winter is coming')
#42 Возврат значений
def truncate(text, length):
    if len(text) > length:
        truncated_text = text[:length] + '...'
    else:
        truncated_text = text
    return truncated_text
print(truncate('hexlet', 2))
print(truncate('it works!', 4))
print(truncate('ok', 5))
#43 Необязательные параметры функций
def get_hidden_card(card_number, stars_count=4):
    visible_digits = card_number[-4:]
    mask = '*' * stars_count
    hidden_card = mask + visible_digits
    return hidden_card
print(get_hidden_card('1234567812345678'))
print(get_hidden_card('1234567812345678', 2))
print(get_hidden_card('1234567812345678', 3))
print(get_hidden_card('2034399002121100'))
print(get_hidden_card('2034399002121100', 1))
#44 Именованные аргументы
def trim_and_repeat(text, offset=0, repetitions=1):
    trimmed_text = text[offset:]
    repeated_text = trimmed_text * repetitions
    return repeated_text
text = 'python'
print(trim_and_repeat(text, offset=3, repetitions=2))
print(trim_and_repeat(text, repetitions=3))
print(trim_and_repeat(text))
#45 Аннотации типов
def word_multiply(text: str, repeats: int) -> str:
    return text * repeats
text = 'python'
print(word_multiply(text, 2))
print(word_multiply(text, 0))
#46 Логический тип
def is_pensioner(age: int) -> bool:
    return age >= 60
print(is_pensioner(75))
print(is_pensioner(18))
#47 Сравнение строк
def is_long_word(word: str) -> bool:
    return len(word) > 5
print(is_long_word("apple")) 
print(is_long_word("banana")) 
#48 Комбинирование операций и функций
def is_international_phone(phone_number: str) -> bool:
    return phone_number.startswith("+")
print(is_international_phone('89602223423'))
print(is_international_phone('+79602223423'))
#49 Логические операторы
def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
print(is_leap_year(2018))
print(is_leap_year(2017))
print(is_leap_year(2016))
#50 Отрицание
def is_palindrome(word: str) -> bool:
    normalized_word = word.lower()
    reversed_word = normalized_word[::-1]
    return normalized_word == reversed_word
def is_not_palindrome(word: str) -> bool:
    return not is_palindrome(word)
print(is_palindrome('шалаш'))
print(is_palindrome('хекслет'))
print(is_palindrome('Довод'))
print(is_palindrome('Функция'))
print(is_not_palindrome('шалаш'))
print(is_not_palindrome('Ага'))
print(is_not_palindrome('хекслет'))
#51 Результат логических выражений
def string_or_not(obj):
       return 'yes' if isinstance(obj, str) else 'no'
print(string_or_not('Hexlet'))
print(string_or_not(10))
print(string_or_not(''))
print(string_or_not(False))
#52 Условная конструкция (if)
def guess_number(number: int) -> str:
    if number == 42:
        return 'You win!'
    return 'Try again!'
print(guess_number(42))
print(guess_number(61))
#53 Условная конструкция else
def normalize_url(url: str) -> str:
    if url.startswith('https://'):
        return url
    elif url.startswith('http://'):
        return 'https://' + url[len('http://'):]
    else:
        return 'https://' + url
print(normalize_url('https://ya.ru'))
print(normalize_url('google.com'))
print(normalize_url('http://ai.fi'))
#54 Конструкция else + if = elif
def who_is_this_house_to_starks(house: str) -> str:
    if house == 'Karstark' or house == 'Tully':
        return 'friend'
    elif house == 'Lannister' or house == 'Frey':
        return 'enemy'
    else: 
        return 'neutral'
print(who_is_this_house_to_starks('Karstark'))
print(who_is_this_house_to_starks('Frey'))
print(who_is_this_house_to_starks('Joar'))
print(who_is_this_house_to_starks('Ivanov'))
#55 Тернарный оператор
def flip_flop(word: str) -> str:
    if word == 'flip':
        return 'flop'
    else:
        return 'flip'
print(flip_flop('flip'))
print(flip_flop('flop'))
#56 Оператор Match
def get_number_explanation(number: int) -> str:
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'
print(get_number_explanation(8))
print(get_number_explanation(666))
print(get_number_explanation(42))
print(get_number_explanation(7))
#57 Цикл While
def print_reversed_numbers(n: int) -> None:
    i = n 
    while i > 0:
        print(i)
        i -= 1 
    print("finished!")
print_reversed_numbers(4)
#58 Агрегация данных (Числа)
def multiply_numbers_from_range(start: int, end: int) -> int:
    product = 1
    for num in range(start, end + 1):
        product *= num
    return product 
print(multiply_numbers_from_range(1, 5))
print(multiply_numbers_from_range(2, 3))
#59 Агрегация данных (Строки)
def join_numbers_from_range(start: int, end: int) -> str:
    result = ''
    for num in range(start, end + 1):
        result += str(num)
    return result
print(join_numbers_from_range(1, 1))
print(join_numbers_from_range(2, 3))
print(join_numbers_from_range(5, 10))
#60 Обход строк
def add_spaces(text: str) -> str:
    result = ''
    for char in text[:-1]:
        result += char + ' '
    result += text[-1]
    return result
print(add_spaces("hex"))
print(add_spaces("Arya"))
#61 Условия внутри тела цикла
def count_chars(string: str, char: str) -> int:
    count = 0
    target_char = char.lower()
    normalized_string = string.lower()
    for current_char in normalized_string:
        if current_char == target_char:
            count += 1
    return count
print(count_chars('HexlEt', 'e'))
print(count_chars('HexlEt', 'E'))
#62 Синтаксический сахар
def filter_string(text, char):
    result = ''
    i = 0
    while i < len(text):
        if text[i] != char:
            result += text[i]
        i += 1
    return result
#63 Возврат из циклов
def is_contains_char(string: str, char: str) -> bool:
    index = 0
    while index < len(string):
        if string[index] == char:
            return True
        index += 1
    return False
#64 Цикл For
def filter_string(text: str, char: str) -> str:
    new_text = ""
    for current_char in text:
        if current_char.lower() != char.lower():
            new_text += current_char
    return new_text
#65 Цикл for и функция range
def fizzbuzz(n: int) -> str:
    result = []
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))
    return " ".join(result) 