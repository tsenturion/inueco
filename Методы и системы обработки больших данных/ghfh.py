import random

words = ['космос', 'игра', 'робот', 'машина', 'питон']
secret = random.choice(words)
attempts = 3

print("Угадай слово! У тебя есть 3 попытки.")

while attempts > 0:
    guess = input("Введите слово: ").lower()
    if guess == secret:
        print("Правильно! Ты выиграл!")
        break
    else:
        attempts -= 1
        print(f"Ошибся! Осталось попыток: {attempts}")

if attempts == 0:
    print(f"Ты проиграл! Загаданное слово было: {secret}")