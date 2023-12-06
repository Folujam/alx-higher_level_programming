#!usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return
    else:
        max_key = None
        max_val = -float('inf')
        for key, value in a_dictionary.items():
            if value > max_val:
                max_val = value
                max_key = key
    return (max_key)
