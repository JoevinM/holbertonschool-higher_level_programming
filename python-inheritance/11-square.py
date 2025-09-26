#!/usr/bin/python3

"""
Square class that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initialize a Square

        Args:
        size (int): The size of the square sides (must be > 0)
        """

        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square

        Returns:
            int: The area of the square
        """

        return self.__size * self.__size

    def __str__(self):
        """
        Return the string representation of the square

        Returns:
            str: Square description in the format [Square] <size>/<size>
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
