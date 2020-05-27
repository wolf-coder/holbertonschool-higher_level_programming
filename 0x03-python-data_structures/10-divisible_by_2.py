#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy = []
    for i in my_list:
        if i % 2 == 0:
            cpy.append(True)
        else:
            cpy.append(False)
    return cpy
