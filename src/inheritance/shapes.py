import json
import math
from abc import ABC, abstractmethod


class JSONMixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class Shape(ABC, JSONMixin):
    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * pow(self.radius, 2)

    def get_perimeter(self) -> float:
        return math.pi * self.radius * 2


class Rectangle(Shape):
    def __init__(self, length: int, width: int):
        self.width = width
        self.length = length

    def get_area(self) -> float:
        return self.width * self.length

    def get_perimeter(self) -> float:
        return self.width * 2 + self.length * 2


class Square(Rectangle):
    def __init__(self, side: int):
        super().__init__(side, side)
