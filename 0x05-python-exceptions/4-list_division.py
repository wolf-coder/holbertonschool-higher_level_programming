#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res_l = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except Exception as e:
            if isinstance(e, IndexError):
                print("{}".format("out of range"))
            elif isinstance(e, TypeError):
                print("{}".format("wrong type"))
            elif isinstance(e, ZeroDivisionError):
                print("{}".format("division by 0"))
            res = 0
        finally:
            res_l.append(res)
    return res_l
