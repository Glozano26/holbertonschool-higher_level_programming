#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    returns: the number of characters added
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        return (file.write(text))
