#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    item_dicc = {}
    items_sorted = sorted(a_dictionary.items())
    item_dicc = dict(items_sorted)

    for key, value in item_dicc.items():
        print(f"{key}: {value}")
