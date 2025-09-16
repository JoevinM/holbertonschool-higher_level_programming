#!/usr/bin/python3
"""
This module defines a class Square that represents a geometric square.
The Square class validates size and position on instantiation
and can compute its area and print itself.
"""


class Square:
    """
    This is a class that defines a square structure.
    The class allows you to set the size and position
    with type and value validation.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance with optional size and position.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): 2 positive integers representing the
                horizontal and vertical offsets (default is (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not
            a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Compute and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#',
        taking into account the position attribute.

        Behavior:
            - If size is 0, prints an empty line.
            - Otherwise, prints spaces before the square
              according to position, then the square itself.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
