# 1 
print("Здравствуй, мир!")
# 2
print(4, 8, 15, 16, 23, 42)
# 3
print(4)
print(8)
print(15)
print(16)
print(23)
print(42)
# 4
n = 7
for i in range(1, n + 1):
    print('*' * i)
# 5
name = input()
print(f"Привет, {name}")
# 6
team_name = input()
print(team_name + ' - чемпион!')
# 7
line1 = input()
line2 = input()
line3 = input()
print(line1)
print(line2)
print(line3)
# 8
line1 = input()
line2 = input()
line3 = input()
print(line3)
print(line2)
print(line1)
# 9
print('I', '*'*3, 'like', '*'*3, 'Python', sep='')
# 10
username = input()
print(f"Привет, {username}!")
# 11
separator = input()
first_string = input()
second_string = input()
third_string = input()
print(first_string, second_string, third_string, sep=separator)
# 12
number = int(input())
print(number)
print(number + 1)
print(number + 2)
# 13
a = int(input())
b = int(input())
c = int(input())
summa = a + b + c
print(summa)
# 14
monitor_price = int(input())
system_unit_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())
computer_cost = monitor_price + system_unit_price + keyboard_price + mouse_price
total_cost = computer_cost * 3
print(total_cost)
# 15
a = int(input())
b = int(input())
sum_ab = a + b    
cube_sum_ab = sum_ab * sum_ab * sum_ab 
square_b = b * b   
result = 3 * cube_sum_ab + 275 * square_b - 127 * a - 41
print(result)