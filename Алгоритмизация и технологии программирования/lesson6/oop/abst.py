from abc import ABC, abstractmethod
#создать абстрактный MClass с несколькими абстрактными методами\
# в другом файле импортировать его и реализовать в наследнике
class Animal(ABC):
    info = 'animal'

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def make_voice(self):
        pass

    @abstractmethod
    def walk(self):
        pass

class MClass(ABC):
    @classmethod
    @abstractmethod
    def add(cls):
        pass

    @classmethod
    @abstractmethod
    def substruct(cls):
        pass

