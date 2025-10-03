#!/usr/bin/python3
"""
Module for demonstrating pickling and unpickling
custom Python objects using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom Python class with basic attributes and methods
    for serialization and deserialization using pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the attributes of the object in a readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The file to which the object will be saved.

        Returns:
            bool: True if serialization succeeds, False otherwise.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except (FileNotFoundError, pickle.PickleError, OSError):
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Args:
            filename (str): The file from which the object will be loaded.

        Returns:
            CustomObject: An instance of CustomObject if successful,
            None if the file is missing or malformed.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (FileNotFoundError, pickle.PickleError, OSError, EOFError):
            return None
