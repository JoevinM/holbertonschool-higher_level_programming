#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    result = 0
    temp = 0

    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for roman_int in reversed(roman_string):
        for key, value in roman.items():
            if roman_int == key:
                if value < temp:
                    result -= value
                    break
                if value > temp:
                    result += value
                    break
            temp = value
    return result
