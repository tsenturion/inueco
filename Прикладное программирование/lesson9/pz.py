"""### Практическое задание

Вы создаете программу для управления виртуальным зоопарком. 


### **Класс `Animal`**

Реализуйте класс `Animal`, который представляет одно животное.

**Атрибуты:**
*   `name` (str): кличка животного.
*   `species` (str): вид животного (например, "лев", "слон", "пингвин").
*   `age` (int): возраст животного в годах.
*   `weight` (float): вес животного в килограммах.

**Магические методы для реализации в `Animal`:**

1.  **`__init__(self, name, species, age, weight)`**
    *   Конструктор класса. Инициализирует все атрибуты.

2.  **`__str__(self)`**
    *   Должен возвращать строку в формате: `"Аристотель (Лев, 5 лет, 190 кг)"`.
    *   Используется функциями `print()` и `str()`.

3.  **`__repr__(self)`**
    *   Должен возвращать строку, которую можно использовать для повторного создания объекта, например: `"Animal('Аристотель', 'Лев', 5, 190)"`.
    *   Используется в интерпретаторе и функцией `repr()`.

4.  **`__eq__(self, other)`**
    *   Определяет поведение оператора равенства `==`.
    *   Два животных считаются равными, если совпадают их `name` и `species`.

5.  **`__lt__(self, other)`**
    *   Определяет поведение оператора "меньше" `<`.
    *   Сравнение должно производиться по весу животного. Позволит сортировать животных по весу.

6.  **`__add__(self, other)`**
    *   Определяет поведение оператора сложения `+`.
    *   При сложении двух животных (`animal1 + animal2`) должен возвращаться **новый объект** класса `Animal`.
    *   **Логика:** Новое животное получает имя "Потомок", вид определяется как вид первого животного, возраст = 0, вес = 10% от суммы весов родителей.
    *   *Пример:* `Аристотель (Лев) + Зара (Львица) = Потомок (Лев, 0 лет, 25.5 кг)`


### **Класс `Zoo`**

Реализуйте класс `Zoo`, который представляет собой коллекцию животных.

**Атрибуты:**
*   `animals` (list): список объектов `Animal`, находящихся в зоопарке.

**Магические методы для реализации в `Zoo`:**

1.  **`__init__(self, name)`**
    *   Конструктор. Принимает название зоопарка. Инициализирует пустой список `animals`.

2.  **`__str__(self)`**
    *   Возвращает строку: `"Зоопарк 'Сафари': 5 животных"`.

3.  **`__len__(self)`**
    *   Возвращает количество животных в зоопарке с помощью функции `len()`.

4.  **`__getitem__(self, index)`**
    *   Позволяет обращаться к животным по индексу: `zoo[0]` вернет первого животного.
    *   **Бонус:** Реализуйте поддержку срезов (slicing).

5.  **`__contains__(self, item)`**
    *   Позволяет использовать оператор `in` для проверки наличия животного в зоопарке.
    *   Должен работать как при передаче объекта `Animal`, так и при передаче клички (строка). `zoo.contains(animal1)` или `zoo.contains("Аристотель")`.

6.  **`__add__(self, other)`**
    *   Позволяет объединять два зоопарка с помощью оператора `+`.
    *   Должен возвращать **новый объект** `Zoo` с названием "Объединенный зоопарк", в котором находятся животные из обоих исходных зоопарков.


### **Задача**

1.  Реализуйте класс `Animal` со всеми указанными магическими методами.
2.  Реализуйте класс `Zoo` со всеми указанными магическими методами.
3.  Протестируйте код на демонстрации.

**main демонстрации:**"""

class Animal:

    def init(self, name: str, species: str, age: int, weight: float):
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight

    def get_info(self) -> str:
            #Возвращение информации о животном
        return f"{self.name} ({self.species}, {self.age} лет, {self.weight} кг)"

    def get_representation(self) -> str:
            #Воссоздание объекта
        return f"Animal('{self.name}', '{self.species}', {self.age}, {self.weight})"

    def is_equal_to(self, other) -> bool:
            #Сравнение животных
        if not isinstance(other, Animal):
            return False
        return self.name == other.name and self.species == other.species

    def is_lighter_than(self, other) -> bool:
            #Сравнение весах животных
        if not isinstance(other, Animal):
            return NotImplemented
        return self.weight < other.weight

    def reproduce_with(self, other):
            #Потомок от двух животных
        if not isinstance(other, Animal):
            return None
        new_weight = (self.weight + other.weight) * 0.1
        return Animal("Потомок", self.species, 0, new_weight)


class Zoo:
    
    def init(self, name: str):
        self.name = name
        self.animals = []

    def get_info(self) -> str:
            #Информация о зоопарке 
        count = self.get_animal_count()
        return f"Зоопарк '{self.name}': {count} животных"

    def get_animal_count(self) -> int:
            #Количество живтных в зоопарке 
        return len(self.animals)

    def get_animal_at(self, index):
            #Животное по индексу
        return self.animals[index]

    def has_animal(self, item) -> bool:
            #Есть ли животное в зоопарке 
        if isinstance(item, Animal):
            return item in self.animals
        if isinstance(item, str):
            return any(animal.name == item for animal in self.animals)
        return False

    def merge_with(self, other):
            #Объединение двух зоопарков
        if not isinstance(other, Zoo):
            return None
        new_zoo = Zoo("Объединенный зоопарк")
        new_zoo.animals = self.animals + other.animals
        return new_zoo

if __name__ == '__main__':
        #Создание животных
    lion = Animal("Аристотель", "Лев", 5, 190)
    lioness = Animal("Зара", "Львица", 4, 150)
    elephant = Animal("Дамбо", "Слон", 10, 1500)
    print("Демонстрация класса Animal")
    print(lion.get_info()) 
    print(lion.get_representation())

        #Сравнение животных
    print("\n Сравнение животных")
    print(f"Аристотель равен Заре: {lion.is_equal_to(lioness)}")
    print(f"Аристотель легче Дамбо: {lion.is_lighter_than(elephant)}")

        #Размножение животных
    print("\n Сложение животных")
    baby = lion.reproduce_with(lioness)
    print(baby.get_info())

        #Работа с зоопарком
    print("\n Демонстрация класса Zoo")
    zoo1 = Zoo("Сафари")
    zoo1.animals.extend([lion, lioness, baby])

    zoo2 = Zoo("Африканский")
    zoo2.animals.append(elephant)
    print(f"Количество животных в '{zoo1.name}': {zoo1.get_animal_count()}")
    animal_at_0 = zoo1.get_animal_at(0)
    print(f"Первое животное в '{zoo1.name}': {animal_at_0.get_info()}")
    print(f"Есть ли 'Аристотель' в '{zoo1.name}': {zoo1.has_animal('Аристотель')}")
    print(f"Есть ли 'Дамбо' в '{zoo1.name}': {zoo1.has_animal(elephant)}")

        #Объединение зоопарков
    print("\n Объединение зоопарков")
    big_zoo = zoo1.merge_with(zoo2)
    print(f"{big_zoo.get_info()}")