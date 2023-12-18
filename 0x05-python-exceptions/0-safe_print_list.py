#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item_index = 0
    for index, item in enumerate(my_list):
        try:
            print(item, end="")
            item_index += 1
            if x == item_index:
                break
        except IndexError:
            break
    print()
    return item_index
