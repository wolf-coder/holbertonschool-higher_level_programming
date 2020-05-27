#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) != 4:
        print("{} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    elif sys.argv[2] not in '/*+-':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        opp = sys.argv[2]
        Dict = {'+': add, '-': sub, '/': div, '*': mul}

        for op in Dict.keys():
            if op == opp:
                print("{} {} {} = {}".format(a, opp, b, Dict[op](a, b)))
        sys.exit(0)
