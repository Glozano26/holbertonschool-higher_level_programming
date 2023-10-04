#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for i in sorted(set(my_list)):
        new_list.append(i)
    return sum(new_list)
