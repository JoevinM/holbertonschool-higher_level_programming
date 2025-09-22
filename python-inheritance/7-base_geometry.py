#!/usr/bin/python3
"""
Defines an empty class BaseGeometry.
This will serve as a base class for other geometry-related classes.
"""


class BaseGeometry:
    """
    BaseGeometry class.

    Defines the structure for geometry classes.
    Contains:
      - area(): raises an exception (to be implemented by subclasses).
      - integer_validator(): validates a given value is a positive integer.
    """
    pass

    def area(self):
        """
        Raises an Exception because area is not implemented.

        This method is meant to be overridden by subclasses
        to provide their own implementation of area calculation.

        Raises:
            Exception: Always with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that value is an integer greater than 0.

        Args:
            name (str): The name of the variable (used in the error message).
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
