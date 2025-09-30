#!/usr/bin/python3
"""
Module that defines a function to load a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Lire un fichier JSON et le convertir en objet Python.

    Args:
        filename (str): le nom du fichier contenant les données JSON.

    Returns:
        object: l’objet Python obtenu après avoir décodé le contenu JSON.
    """
    with open(filename) as f:
        return json.load(f)
