#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for number in my_list:
            if c < x:
                print(number, end="")
                c += 1
        print()
        return c
    except Exception as ex:
        return 0
