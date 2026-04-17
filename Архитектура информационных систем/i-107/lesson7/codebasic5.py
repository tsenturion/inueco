#56

def print_reversed_numbers(n: int):
    while n > 0:
        print(n)
        n = n - 1
    print("finished!")

#57

def join_numbers_from_range(start: int, finish: int):
    result = ''
    i = start
    while i <= finish:
        result = result + str(i)
        i = i + 1
    return result

#58

def add_spaces(text: str) -> str:
    result = ''
    i = 0
    while i < len(text):
        result = result + text[i]
        if i < len(text) - 1:
            result = result + ' '
        i = i + 1
    return result

#59

def count_chars(string: str, char: str) -> int:
    index = 0
    count = 0
    target_char = char.lower()
    while index < len(string):

        if string[index].lower() == target_char:
            count = count + 1
        index = index + 1
    return count

#60

def filter_string(text: str, char: str) -> str:
    result = ''
    i = 0
    
    while i < len(text):
        if text[i] != char:
            result += text[i]  
        i += 1  
    
    return result

#61

def is_contains_char(string: str, char: str) -> bool:
    i = 0
    
    while i < len(string):
        if string[i] == char:
            return True
        i += 1
    
    return False

#62

def filter_string(text: str, char: str) -> str:
    result = ''
    target_char = char.lower()
    
    for current_char in text:
        if current_char.lower() != target_char:
            result += current_char
    
    return result

#63

def fizzbuzz(n: int) -> str:
    result = ''
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result += 'FizzBuzz'
        elif i % 3 == 0:
            result += 'Fizz'
        elif i % 5 == 0:
            result += 'Buzz'
        else:
            result += str(i)


        if i != n:
            result += ' '
    
    return result

