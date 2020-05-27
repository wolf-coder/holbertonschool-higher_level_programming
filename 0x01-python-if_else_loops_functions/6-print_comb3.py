#!/usr/bin/python3
inc1 = 8


def display(start):
    for k in range(start, start + inc1 + 1):
        print("{:02d}, ".format(k), end="")


for i in range(1, 89, 11):
    display(i)
    inc1 = inc1 - 1
print(89)
