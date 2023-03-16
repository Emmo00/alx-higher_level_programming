#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = []
    for e in my_list:
        if e == search:
            list.append(replace)
            continue
        list.append(e)
    return list
