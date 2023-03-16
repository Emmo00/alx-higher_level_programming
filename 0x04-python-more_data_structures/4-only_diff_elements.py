#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    com = []
    for e in set_1:
        if e not in set_2:
            com.append(e)
    for e in set_2:
        if e not in set_1:
            com.append(e)
    return com
