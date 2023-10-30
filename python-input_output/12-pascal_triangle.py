#!/usr/bin/python3

def pascal_triangle(n):
    if n == 0:
        return [1]
        fila_anter = pascal_triangle(n - 1)
    if n == 1:
        return [1]
    else:
        return []