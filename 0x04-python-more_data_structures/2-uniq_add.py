#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set()
    for i in my_list:
        uniq_list.add(i)
    s = sum(uniq_list)
    return (s)
