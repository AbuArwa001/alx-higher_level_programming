#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item_index = 0
    for item in range(x):
        try:
            print(my_list[item], end="")
            item_index += 1
        except IndexError:
            break
    print("")
    return item_index
