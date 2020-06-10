#!/usr/bin/python3

"""
module : Pascal Triangle.
"""


def pascal_triangle(n):
    """
    Pascal Triangle generator
    """
    Res = [[1]]
    r3 = []
    if n <= 0:
        return []
    for N in range(n - 1):
        r3 = Res[len(Res) - 1]
        k = []
        for i in range(len(r3) + 1):
            if i == 0 or i == len(r3):
                k.append(1)
            else:
                k.append(r3[i - 1] + r3[i])
        Res.append(k)
    return Res
