from animal import Animal

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __str__(self):
        return f"Зоопарк '{self.name}': {len(self)} животных"

    def __repr__(self):
        return f"Zoo('{self.name}', {self.animals})"

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
        # Проверка по имени животного (строка)
        elif isinstance(item, str):
            return any(animal.name == item for animal in self.animals)
        return False

    def __add__(self, other):
        if not isinstance(other, Zoo):
            return NotImplemented
        
        new_zoo = Zoo("Объединенный")
        new_zoo.animals = self.animals + other.animals
        return new_zoo

    def add_animal(self, animal):
        """Дополнительный метод для добавления животного"""
        if isinstance(animal, Animal):
            self.animals.append(animal)
        else:
            raise TypeError("Можно добавлять только объекты класса Animal")

    def remove_animal(self, animal):
        """Дополнительный метод для удаления животного"""
        if animal in self.animals:
            self.animals.remove(animal)