#!/usr/bin/python3
def uniq_add(my_list=[]):
    it = 0
    for item in set(my_list):
        it += item
    return it
