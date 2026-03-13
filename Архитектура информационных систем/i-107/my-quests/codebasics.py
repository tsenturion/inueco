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

#41 skipped

#42 skipped

#43 skipped

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