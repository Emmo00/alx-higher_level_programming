#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    sum = 0
    for i in my_list:
        if i not in uniq:
           sum = sum + i
    return sum 
