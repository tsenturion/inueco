#14
print("- Did Joffrey agree?\n- He did. He also said \"I love using \\n\".")

#15
print('Winter ' + 'came ' + 'for ' + 'the ' + 'House ' + 'of ' + 'Frey.')

#16
print(chr(126))
print(chr(94))
print(chr(37))

#17
motto = 'What Is Dead May Never Die!'
print(motto)

#18
name = "Brienna"
# BEGIN (write your solution here)
name='anneirB'
# END
print(name)

#19
a = 2
print(a)

#20
euros_count = 100
# BEGIN (write your solution here)
dollar = euros_count*1.25
inter_dollar = int(dollar)
youan = inter_dollar*6.91
print(dollar)
print(youan)
# END

#21
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security.\n"

first_name = "Joffrey"
greeting = "Hello"

# BEGIN (write your solution here)
print(greeting + ', ' + first_name +'!')
print(intro + info)
# END

#22
first_num = 20
second_num = -100
print(first_num*second_num)

#23
king = "Rooms in King Balon's Castles:"

# BEGIN (write your solution here)
castles = 6
rooms = 17
print(king)
print(castles*rooms)
# END

#24
DRAGONS_BORN_COUNT = 3

#25
stark = "Arya"

# BEGIN (write your solution here)
print('Do you want to eat,', stark+'?')
# END

#26
name = "Na\nharis"

# BEGIN (write your solution here)
print(name[-1])
# END

#27
value = "Hexlet"

# BEGIN (write your solution here)
print(value[2:5])
# END


#28
# BEGIN (write your solution here)
text = 'Lannister, Targaryen, Baratheon, Stark, Tyrell...\nthey\'re all just spokes on a wheel.\nThis one\'s on top, then that one\'s on top, and on and on it spins,\ncrushing those on the ground.'
# END

print(text)

#29
print(-0.304)

#30
print(7 - (-8 - -2))

#31
one = "Naharis"
two = "Mormont"
three = "Sand"

# BEGIN (write your solution here)
print(one[2]+two[1]+three[3]+two[4]+two[2])
# END

#32
value = 2.9

# BEGIN (write your solution here)
print(str(int(2.9)),'times')
# END

#33
company1 = "Apple"
company2 = "Samsung"

# BEGIN (write your solution here)
print(len(company1+company2))
# END


#34
number = 10.1234

# BEGIN (write your solution here)
print(round(number,2))
# END

#35
text = "Never forget what you are, for surely the world will not"

# BEGIN (write your solution here)
print(f'First: {text[0]}\nLast: {text[-1]}')
# END

#36
# BEGIN (write your solution here)
print(min([3,10,22,-3,0]))
# END

#37
# imports are studied on Hexlet
from random import random

# BEGIN (write your solution here)
print(round(random()*10))
# END

#38
text = "a MIND needs Books as a Sword needS a WHETSTONE."

# BEGIN (write your solution here)
print(text.lower())
# END

#39
first_name = "  Grigor   \n"

# BEGIN (write your solution here)
print(first_name.strip())
# END

#40
text = "When \t\n you play a \t\n game of thrones you win or you die."

# BEGIN (write your solution here)
print(len(text[4:15].strip()))
# END

#41
def print_motto():
    print("Winter is coming")

#42
def truncate(text, length):
    # BEGIN (write your solution here)
    return text[:length]+'...'
    # END

#43
def get_hidden_card(card_number, stars_count=4):
    visible_digits = card_number[-4:]
    return '*' * stars_count + visible_digits

#44
def trim_and_repeat(text, offset=0, repetitions=1):
    trimmed_text = text[offset:]
    return trimmed_text * repetitions
text = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
trim_and_repeat(text,offset=2,repetitions=4)

#45
def word_multiply(text: str, n: int) -> str:
    return text * n

text = 'python'
print(word_multiply(text, 2))
print(word_multiply(text, 0))

#46
def is_pensioner(age):
    return age >= 60
print(is_pensioner(59))
print(is_pensioner(60))
print(is_pensioner(65))

#47
def is_long_word(word):
    return len(word) > 5

#48
def is_international_phone(phone):
    return phone[0]=='+'

#49
def is_leap_year(year):
    return year%400==0 or (year%4==0 and year%100!=0)

#50
def is_palindrome(a):
    b = a.lower()
    return b == b[::-1]
def is_not_palindrome(a):
    return not is_palindrome(a)

#51
def string_or_not(word):
    if isinstance(word, str):
        return 'yes'
    else:
        return 'no'
    
#52
def guess_number(num):
    return 'You win!' if num==42 else 'Try again!'

#53
def normalize_url(url):
    if url[:8] == 'https://':
        return url
    if url[:7] == 'http://':
        return 'https://' + url[7:]
    return 'https://' + url

#54
def who_is_this_house_to_starks(surname):
    if surname == 'Karstark' or surname == 'Tully':
        return 'friend'
    elif surname == 'Lannister' or surname == 'Frey':
        return 'enemy'
    else:
        return 'neutral' 
    
#55
def flip_flop(word):
    return 'flop' if word=='flip' else 'flip'

#56
def get_number_explanation(num):
    if num == 666:
        return 'devil number'
    elif num == 42:
        return 'answer for everything'
    elif num == 7:
        return 'prime number'
    else:
        return 'just a number'


#57
def print_reversed_numbers(number):
    while number > 0:
        print(number)
        number -= 1
    print('finished!')

#58
def multiply_numbers_from_range(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

#59
def join_numbers_from_range(n1,n2):
    r=''
    for i in range(n1,n2+1):
        r+=str(i)
    return r

#60
def add_spaces(text):
    result = ""
    for char in text:
        result += char + " "
    return result.strip()

#61
def count_chars(text, char):
    count = 0
    ltext = text.lower()
    lchar = char.lower()
    for cchar in ltext:
        if cchar == lchar:
            count += 1
    return count

#62
def filter_string(text, char):
    result = ''
    i = 0
    while i < len(text):
        current_char = text[i]
        if current_char != char:
            result += current_char
        i += 1
    return result

#63
def is_contains_char(word, symb):
    return symb in word

#64
def filter_string(word, symb):
    return "".join([char for char in word if char.lower() != symb.lower()])

#65
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return " ".join(result)