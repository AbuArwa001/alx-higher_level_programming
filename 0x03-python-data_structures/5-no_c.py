#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    length = len(my_string) - 1
    new_str = "".join([i for i in my_string if i != 'c' and i != 'C'])
    return new_str
