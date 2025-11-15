from Animal import Animal
from Zoo import Zoo

if __name__ == "__main__":
    # Создание животных
    lion = Animal("Аристотель", "Лев", 5, 190)
    lioness = Animal("Зара", "Львица", 4, 150)
    elephant = Animal("Дамбо", "Слон", 10, 1500)
    print(lion) # Аристотель (Лев, 5 лет, 190 кг)
    print(repr(lion)) # Animal('Аристотель', 'Лев', 5, 190)

    # Сравнение животных
    print(lion == lioness) # False (разные имена)
    print(lion < elephant) # True (190 < 1500)

    # "Размножение" животных
    baby = lion + lioness
    print(baby) # Потомок (Лев, 0 лет, 34.0 кг)

    # Работа с зоопарком
    zoo1 = Zoo("Сафари")
    zoo1.animals.extend([lion, lioness, baby])

    zoo2 = Zoo("Африканский")
    zoo2.animals.append(elephant)

    print(len(zoo1)) # 3
    print(zoo1[0]) # Аристотель (Лев, 5 лет, 190 кг)
    print("Аристотель" in zoo1) # True
    print(elephant in zoo1) # False

    # Объединение зоопарков
    big_zoo = zoo1 + zoo2
    print(f"{big_zoo}: {len(big_zoo)} животных") # Зоопарк 'Объединенный': 4 животных
