#35

number = round(10.1234, 2)
print(number)
#36

text = "Never forget what you are, for surely the world will not"

result = f'First: {text[0]}\nLast: {text[-1]}'
print(result)

#37

print(min(3, 10, 22, -3, 0))

#38

from random import random
print(round(random() * 10))

#39

text = "a MIND needs Books as a Sword needS a WHETSTONE."
print(text.lower())

#40

first_name = "  Grigor   \n"
cleaned = first_name.strip()
print(cleaned)

#41

text = "When \t\n you play a \t\n game of thrones you win or you die."
result = text[5:15].strip()
print(len(result))

#42

def print_motto():
    print('Winter is coming')

# 43 

def truncate(text, length):
    return text[:length] + '...'

#44

def get_hidden_card(card_number, stars_count=4):
    return '*' * stars_count + card_number[-4:]

#45
