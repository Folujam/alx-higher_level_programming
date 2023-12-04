#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return
    else:
        nw_lst = []
        for i in my_list:
            if i % 2 == 0:
                nw_lst.append(True)
            else:
                nw_lst.append(False)
    return nw_lst
