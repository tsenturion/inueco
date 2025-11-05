class Animal:
    def __init__(self, name, species, age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} лет, {self.weight} кг)"

    def __repr__(self):
        return f"Animal('{self.name}', '{self.species}', {self.age}, {self.weight})"

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.species == other.species

    def __lt__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        return self.weight < other.weight

    def __add__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        
        # Вычисляем вес потомка - 10% от суммы весов родителей
        baby_weight = (self.weight + other.weight) * 0.1
        # Вид берем от первого родителя
        baby_species = self.species
        
        return Animal("Потомок", baby_species, 0, baby_weight)


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __str__(self):
        return f"Зоопарк '{self.name}': {len(self)} животных"

    def __len__(self):
        return len(self.animals)

    def __getitem__(self, index):
        # Поддержка срезов
        if isinstance(index, slice):
            return self.animals[index]
        return self.animals[index]

    def __contains__(self, item):
        # Проверка по объекту Animal
        if isinstance(item, Animal):
            return item in self.animals
        # Проверка по имени (строке)
        elif isinstance(item, str):
            return any(animal.name == item for animal in self.animals)
        return False

    def __add__(self, other):
        if not isinstance(other, Zoo):
            return NotImplemented
        
        new_zoo = Zoo("Объединенный")
        new_zoo.animals = self.animals + other.animals
        return new_zoo


# Демонстрация работы
if __name__ == "__main__":
    # Создание животных
    lion = Animal("Аристотель", "Лев", 5, 190)
    lioness = Animal("Зара", "Львица", 4, 150)
    elephant = Animal("Дамбо", "Слон", 10, 1500)
    
    print("=== Создание животных ===")
    print(lion)  # Аристотель (Лев, 5 лет, 190 кг)
    print(repr(lion))  # Animal('Аристотель', 'Лев', 5, 190)

    print("\n=== Сравнение животных ===")
    print(f"{lion} == {lioness}: {lion == lioness}")  # False (разные имена)
    print(f"{lion} < {elephant}: {lion < elephant}")  # True (190 < 1500)

    print("\n=== 'Размножение' животных ===")
    baby = lion + lioness
    print(baby)  

    print("\n=== Работа с зоопарком ===")
    zoo1 = Zoo("Сафари")
    zoo1.animals.extend([lion, lioness, baby])

    zoo2 = Zoo("Африканский")
    zoo2.animals.append(elephant)

    print(f"Количество животных в zoo1: {len(zoo1)}")  
    print(f"Первое животное в zoo1: {zoo1[0]}")  
    print(f"'Аристотель' в zoo1: {'Аристотель' in zoo1}")  # True
    print(f"{elephant} в zoo1: {elephant in zoo1}")  # False

    print("\n=== Работа со срезами ===")
    print("Первые два животных в zoo1:")
    for animal in zoo1[:2]:
        print(f"  - {animal}")

    print("\n=== Объединение зоопарков ===")
    big_zoo = zoo1 + zoo2
    print(f"{big_zoo}: {len(big_zoo)} животных")  
    
    print("\nВсе животные в объединенном зоопарке:")
    for animal in big_zoo:
            print(f"  - {animal}")