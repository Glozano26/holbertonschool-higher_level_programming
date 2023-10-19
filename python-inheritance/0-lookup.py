#!/usr/bin/python3
"""Lookup"""
def lookup(obj):
    """function that returns the list
    of available attributes and methods of an object
    Returns a list object
    """
    list = obj
    return (dir(list))
