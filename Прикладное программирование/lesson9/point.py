from dataclasses import dataclass
from functools import total_ordering


class CoordinateDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        print(f'getting {self.name}')
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError('value should be (int, float)')
        print(f'setting {self.name} to {value}')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print(f'deleting {self.name}')
        del instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name



class Point(CoordinateDescriptor):
    x = CoordinateDescriptor()
    y = CoordinateDescriptor()
    def __init__(self, x=None, y=None):
        self._x = x
        self._y = y

    def point_print(self):
        print(f'Point x={self._x}, y={self._y}')

    def __str__(self):
        return f'Point x={self._x}, y={self._y}'

    def __add__(self, other):
        if not isinstance(other, Point):
            return False
        return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return False
        return Point(self._x - other._x, self._y - other._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError('scalar must be (int, float)')
        return Point(self._x * scalar, self._y * scalar)

    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise ValueError('scalar must be (int, float)')
        if scalar == 0:
            raise ZeroDivisionError('нельзя 0')
        return Point(self._x / scalar, self._y / scalar)

    def __len__(self):
        if self._x is None and self._y is None:
            return 2
        elif self._x is None or self._y is None:
            return 1
        else:
            return 0

    def __getitem__(self, index):
        if index == 0:
            return self._x
        elif index == 1:
            return self._y
        else:
            raise IndexError('out of range')
    


p1 = Point(1, 2)
print(p1.x)
print(p1.y)
p1.x = 5
p1.y = 8
p1.point_print()
print(p1)
p2 = Point(1, 2)
p1 += p2
print(p1)
print(p1 == Point(6, 10))
print(p1[0])
print(p1[1])
p3 = Point()