#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in my_list]

    # boolist = my_list[:]
    # for count, i in enumerate(my_list):
    #     if i % 2 == 0:
    #         boolist[count] = True
    #     else:
    #         boolist[count] = False
    # return boolist
# def divisible_by_2(my_list=[]):
#     if my_list is None:
#         return []
#     return [i % 2 if i != 0 else True for i in my_list]
#
# def divisible_by_2(my_list):
# #return [i % 2 == 0 if i == 0 True for i in my_list]
# 	return [i % 2 if i != 0 else True for i in my_list]
