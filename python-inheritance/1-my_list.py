#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """that prints the list, but sorted ascending sort.
    You can assume that all the elements of the list will be of type int.
    """
    def print_sorted(self):
        print(sorted(self))
