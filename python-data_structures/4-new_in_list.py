#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cop = my_list.copy()
    if idx < 0:
        list_cop = copy(my_list)
        return list_cop
    elif idx >= len(my_list):
        list_cop = copy(my_list)
        return list_cop
    else:
        list_cop[idx] = element
        return list_cop
