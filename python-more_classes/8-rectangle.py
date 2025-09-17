#!/usr/bin/python3
"""
This module defines a class Rectangle
that represents a geometric rectangle.
The Rectangle class manages width, height,
number of instances, print symbol, and includes
a static method to compare rectangles by area.
"""


class Rectangle:
    """
    This class defines a rectangle structure.
    It allows instantiation with optional width and height,
    including type and value validation.

    number_of_instances (int): Tracks the number of Rectangle instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance with optional width and height.
        Increment the number_of_instances counter.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        area = self.width * self.height

        return area

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
                 Returns 0 if either width or height is 0.
        """
        perimeter = 0
        if self.width == 0 or self.height == 0:
            return perimeter
        else:
            perimeter = (self.width * 2) + (self.height * 2)
            return perimeter

    def __str__(self):
        """
        Return the "informal" string representation of the rectangle,
        using the '#' character to draw the shape.

        Returns:
        str: A string visualizing the rectangle with '#' characters.
             If width or height is 0, returns an empty string.
        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return ((str(self.print_symbol) *
                    self.width + "\n") * self.height)[:-1]

    def __repr__(self):

        """
        Return a string representation of the rectangle that can be used
        to recreate the same instance using eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when an instance is deleted and
        decrement the instance counter."""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area.

        Args:
            rect_1 (Rectangle): First rectangle
            rect_2 (Rectangle): Second rectangle

        Raises:
            TypeError: If either rect_1 or rect_2 is not a Rectangle

        Returns:
            Rectangle: Rectangle with larger area, or rect_1 if equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
