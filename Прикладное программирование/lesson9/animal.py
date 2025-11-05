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
        
        # Определяем вид потомка (берем вид первого родителя)
        child_species = self.species
        # Вес потомка = 10% от суммы весов родителей
        child_weight = (self.weight + other.weight) * 0.1
        
        return Animal("Потомок", child_species, 0, child_weight)