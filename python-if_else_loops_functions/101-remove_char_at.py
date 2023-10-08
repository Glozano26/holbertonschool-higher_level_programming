#!/usr/bin/env python3
def remove_char_at(str, n):
    if 0 <= n < len(str):
        new_string = str[:n] + str[n + 1:]
        return new_string
    else:
        return str
