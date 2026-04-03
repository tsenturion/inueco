import random

print("Добро пожаловать в игру 'Угадай число'!")

# Загадываем число от 1 до 100
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Введите своё предположение (от 1 до 100): "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("Пожалуйста, введите число в диапазоне от 1 до 100.")
        elif guess < secret_number:
            print("Моё число больше.")
        elif guess > secret_number:
            print("Моё число меньше.")
        else:
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break
    except ValueError:
        print("Пожалуйста, введите правильное число.")