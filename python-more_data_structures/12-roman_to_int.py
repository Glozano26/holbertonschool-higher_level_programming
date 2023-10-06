#!/usr/bin/python3
def roman_to_int(roman_string):
    n_roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    while i < len(roman_string):
        vlr = n_roma[roman_string[i]]
        if i + 1 < len(roman_string) and n_roma[roman_string[i + 1]] > vlr:
            total = total - vlr
        else:
            total += vlr

        i = i + 1
    return total
