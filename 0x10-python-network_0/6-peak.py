#!/usr/bin/python3
"""
6. Find a peak
"""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    """
    L = list_of_integers
    if L == []:
        return None
    if len(L) == 1:
        return L[0]
    if L[0] >= L[1]:
        return L[0]
    if L[len(L) - 1] >= L[len(L) - 2]:
        return L[len(L) - 1]
    for i in range(1, len(L) - 1):
        if L[i] >= L[i - 1] and L[i] >= L[i + 1]:
            return L[i]
