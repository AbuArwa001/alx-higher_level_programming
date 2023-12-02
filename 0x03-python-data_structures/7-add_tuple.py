#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length = max(len(tuple_a), len(tuple_b))
    result_tuple = []
    for i in range(length):
        element_a = tuple_a[i] if tuple_a[i] is not None else 0
        if i > len(tuple_b) - 1:
            element_b = 0
        else:
            element_b = tuple_b[i]
        result_tuple.append(element_a + element_b)
    return tuple(result_tuple)

# [[row[i] for row in llist] for i in range(2)]
