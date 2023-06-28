#!/usr/bin/python3
"""6-peak module:
    defines find_peak funciton"""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) in [1, 2]:
        return max(list_of_integers)
    return max(list_of_integers[1:-1])
