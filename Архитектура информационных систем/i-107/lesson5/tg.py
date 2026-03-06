#Яндекс Python 2.2
#A
name = input()
mood = input()
print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if mood == "хорошо":
    print("Я за Вас рада!")
else:
    print("Всё наладится!")
#B
petya_speed = int(input())
vasya_speed = int(input())
if petya_speed > vasya_speed:
    print("Петя")
else:
    print("Вася")
#C
petya = int(input())
vasya = int(input())
tolya = int(input())
if petya > vasya and petya > tolya:
    print("Петя")
elif vasya > petya and vasya > tolya:
    print("Вася")
else:
    print("Толя")
#D
petya = int(input())
vasya = int(input())
tolya = int(input())
if petya > vasya and petya > tolya:
    first = "Петя"
    if vasya > tolya:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif vasya > petya and vasya > tolya:
    first = "Вася"
    if petya > tolya:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
else:
    first = "Толя"
    if petya > vasya:
        second = "Петя"
        third = "Вася"
    else:
        second = "Вася"
        third = "Петя"

print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")
#E
a = int(input())
b = int(input())
petya = 6 + a
vasya = 12 + b
if petya > vasya:
    print("Петя")
else:
    print("Вася")
#F
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")
#G
number = input()
if number[0] == number[3] and number[1] == number[2]:
    print("YES")
else:
    print("NO")
#H
text = input()
if "зайка" in text:
    print("YES")
else:
    print("NO")
#I
n1 = input()
n2 = input()
n3 = input()
if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)
#J
n = int(input())
h = n // 100
a = (n // 10) % 10
b = n % 10
sum1 = a + b        
sum2 = h + a     
if sum1 > sum2:
    print(f"{sum1}{sum2}")
else:
    print(f"{sum2}{sum1}")
#K
n = int(input())
a = n // 100          
b = (n // 10) % 10    
c = n % 10            
if a >= b and a >= c:
    maxi = a
elif b >= a and b >= c:
    maxi = b
else:
    maxi = c

if a <= b and a <= c:
    mini = a
elif b <= a and b <= c:
    mini = b
else:
    mini = c
middle = a + b + c - maxi - mini
if mini + maxi == middle * 2:
    print("YES")
else:
    print("NO")
#L
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")
#M
n1 = input()
n2 = input()
n3 = input()
if n1[0] == n2[0] == n3[0]:
    print(n1[0])
elif n1[1] == n2[1] == n3[1]:
    print(n1[1])
#Q
n1 = input()
n2 = input()
a = int(n1[0])
b = int(n1[1])
c = int(n2[0])
d = int(n2[1])
if a >= b and a >= c and a >= d:
    maxi = a
elif b >= a and b >= c and b >= d:
    maxi = b
elif c >= a and c >= b and c >= d:
    maxi = c
else:
    maxi = d
if a <= b and a <= c and a <= d:
    mini = a
elif b <= a and b <= c and b <= d:
    mini = b
elif c <= a and c <= b and c <= d:
    mini = c
else:
    mini = d
total = a + b + c + d
sum = total - maxi - mini
middle = sum % 10
number = maxi * 100 + middle * 10 + mini
print(number)
#R
a = float(input())
b = float(input())
c = float(input())
if a >= b and a >= c:
    longest = a
    side1 = b
    side2 = c
elif b >= a and b >= c:
    longest = b
    side1 = a
    side2 = c
else:
    longest = c
    side1 = a
    side2 = b
if longest2 < side12 + side2**2:
    print("крайне мала")
elif longest2 > side12 + side2**2:
    print("велика")
else:
    print("100%")
#T
str1 = input()
str2 = input()
str3 = input()
result = []
if "зайка" in str1:
    result.append(str1)
if "зайка" in str2:
    result.append(str2)
if "зайка" in str3:
    result.append(str3)
result.sort()
print(result[0], len(result[0]))