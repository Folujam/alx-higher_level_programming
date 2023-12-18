#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    countr = 0
    for i in range(x):
        try:
            print(f"{(my_list[i])}", end="")
            countr += 1
        except IndexError:
            break
    print()
    return (countr)
