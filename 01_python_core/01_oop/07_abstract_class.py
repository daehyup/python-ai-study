# 07_abstract_class.py
# 학습일: 2026-06-24
# 개념: ABC 추상 클래스, @abstractmethod

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(4, 5)
print(r.area())       # 20
print(r.perimeter())  # 18

c = Circle(7)
print(c.area())       # 153.94 (π * r²)
print(c.perimeter())  # 43.98  (2 * π * r)