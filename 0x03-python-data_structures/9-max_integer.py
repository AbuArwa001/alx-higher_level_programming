#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    largest = 0
    for i in my_list:
        if largest > i:
            continue
        else:
            largest = i
    return largest
