#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for let in range(len(str)):
        if let != n:
            new_str += str[let]
    return new_str
