#!/usr/bin/python3


def Display():
    import sys
    i = ""
    Len = len(sys.argv)
    Plural = "s"
    if Len == 1:
        End = "."
    else:
        if Len == 2:
            Plural = ""
        End = ":"

    print("{} argument{}{}".format(Len - 1, Plural, End))
    if Len > 1:
        for i in range(1, Len):
            print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    Display()
