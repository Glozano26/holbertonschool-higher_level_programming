#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    my_list.sort()
    max_value = my_list[-1]
    return max_value
