"""
вводить возраст с консоли и печатать его на экран. Возраст должен быть int
пока не будет введено exit
"""


flag = False
while flag != True:
    age = input("Введите свой возраст: ")
    if age == "exit" or age == "Exit" or age == "EXIT":
        flag = True
    else: int(age)
    print (age)
else:
    print("Введён Exit завершаем цикл!")

