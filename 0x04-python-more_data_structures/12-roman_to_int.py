#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str\
       or roman_string is None or len(roman_string) is 0:
        return 0
    Len = len(roman_string)
    d = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    N = 0
    for i in range(Len):
        for Key in d.keys():
            if Key == roman_string[i]:
                N += d[Key]
                if i > 0 and d[roman_string[i-1]] < d[roman_string[i]]:
                    N -= 2 * d[roman_string[i-1]]
    return N
