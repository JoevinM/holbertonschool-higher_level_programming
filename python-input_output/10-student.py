#!/usr/bin/python3
"""
Defines a Student class with a JSON-friendly dictionary representation
that can be filtered by attribute names.
"""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional):
            List of attribute names (strings) to include.
                If None or not a list of strings, all attributes are returned.

        Returns:
            dict: Dictionary of requested attributes or all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__
