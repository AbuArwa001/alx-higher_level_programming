#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
# largest = 0
# if not a_dictionary:
#     return None
# for x, y in a_dictionary.items():
#     if y >= largest:
#         largest = y
# return largest
