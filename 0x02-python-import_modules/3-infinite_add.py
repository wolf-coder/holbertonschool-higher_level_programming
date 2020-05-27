#!/usr/bin/python3


def Display():
    import sys
    list1 = [int(i) for i in sys.argv[1:]]
    print("{}".format(sum(list1)))

if __name__ == "__main__":
    Display()
