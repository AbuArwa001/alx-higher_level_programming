#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return
    length = len(my_string) - 1
    new_str = ""
    return new_str.join([i for i in my_string if i != 'c' if i != 'C'])
