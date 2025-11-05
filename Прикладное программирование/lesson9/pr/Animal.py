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
        if isinstance(other, Animal):
            return self.name == other.name and self.species == other.species
        return False

    def __lt__(self, other):
        if isinstance(other, Animal):
            return self.weight < other.weight
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Animal):
            new_name = "Потомок"
            new_species = self.species
            new_age = 0
            new_weight = (self.weight + other.weight) * 0.1
            return Animal(new_name, new_species, new_age, new_weight)
        return NotImplemented
