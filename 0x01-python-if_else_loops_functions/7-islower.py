#!/usr/bin/python3
def islower(a):
    if ord(a) in range(ord('a'), ord('z') + 1):# + 1 is not checked by the checker
        return True
    else:
        return False
