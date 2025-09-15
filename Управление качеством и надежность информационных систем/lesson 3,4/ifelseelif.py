"""
if - если, с пробелом после if, с : в конце
if обязательный
вместо age > 18 можно любое булево выражение
если в условии образуется True, то выполняется первый блок кода внутри if
если в условии образуется False, то выполняется второй блок кода внутри else
else без условия, но с : в конце
else не обязателен
elif
"""
print(print())
age = int(input("Enter your age: "))

if age > 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


if True and 6 < 5 or not False:
    print("True")

flag1 = True

if flag1:
    print("True")

"""
False:
0
""
''
[]
()
{}
set()
frozenset()

None

True:
когда есть что-то
"""

if 0:
    if 0:
        print("True")
    else:
        if 0:
            if 0:
                print("True")
            else:
                print("False")
        else:
            print("False")
else:
    print("False")


mark = int(input("Enter your mark: "))

if mark >= 80:
    print("A")
elif mark >= 60:
    print("B")
elif mark >= 40:
    print("C")
else:
    print("D")

"""
<<<<<<< HEAD
опередить возраст
>65 пожилой
>18 совершеннолетний
<18 несовереннолетний
"""

age = int(input("Введите свой возраст: "))
if age>65:
    print("Ты пожилой человек, держись там :)")
elif age >= 18:
    print("Ты сорешеннолетний, тебя вся жизнь впереди, живи полной жизнью)")
else:
    print("Тебе ещё даже 18 нет, так что учись пока, дальше всё будет только сложнее, наслаждайся жизьню пока можешь, дальше будут хуже")

=======
определить возраст
> 65 пожилой
> 18 совершеннолетний
< 18 несовершеннолетний
"""

# age = 12
age = int(input("Enter your age: "))

if age > 65:
    print("пожилой")
elif age >= 18:
    print("совершеннолетний")
else:
    print("несовершеннолетний")
>>>>>>> 81c9451d9398857c3c34ebb6e0ad6e8c716c96d5
