#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """Write a function that reads a text file (UTF8) and prints it to stdout"""
    with open('my_file_0.txt', 'r', encoding="utf-8") as file:
        contenido = file.read()
        print(contenido, end="")
