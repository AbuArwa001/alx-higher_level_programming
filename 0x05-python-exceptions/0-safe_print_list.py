#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item_index = 0
    if not my_list:
        return 0
    try:
        for index, item in enumerate(my_list):
            item_index += 1
            print(item, end="")
            if x == item_index:
                break
        print()
    except IndexError:
        print(end="")
    finally:
        return item_index
