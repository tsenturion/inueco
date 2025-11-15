from Animal import Animal
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def __str__(self):
        return f"Зоопарк '{self.name}': {len(self.animals)} животных"

    def __len__(self):
        return len(self.animals)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.animals[index]
        return self.animals[index]

    def __contains__(self, item):
        if isinstance(item, Animal):
            return any(animal == item for animal in self.animals)
        elif isinstance(item, str):
            return any(animal.name == item for animal in self.animals)
        return False

    def __add__(self, other):
        if isinstance(other, Zoo):
            new_zoo = Zoo("Объединенный")
            new_zoo.animals = self.animals + other.animals
            return new_zoo
        return NotImplemented