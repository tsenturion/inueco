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
        
       
        species = self.species
        
       
        weight = (self.weight + other.weight) * 0.1
        
        return Animal("Потомок", species, 0, weight)


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __str__(self):
        return f"Зоопарк '{self.name}': {len(self)} животных"

    def __len__(self):
        return len(self.animals)

    def __getitem__(self, index):
       
        if isinstance(index, slice):
            return self.animals[index]
        return self.animals[index]

    def __contains__(self, item):
        
        if isinstance(item, Animal):
            return item in self.animals
        
        
        if isinstance(item, str):
            return any(animal.name == item for animal in self.animals)
        
        return False

    def __add__(self, other):
        if not isinstance(other, Zoo):
            return NotImplemented
        
        
        new_zoo = Zoo("Объединенный")
        new_zoo.animals = self.animals + other.animals
        return new_zoo



if __name__ == "__main__":
    # Создание животных
    lion = Animal("Аристотель", "Лев", 5, 190)
    lioness = Animal("Зара", "Львица", 4, 150)
    elephant = Animal("Дамбо", "Слон", 10, 1500)
    
    print(lion)  
    print(repr(lion)) 

    # Сравнение животных
    print(lion == lioness)  
    print(lion < elephant)  

    
    baby = lion + lioness
    print(baby)  

    # Работа с зоопарком
    zoo1 = Zoo("Сафари")
    zoo1.animals.extend([lion, lioness, baby])

    zoo2 = Zoo("Африканский")
    zoo2.animals.append(elephant)

    print(len(zoo1))  
    print(zoo1[0])  
    print("Аристотель" in zoo1)  
    print(elephant in zoo1)  

   
    print("Первые два животных:")
    for animal in zoo1[:2]:
        print(f"  - {animal}")

    # Объединение зоопарков
    big_zoo = zoo1 + zoo2
    print(f"{big_zoo}: {len(big_zoo)} животных")  
    
    # Вывод всех животных в объединенном зоопарке
    print("\nВсе животные в объединенном зоопарке:")
    for animal in big_zoo:
        print(f"  - {animal}")