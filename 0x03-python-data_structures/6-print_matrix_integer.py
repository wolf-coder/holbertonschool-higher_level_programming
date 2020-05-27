#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    else:
        for elm in matrix:
            Len = len(elm)
            for x in range(Len):
                print("{:d}{}".format(elm[x], " " if x < Len-1 else "\n"),
                      end='')
