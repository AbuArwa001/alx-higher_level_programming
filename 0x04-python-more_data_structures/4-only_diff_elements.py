#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set_1.symmetric_difference(set_2)
    # res = set()
    # for y in set_1:
    #     if y not in set_2:
    #         res.add(y)
    # for x in set_2:
    #     if x not in set_1:
    #         res.add(x)
    # return res
