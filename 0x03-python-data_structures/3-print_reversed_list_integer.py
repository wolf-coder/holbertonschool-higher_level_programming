#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
"""
if you try  for in  my_list.reverse() it fails->
TypeError: 'NoneType' object is not iterable
"""
