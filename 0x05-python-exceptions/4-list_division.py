#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(0, list_length):
        result_list.append(0)
        try:
            re = my_list_1[i] / my_list_2[i]
            result_list[i] = re
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            continue
    return (result_list)
