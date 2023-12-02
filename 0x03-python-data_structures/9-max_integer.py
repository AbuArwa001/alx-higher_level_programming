#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return
    largest = 0
    for i in my_list:
        if largest > i:
            continue
        else:
            largest = i
    return largest
