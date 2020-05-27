#!/usr/bin/python3
def best_score(a_dictionary):
    a = a_dictionary
    if a_dictionary is not None and a_dictionary:
        return [x for x, y in a.items()if y == max(a.values())][0]
    else:
        return None
