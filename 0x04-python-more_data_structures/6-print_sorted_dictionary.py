#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for Key in sorted(a_dictionary):
        print("{}: {}".format(Key, a_dictionary[Key]))
