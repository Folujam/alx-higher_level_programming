#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys_lst = list(a_dictionary.keys())
    sortd_list = sorted(keys_lst)
    for key in sortd_list:
        print("{}: {}".format(key, a_dictionary[key]))
