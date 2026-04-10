#1
print('Hello, World!')
#2
# You know nothing, Jon Snow!
#3
print('Robert')
print('Stannis')
print('Renly')
#4
print('10')
#5
print('What Is Dead May Never Die')
#6
print(81/9)
#7
a = 6
b = -81
print(a - b)
#8
print(3**5)
print(-8/-4)
#9
a = (8/2 + 5)
b = (-3/2)
print(a-b)
#10
print(70 *(3 + 4) / (8+2))
#11
print(0.39 * 0.22)
#12
print((5 ** 2) - (3 * 7))
#13
print('"Khal Drogo\'s favorite word is "athjahakar""')

#14
print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

#15
print('- Did Joffrey agree?\n- He did. He also said "I love using \\n".')

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
name = "anneirB"
# END


print(name)

#19
brothers = 2
print(brothers)

#20
euros_count = 100
# BEGIN (write your solution here)
dollars_count= euros_count* 1.25
yuans_count = dollars_count * 6.91
print(dollars_count)
print(yuans_count)
# END

#21
info = "We couldn't verify your mother's maiden name."
intro = "Here is important information about your account security."

first_name = "Joffrey"
greeting = "Hello"

# BEGIN (write your solution here)
print(greeting + "," + " " + first_name + "!")
print(intro + "\n" + info)
# END


#22
first_number = 20
second_number = -100

cifra = first_number * second_number
print(cifra)
#23
king = "Rooms in King Balon's Castles:"

# BEGIN (write your solution here)
print(king + "\n" + "102")
# END

#24
DRAGONS_BORN_COUNT = 3
#25
stark = "Arya?"


# BEGIN (write your solution here)
print(f'Do you want to eat, {stark}')
# END

#26
name = "Na\nharis"

# BEGIN (write your solution here)
print(name[7])
# END

#27
value = "Hexlet"

# BEGIN (write your solution here)
print(value[2:5])
# END

#28

# BEGIN (write your solution here)
text = '''Lannister, Targaryen, Baratheon, Stark, Tyrell...
they're all just spokes on a wheel.
This one's on top, then that one's on top, and on and on it spins,
crushing those on the ground.'''

# END

print(text)

#29

print(-0.304)

#30

print(7 - (-8 - -2))

#31

one = "\nNaharis"
two = "\nMormont"
three = "\nSand"

# BEGIN (write your solution here)
print(one[3] + two[2] + three[4] + two[5] + two[3])
# END

#32

value = 2.9

# BEGIN (write your solution here)
value = 2.9 - 0.9
a = int(value)
print(str(a) + " times")
# END

#33
company1 = "Apple"
company2 = "Samsung"

# BEGIN (write your solution here)
print(len(company1 + company2))

# END

#34

number = 10.1234

# BEGIN (write your solution here)
result = round(10.1234, 2)
print(result)
# END


#35

text = "Never forget what you are, for surely the world will not"

# BEGIN (write your solution here)
result = f'First: {text[0]}\nLast: {text[-1]}'
print(result)

# END

#36

# BEGIN (write your solution here)
print(min(3, 10, 22, -3, 0))
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
text = "a MIND needs Books as a Sword needS a WHETSTONE."

# BEGIN (write your solution here)
print(text.lower())
# END

#40

text = "When \t\n you play a \t\n game of thrones you win or you die."

# BEGIN (write your solution here)
print(len(text[6:15].strip()))
# END

#41
def print_motto():
    motto = 'Winter is coming'
    print(motto)
    
#42
def truncate(text, length):
    # BEGIN (write your solution here)
    result = f"{text[0:length]}..."
    return(result)
    # END

#43

def trim_and_repeat (text, offset=0, repetitions=1):
    return text[offset:] * repetitions
#44
def word_multiply(text: str,count: int) -> str:
    return text * count

#45
def is_pensioner(age):
    if age >= 60:
        return True 
    else:
        return False
        

#46
def is_long_word(word):
    if len(word) > 5:
        return True
    else:
        return False

#47
def is_international_phone(number:int) -> str:
    return number[0] == '+'
#48
def is_leap_year(year):
    if year % 400 == 0 or year % 4 ==0 and year % 100 !=0:
        return True
    else:
        False
        
№49
def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]
def is_not_palindrome(word):
    return not is_palindrome(word)
