#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length = max(len(tuple_a), len(tuple_b))
    result_tuple = []
    for i in range(0, 2):
        if i > len(tuple_a) - 1:
            element_a = 0
        else:
            element_a = tuple_a[i]

        if i > len(tuple_b) - 1:
            element_b = 0
        else:
            element_b = tuple_b[i]
        result_tuple.append(element_a + element_b)
    return tuple(result_tuple)
# [[row[i] for row in llist] for i in range(2)]
# def add_tuple(tuple_a=(), tuple_b=()):
#     length = max(len(tuple_a), len(tuple_b))
#     result_tuple = tuple(
#         tuple_a[i] + tuple_b[i] if i < len(tuple_a) and
#         i < len(tuple_b) and tuple_b[i] is not None else
#         tuple_a[i] if i < len(tuple_a) else
#         tuple_b[i] if i < len(tuple_b) and tuple_b[i] is not None else
#         0
#         for i in range(length)
#     )
#     return result_tuple
