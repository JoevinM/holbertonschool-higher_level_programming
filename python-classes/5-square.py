#!/usr/bin/python3
"""
This module defines a class Square that represents a geometric square.
The Square class validates size on instantiation and can compute its area.
"""


class Square:

    """
    This is a class that defines a square structure.
    At this stage, the class allows you to set the
    size with type and value validation.
    """

    def __init__(self, size=0):

        """
        Initialize a new Square instance with optional size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size

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

    def area(self):
        """
        Compute and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square with the character '#'.

        Behavior:
            - If size is 0, prints an empty line.
            - Otherwise, prints size lines, each containing size '#' characters
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
