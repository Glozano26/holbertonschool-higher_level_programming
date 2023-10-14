#!/usr/bin/python3
"""Print square"""


def print_square(size):
    """Prints a square with # representing dimensions
    Arguments:
        size (int): size of square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            print("#" * size)
