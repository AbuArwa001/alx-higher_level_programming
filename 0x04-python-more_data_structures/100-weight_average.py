#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    avg = 0
    ttl = 0
    for i in my_list:
        avg += i[0] * i[1]
        ttl += i[1]
    return avg/ttl


# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
