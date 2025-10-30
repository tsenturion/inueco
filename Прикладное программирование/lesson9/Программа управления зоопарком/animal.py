class Animal:
    
    #Представление животных в зоопарке
    def __init__(self, name, species, age, weight):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    #Cтроковое представление животного
    def __str__(self):
        return f"{self.name} ({self.species}, {self.age} лет, {self.weight} кг)"
    
    #Cтроковое представление для воссоздания объекта
    def __repr__(self):
        return f"Animal('{self.name}', '{self.species}', {self.age}, {self.weight})"

    #Проверка равенства двух животных по имени и виду
    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.species == other.species
    
    #Сравнение животных по весу
    def __lt__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        return self.weight < other.weight
    
    #Cоздание потомка
    def __add__(self, other):
        if not isinstance(other, Animal):
            return NotImplemented
        
        baby_weight = (self.weight + other.weight) * 0.1
        baby_species = self.species
        
        return Animal("Потомок", baby_species, 0, baby_weight)