class Animal:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def make_voice(self):
        print(f'{self.name} maked voice')

class Cat(Animal):
    def __init__(self, name, height, weight, color):
        super().__init__(name, height, weight)
        self.color = color

    def greet(self):
        super().make_voice()

cat = Animal('вася', 12, 12)

Cat = Cat('вася', 12, 12, 'black')
Cat.make_voice()
Cat.greet()

# MClass от него унаследовать в тригонометрию
# в триг мат функции
# иниц предыдущее и 1 новое
# из триг вызвать методы MClass