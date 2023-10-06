#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            total = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            total = 0
            print(f"division by {total}")
        except TypeError:
            total = 0
            print("wrong type")
        except IndexError:
            total = 0
            print("out of range")
        finally:
            new_list.append(total)
    return new_list
