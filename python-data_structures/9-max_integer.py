#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    my_list.sort()
    my_list.reverse()
    return my_list[0]
