#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    length = len(my_list) - 1
    l_copy = []
    if idx < 0 or idx > length:
        return [i for i in my_list]
    l_copy = [i for i in my_list]
    l_copy[idx] = element
    return l_copy
