class Animal:
    def __init__(self, name: str, species: str, age: int, weight: float):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} лет, {self.weight} кг)"
    
    def __repr__(self):
        return f"Animal(name={self.name!r}, species={self.species!r}, age={self.age!r}, weight={self.weight!r})"
    
    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.species == other.species
    
    def __lt__(self, other):
        return self.weight < other.weight

    def __add__(self, other):
        return Animal('Потомок', self.species, 0, (self.weight + other.weight) * 0.1)
    
