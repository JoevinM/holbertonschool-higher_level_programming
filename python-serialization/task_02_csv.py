#!/usr/bin/env python3

"""
Module to convert a CSV file into a JSON file.
"""


import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert a CSV file into a JSON file with the same basename.

    Args:
        csv_file (str): Path to the CSV file.

    Returns:
        str: Path to the generated JSON file.
    """

    with open(csv_file, "r") as csvfile:
        csv_data = csv.DictReader(csvfile)
        with open("data.json", "w") as file_json:
            list_conv = []
            for row in csv_data:
                list_conv.append(row)
            json.dump(list_conv, file_json)
