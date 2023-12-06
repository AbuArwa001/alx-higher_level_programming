#!/usr/bin/python3
def common_elements(set_1, set_2):
    result_set = {q for q, a in zip(set_1, set_2) if q in set_1 and q in set_2}
    return result_set
