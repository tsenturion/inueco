from animal import Animal

    #Коллекция животных
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    #Строковое представление зоопарка
    def __str__(self):
        return f"Зоопарк '{self.name}': {len(self)} животных"

    #Количество животных в зоопарке
    def __len__(self):
        return len(self.animals)

    #Доступ к животным по индексу или срезу
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.animals[index]
        return self.animals[index]

    #Проверка наличия животного в зоопарке
    def __contains__(self, item):
        if isinstance(item, Animal):
            return item in self.animals
        elif isinstance(item, str):
            return any(animal.name == item for animal in self.animals)
        return False

    #Сложение двух зоопарков
    def __add__(self, other):
        if not isinstance(other, Zoo):
            return NotImplemented
        
        new_zoo = Zoo("Объединенный")
        new_zoo.animals = self.animals + other.animals
        return new_zoo