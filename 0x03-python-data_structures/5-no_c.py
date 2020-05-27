#!/usr/bin/python3


def no_c(my_string):
    Len = len(my_string)
    cpy = []
    for ch in my_string:
        if ch not in "cC":
            cpy.append(ch)
    return ''.join(cpy)
