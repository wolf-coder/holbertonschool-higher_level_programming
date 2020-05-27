#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    Len = len(my_list)
    cpy = my_list[:]
    if idx > Len-1 or idx < 0:
        return cpy
    else:
        cpy[idx] = element
        return cpy
