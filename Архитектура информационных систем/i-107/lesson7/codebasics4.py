#45
def is_pensioner(age: int) -> bool:
    return age >= 60

#46
def is_long_word(word: str) -> bool:
    return len(word) > 5

#47

def is_international_phone(phone):
    if phone[0] == '+':
        return True
    else:
        return False
    
#48 

def is_leap_year(year):
   return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

#49

def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]

def is_not_palindrome(word):
    return not is_palindrome(word)

#50

def string_or_not(value):
    return isinstance(value, str) and 'yes' or 'no'

#51

def guess_number(number):
    if number == 42:
        return 'You win!'
    return 'Try again!'

#52

def normalize_url(url):
    if url.startswith('https://'):
        return url
    elif url.startswith('http://'):
        return 'https://' + url[7:]
    else:
        return 'https://' + url
    
#53

def who_is_this_house_to_starks(house_name):
    if house_name == 'Karstark' or house_name == 'Tully':
        return 'friend'
    elif house_name == 'Lannister' or house_name == 'Frey':
        return 'enemy'
    else:
        return 'neutral'
    
#54

def flip_flop(value):
    if value == 'flip':
        return 'flop'
    else:
        return 'flip'
    
#55

def get_number_explanation(number):
    match number:
        case 666:
            return 'devil number'
        case 42:
            return 'answer for everything'
        case 7:
            return 'prime number'
        case _:
            return 'just a number'