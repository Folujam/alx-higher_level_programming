#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) is 0:
        return
    else:
        for i in my_list:
            if i % 2 is 0:
                return True
            else:
                return False
