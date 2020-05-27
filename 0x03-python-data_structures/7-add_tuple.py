#!/usr/bin/python3


def config(arg):
    x = [0, 0]
    for i in range(2 if len(arg) >= 2 else len(arg)):
        x[i] = arg[i]
    return tuple(x)


def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(map(sum, zip(config(tuple_a), config(tuple_b))))
