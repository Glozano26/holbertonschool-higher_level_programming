#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number = 0
    c = 0
    try:
        for number in my_list:
            try:
                print('{:d}'.format(my_list[number]), end='')
                c += 1
            except ValueError:
                pass
            except TypeError:
                pass
        print()
        return c
