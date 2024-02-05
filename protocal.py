from typing import Protocol
import math

class Shape(Protocol):
    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    circle: Shape = Circle(5)
    rectangle: Shape = Rectangle(10, 5)

    print(f"Circle Area: {circle.area()}")
    print(f"Circle Perimeter: {circle.perimeter()}")
    print(f"Rectangle Area: {rectangle.area()}")
    print(f"Rectangle Perimeter: {rectangle.perimeter()}")
