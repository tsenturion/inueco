from typing import Union
from animal import Animal

class Zoo:
    def __init__(self, name: str, animals: list[Animal] | None = None):
        self.name = name
        self.animals = animals if animals is not None else []

    def __str__(self):
        return f"Зоопарк '{self.name}': {len(self.animals)} животных"
    
    def __len__(self):
        return len(self.animals)

    def __getitem__(self, index: Union[int, slice]) -> Union[Animal, 'Zoo']:
        if isinstance(index, slice):
            return Zoo(self.name, self.animals[index])
        return self.animals[index]
    
    def __contains__(self, item):
        if isinstance(item, str):
            return item in [animal.name for animal in self.animals]
        return item in self.animals

    def __add__(self, other):
        return Zoo("Объединённый", [*self.animals, *other.animals])