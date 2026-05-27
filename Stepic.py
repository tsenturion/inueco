#11.1
n = int(input())

result = list(range(1, n + 1))

print(result)
#2
n = int(input())

alphabet = list('abcdefghijklmnopqrstuvwxyz')

print(alphabet[:n])
#3
n = int(input())

result = list(range(1, n + 1, 2))

print(result)
#4
s = input()

result = list(s[::2])

print(result)
#11.2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[16])
#2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[-1])
#3
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

print(primes[:6])
#4
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

print(min(numbers) + max(numbers))
#5
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

average = sum(evens) / len(evens)

print(average)
#6
rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

rainbow[3] = 'Зеленый'
rainbow[6] = 'Фиолетовый'

print(rainbow)
#7
languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic',
             'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

print(languages[::-1])
#8
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 * 2 + numbers2 * 9 + numbers3)
#11.3
result = []

for i in range(26):
    result.append(chr(97 + i) * (i + 1))

print(result)

#2
n = int(input())

result = []

for _ in range(n):
    result.append(input())

print(result)
#3
n = int(input())

result = []

for _ in range(n):
    x = int(input())
    result.append(x ** 3)

print(result)
#4
numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10,
           8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 
           1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))

print(numbers[-1])

print(numbers[::-1])

print("YES" if 5 in numbers and 17 in numbers else "NO")

print(numbers[1:-1])
#5
n = int(input())

result = []

for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)

print(result)
#6
n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

result = []
for i in range(n - 1):
    result.append(numbers[i] + numbers[i + 1])

print(result)
#7
n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

del numbers[1::2]

print(numbers)
#8
n = int(input())

result = []

for _ in range(n):
    s = input()
    for char in s:
        result.append(char)

print(result)
#9
n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

k = int(input())

result = ''

for s in strings:
    if len(s) >= k:
        result += s[k - 1]

print(result)
#11.4
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

print(sum(x**2 for x in numbers))
#2
n = int(input())

negatives = []
zeros = []
positives = []

for _ in range(n):
    x = int(input())
    if x < 0:
        negatives.append(x)
    elif x == 0:
        zeros.append(x)
    else:
        positives.append(x)

for num in negatives:
    print(num)

for num in zeros:
    print(num)

for num in positives:
    print(num)
#3
n = int(input())

seen = set()

for _ in range(n):
    s = input()
    if s not in seen:
        print(s)
        seen.add(s)
#4
n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

for num in numbers:
    print(num)

print()

for num in numbers:
    print(num**2 + 2*num + 1)
#5
n = int(input())

numbers = []
for _ in range(n):
    numbers.append(int(input()))

min_val = min(numbers)
max_val = max(numbers)

for num in numbers:
    if num != min_val and num != max_val:
        print(num)
#6
n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

query = input().lower()

for s in strings:
    if query in s.lower():
        print(s)
#7
n = int(input())

strings = []
for _ in range(n):
    strings.append(input())

k = int(input())

queries = []
for _ in range(k):
    queries.append(input().lower())

for s in strings:
    s_lower = s.lower()
    if all(q in s_lower for q in queries):
        print(s)
#11.5
s = input()

words = s.split()

for word in words:
    print(word)
#2
s = input().split()

print(f"{s[0][0]}.{s[1][0]}.{s[2][0]}.")
#3
s = input()

parts = s.split('\\')

for part in parts:
    print(part)
#4
s = input()

numbers = list(map(int, s.split()))

for num in numbers:
    print('+' * num)
#5
s = input()

parts = s.split('.')

if len(parts) != 4:
    print("НЕТ")
else:
    ok = True
    for part in parts:
        if not part.isdigit():
            ok = False
            break
        num = int(part)
        if num < 0 or num > 255:
            ok = False
            break

    print("ДА" if ok else "НЕТ")
#6
s = input()
sep = input()

print(sep.join(s))
#7
nums = list(map(int, input().split()))

count = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            count += 1

print(count)
#11.6
s = input().lower()

words = s.split()

count = 0
for word in words:
    if word in ['a', 'an', 'the']:
        count += 1

print(f"Общее количество артиклей: {count}")
#2
numbers = [8, 9, 10, 11]
numbers[1] = 17
numbers += [4, 5, 6]
del numbers[0]
numbers *= 2
numbers.insert(3, 25)
print(numbers)
#3
first = input()
n = int(first[1:])
for _ in range(n):
    line = input()
    if '#' in line:
        line = line[:line.index('#')]
    print(line.rstrip())
#4
nums = list(map(int, input().split()))

min_index = nums.index(min(nums))
max_index = nums.index(max(nums))

nums[min_index], nums[max_index] = nums[max_index], nums[min_index]

print(*nums)
#5
nums = list(map(int, input().split()))

print(*sorted(nums))

print(*sorted(nums, reverse=True))
#6
n = int(input())

songs = []
for _ in range(n):
    songs.append(input())

songs.sort()

for song in songs:
    print(song)
#11.7
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert','break', 'class', 'continue', 'def', 'del', 'elif', 'else','except', 'finally', 'try', 'for', 'from', 'global', 'if','import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or','pass', 'raise', 'return', 'while', 'yield']

new_keywords = [word[1:] for word in keywords]

print(new_keywords)
#2
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert','break', 'class', 'continue', 'def', 'del', 'elif', 'else','except', 'finally', 'try', 'for', 'from', 'global', 'if','import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or','pass', 'raise', 'return', 'while', 'yield']

lengths = [len(word) for word in keywords]

print(lengths)
#3
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
new_keywords = [word for word in keywords if len(word) >= 5]

print(new_keywords)
#4
palindromes = [x for x in range(100, 1001) if str(x) == str(x)[::-1]]

print(palindromes)
#5
print(*input().split(), sep='\n')
#6
n = int(input())

squares = [i**2 for i in range(1, n + 1)]

for x in squares:
    print(x)
#7
nums = [int(x) ** 3 for x in input().split()]

for num in nums:
    print(num, end=' ')
#8
s = input()

digits = [ch for ch in s if ch.isdigit()]

print(''.join(digits))
#9
print(*[int(x)**2 for x in input().split() if int(x) % 2 == 0 and (int(x)**2) % 10 != 4])
#11.8
a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

n = len(a)

for i in range(n - 1):
    swapped = False
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True
    if not swapped:
        break 

print(a)
#2
a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

n = len(a)

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if a[j] < a[min_index]:
            min_index = j
    
    a[i], a[min_index] = a[min_index], a[i]

print(a)
#13.1
def draw_box():
    for i in range(14):
        if i == 0 or i == 13:
            print('*' * 10)
        else:
            print('*' + ' ' * 8 + '*')

draw_box() 
#2
def draw_triangle():
    for i in range(1, 11):
        print('*' * i)
draw_triangle()
#13.2
def print_fio(name, surname, patronymic):
    print(surname[0].upper() + name[0].upper() + patronymic[0].upper())
name, surname, patronymic = input(), input(), input()
print_fio(name, surname, patronymic)
#2
def print_case_counts(s):
    upper = 0
    lower = 0

    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print(f"Букв в верхнем регистре: {upper}")
    print(f"Букв в нижнем регистре: {lower}")

s = input()

print_case_counts(s)
#3
def print_digit_sum(num):
    total = 0
    for digit in str(num):
        total += int(digit)
    print(total)
n = int(input())
print_digit_sum(n)
#4
def print_sorted_hyphen(s):
    words = s.split('-')
    words.sort()
    print('-'.join(words))
s = input()
print_sorted_hyphen(s)
#5
# объявление функции
def draw_triangle(fill, base):
    mid = base // 2 + 1

    # вверх
    for i in range(1, mid + 1):
        print(fill * i)

    # вниз
    for i in range(mid - 1, 0, -1):
        print(fill * i)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
#6
# объявление функции
def print_perm_time_call(msc_time):
    hours, minutes = map(int, msc_time.split(':'))

    # прибавляем 2 часа
    hours = (hours + 2) % 24

    print(f"Созвон будет в {hours:02d}:{minutes:02d}.")

# считываем данные
msc_time = input()

# вызываем функцию
print_perm_time_call(msc_time)
#7
# объявление функции
def print_symbol_counts(s):
    s = s.lower()
    unique = sorted(set(s))
    
    for ch in unique:
        print(f"{ch}: {s.count(ch)}")

# считываем данные
s = input()

# вызываем функцию
print_symbol_counts(s)
#13.4
# объявление функции
def convert_to_miles(km):
    return km * 0.6214

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))
#2
# объявление функции
def code_format(text):
    return f"<code>{text}</code>"

# считываем данные
text = input()

# вызываем функцию
print(code_format(text))
#3
# объявление функции
def get_days(month):
    if month == 2:
        return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))
#4
# объявление функции
def math_round_to_int(num):
    integer = int(num)
    if num - integer < 0.5:
        return integer
    else:
        return integer + 1

# считываем данные
num = float(input())

# вызываем функцию
print(math_round_to_int(num))
#5
# объявление функции
def get_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
#6
# объявление функции
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]

def number_of_factors(num):
    return len(get_factors(num))

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))
#7
# объявление функции
def get_unique(numbers):
    unique = []
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique

# считываем данные
numbers = eval(input())

# вызываем функцию
print(get_unique(numbers))
#8
# объявление функции
def get_last_index(data, value):
    for i in range(len(data) - 1, -1, -1):
        if data[i] == value:
            return i
    return "ERROR!"

# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))
#9
# объявление функции
def find_all(target, symbol):
    indices = []
    for i in range(len(target)):
        if target[i] == symbol:
            indices.append(i)
    return indices

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))
#10
# объявление функции
def merge(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # добавляем оставшиеся элементы
    result.extend(list1[i:])
    result.extend(list2[j:])

    return result

# считываем данные
numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

# вызываем функцию
print(merge(numbers1, numbers2))
#11
def quick_merge(list1, list2):
    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


# считываем данные
n = int(input())
result = []

for _ in range(n):
    current = [int(x) for x in input().split()]
    result = quick_merge(result, current)

print(*result)
#13.5
# объявление функции
def is_valid_triangle(side1, side2, side3):
    return (side1 + side2 > side3 and
            side1 + side3 > side2 and
            side2 + side3 > side1)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
print(is_valid_triangle(a, b, c))
#2
# объявление функции
def is_palindrome(text):
    # приводим к нижнему регистру и убираем лишние символы
    cleaned = ''
    for ch in text.lower():
        if ch.isalnum():  # оставляем только буквы и цифры
            cleaned += ch

    # проверяем палиндром
    return cleaned == cleaned[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
#3
# объявление функции
def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False

    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return count == 1

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))
#4
# объявление функции
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))
#5
# объявление функции
def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
#6
# объявление функции
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
#7
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False

    has_upper = False
    has_lower = False
    has_digit = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    return has_upper and has_lower and has_digit

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
#8
# объявление функции
def is_correct_bracket(text):
    balance = 0

    for ch in text:
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            balance -= 1

        if balance < 0:
            return False

    return balance == 0

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))
#9
# объявление функции
def is_valid_password(password):
    parts = password.split(':')

    # должно быть ровно 3 части
    if len(parts) != 3:
        return False

    a, b, c = parts

    # a — палиндром
    if a != a[::-1]:
        return False

    # b — простое число
    b = int(b)
    if b <= 1:
        return False
    for i in range(2, int(b ** 0.5) + 1):
        if b % i == 0:
            return False

    # c — чётное число
    if int(c) % 2 != 0:
        return False

    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
#13.6
# объявление функции
def get_middle_point(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
#2
from math import pi

# объявление функции
def get_circle(radius):
    length = 2 * pi * radius
    square = pi * radius ** 2
    return length, square

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)
#3
# объявление функции
def solve(a, b, c):
    D = b**2 - 4*a*c
    sqrt_D = D ** 0.5

    x1 = (-b - sqrt_D) / (2 * a)
    x2 = (-b + sqrt_D) / (2 * a)

    return min(x1, x2), max(x1, x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)