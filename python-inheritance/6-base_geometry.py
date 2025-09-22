#!/usr/bin/python3
"""
Defines an empty class BaseGeometry.
This will serve as a base class for future geometry-related classes.
"""


class BaseGeometry:
    """
    BaseGeometry class.

    Defines the structure for geometry classes.
    Contains the method area() which must be implemented
    by any subclass.
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
