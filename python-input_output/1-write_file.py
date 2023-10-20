#!/usr/bin/python3
"""Write to a file"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    return: number of characters written
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return (file.write(text))
