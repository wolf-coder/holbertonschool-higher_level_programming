#!/usr/bin/python3


def islower(a):
    if ord(a) in range(ord('a'), ord('z') + 1):
        return True
    else:
        return False


def uppercase(str):
    for i in range(0, len(str)):
        print("{}"
              .format(chr(ord(str[i]) - 32) if islower(str[i]) else str[i]),
              end="")
    print()
