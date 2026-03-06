# 1
b1 = int(input())
q = int(input())
n = int(input())
bn = b1 * (q ** (n - 1))
print(bn)
# 2
cm = int(input())
meters = cm // 100
print(meters)
# 3
n = int(input())  # количество школьников
k = int(input())  # количество мандаринов

print(k // n)  # мандаринов каждому школьнику
print(k % n)   # мандаринов останется в корзине
# 4
n = int(input())
survivors = (n + 1) // 2  # округление вверх при делении на 2
print(survivors)
# 5
minutes = int(input())
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} мин - это {hours} час {remaining_minutes} минут.")
# 6
seat = int(input())
compartment = (seat - 1) // 4 + 1
print(compartment)
# 7
number = int(input())
digit1 = number // 100
digit2 = (number // 10) % 10
digit3 = number % 10

sum_digits = digit1 + digit2 + digit3
product_digits = digit1 * digit2 * digit3

print(f"Сумма цифр = {sum_digits}")
print(f"Произведение цифр = {product_digits}")
# 8
number = int(input())
a = number // 100
b = (number // 10) % 10
c = number % 10

print(f"{a}{b}{c}")
print(f"{a}{c}{b}")
print(f"{b}{a}{c}")
print(f"{b}{c}{a}")
print(f"{c}{a}{b}")
print(f"{c}{b}{a}")
# 9
number = int(input())
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

print(f"Цифра в позиции тысяч равна {thousands}")
print(f"Цифра в позиции сотен равна {hundreds}")
print(f"Цифра в позиции десятков равна {tens}")
print(f"Цифра в позиции единиц равна {units}")
# 10
print("Здравствуй, мир!")
# 11
print(4)
print(8)
print(15)
print(16)
print(23)
print(42)
# 12
print(4, 8, 15, 16, 23, 42)
# 13
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")
# 14
name = input()
print(f"Привет, {name}")
#15
team = input()
print(f"{team} - чемпион!")
#16
line1 = input()
line2 = input()
line3 = input()
print(line1)
print(line2)
print(line3)
#17
line1 = input()
line2 = input()
line3 = input()
print(line3)
print(line2)
print(line1)
# 18
print("I", "like", "Python", sep="***")
# 19
name = input()
print("Привет, ", end="")
print(name, end="!")
# 20
separator = input()
str1 = input()
str2 = input()
str3 = input()
print(str1, str2, str3, sep=separator)
