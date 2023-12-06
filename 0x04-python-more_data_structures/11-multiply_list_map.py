#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return None if not my_list else [list(map(lambda x: x * number, my_list))]
