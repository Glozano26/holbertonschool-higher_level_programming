#!/usr/bin/python3
def print_last_digit(number):

    last_num = number % 10
    if number < 0:
        last_num = number % -10
        last_num *= -1
    print(f"{last_num}", end="")
    return last_num
