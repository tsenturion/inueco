from animal import Animal
from zoo import Zoo

def main():
    print("=== ВИРТУАЛЬНЫЙ ЗООПАРК ===\n")
    
    # Создание животных
    lion = Animal("Аристотель", "Лев", 5, 190)
    lioness = Animal("Зара", "Львица", 4, 150)
    elephant = Animal("Дамбо", "Слон", 10, 1500)
    penguin = Animal("Пингви", "Пингвин", 2, 15)
    
    print("=== ИНФОРМАЦИЯ О ЖИВОТНЫХ ===")
    print(lion)  # Аристотель (Лев, 5 лет, 190 кг)
    print(repr(lion))  # Animal('Аристотель', 'Лев', 5, 190)
    print(elephant)
    print(penguin)

    print("\n=== СРАВНЕНИЕ ЖИВОТНЫХ ===")
    print(f"{lion.name} == {lioness.name}: {lion == lioness}")  # False
    print(f"{lion.name} == Аристотель (другой): {lion == Animal('Аристотель', 'Лев', 3, 180)}")  # True
    print(f"{lion.name} < {elephant.name}: {lion < elephant}")  # True
    print(f"{penguin.name} > {elephant.name}: {penguin > elephant}")  # False

    print("\n=== 'РАЗМНОЖЕНИЕ' ЖИВОТНЫХ ===")
    baby_lion = lion + lioness
    print(f"{lion.name} + {lioness.name} = {baby_lion}")

    print("\n=== РАБОТА С ЗООПАРКАМИ ===")
    # Создание зоопарков
    zoo1 = Zoo("Сафари")
    zoo1.add_animal(lion)
    zoo1.add_animal(lioness)
    zoo1.add_animal(baby_lion)

    zoo2 = Zoo("Африканский")
    zoo2.add_animal(elephant)
    zoo2.add_animal(penguin)

    print(zoo1)
    print(zoo2)
    
    print(f"\nКоличество животных в {zoo1.name}: {len(zoo1)}")
    print(f"Количество животных в {zoo2.name}: {len(zoo2)}")

    print(f"\nПервое животное в {zoo1.name}: {zoo1[0]}")
    print(f"Последнее животное в {zoo2.name}: {zoo2[-1]}")

    # Демонстрация работы срезов
    print(f"\nПервые два животных в {zoo1.name}:")
    for animal in zoo1[:2]:
        print(f"  - {animal}")

    print(f"\n=== ПРОВЕРКА НАЛИЧИЯ ЖИВОТНЫХ ===")
    print(f"Есть ли 'Аристотель' в {zoo1.name}: {'Аристотель' in zoo1}")
    print(f"Есть ли 'Дамбо' в {zoo1.name}: {'Дамбо' in zoo1}")
    print(f"Есть ли {elephant.name} в {zoo2.name}: {elephant in zoo2}")
    print(f"Есть ли {lion.name} в {zoo2.name}: {lion in zoo2}")

    print("\n=== ОБЪЕДИНЕНИЕ ЗООПАРКОВ ===")
    big_zoo = zoo1 + zoo2
    print(f"Результат объединения: {big_zoo}")
    print(f"Всего животных в объединенном зоопарке: {len(big_zoo)}")

    print("\n=== ВСЕ ЖИВОТНЫЕ В ОБЪЕДИНЕННОМ ЗООПАРКЕ ===")
    for i, animal in enumerate(big_zoo, 1):
        print(f"{i}. {animal}")

    print("\n=== СОРТИРОВКА ЖИВОТНЫХ ПО ВЕСУ ===")
    sorted_animals = sorted(big_zoo.animals)
    for i, animal in enumerate(sorted_animals, 1):
        print(f"{i}. {animal.name}: {animal.weight} кг")

    print("\n=== ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ ===")
    # Создание нового животного через сложение разных видов
    exotic_baby = lion + penguin
    print(f"Эксперимент: {lion.name} + {penguin.name} = {exotic_baby}")

    # Проверка добавления животного в зоопарк
    big_zoo.add_animal(exotic_baby)
    print(f"\nПосле добавления экзотического потомка: {big_zoo}")

if __name__ == "__main__":
    main()