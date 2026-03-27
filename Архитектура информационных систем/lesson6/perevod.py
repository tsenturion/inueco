translations = {
    "hello": "привет",
    "goodbye": "до свидания",
    "cat": "кот",
    "dog": "собака",
    "thank you": "спасибо",
    "please": "пожалуйста",
}

word = input("Введите английское слово для перевода: ").lower()

if word in translations:
    print(f"Перевод: {translations[word]}")
else:
    print("Извините, перевод для этого слова не найден.")