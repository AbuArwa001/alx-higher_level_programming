#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item_index = 0
    for index, item in enumerate(my_list):
        try:
            item_index += 1
            print(item, end="")
            if x == item_index:
                break
        except IndexError:
            print(end="")
    print()
    return item_index
