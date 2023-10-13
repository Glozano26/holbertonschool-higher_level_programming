#!/usr/bin/python3
"""Integers addition
Adds two integers (a, b) and returns integer sum
a and b int or float
Floats get converted to integers, all others raise TypeError
"""


def matrix_divided(matrix, div):
    """adds two integers
    Returns: integer sum
    """
    error_matriz = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(error_matriz)
    else:
        total = [[round(x / div, 2) for x in row] for row in matrix]
        row = len(matrix)
        column = len(matrix[0])

        for x in matrix:
            if len(x) != column:
                raise TypeError("Each row of the matrix must \
                have the same size")
    return total
