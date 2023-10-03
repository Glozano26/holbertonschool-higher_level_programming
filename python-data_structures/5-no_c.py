#!/usr/bin/python3
def no_c(my_string):
    del_char1 = "c"
    del_char2 = "C"
    new_str = ""
    for char in my_string:
        if char != del_char1 and char != del_char2:
            new_str += char
    return new_str
