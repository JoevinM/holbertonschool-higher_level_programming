#!/usr/bin/env python3
"""
Duck typing and Abstract Base Classes example:
- Abstract Shape class
- Circle and Rectangle implementations
- shape_info function using duck typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class Shape with abstract methods area and perimeter
    """

    @abstractmethod
    def area(self):
        """
        Compute the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape
    """

    def __init__(self, radius):
        """
        Initialize Circle with a radius
        """
        self.__radius = radius

    def area(self):
        """
        Return the area of the circle
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Return the perimeter (circumference) of the circle
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)


def shape_info(obj):
    """
    Print the area and perimeter of a shape object
    Relies on duck typing (expects obj to have area and perimeter)
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
