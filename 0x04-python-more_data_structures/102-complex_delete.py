#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for x, y in a_dictionary.items():
        if y is value:
            keys.append(x)
    for i in keys:
        del a_dictionary[i]
    return a_dictionary
