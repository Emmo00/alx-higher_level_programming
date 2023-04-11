#!/usr/bin/python3
"""Defines MyList class - a subclass of the list class
Example:
    >>> my_list = MyList()
    """


class MyList(list):
    """MyList - a subclass of the list class"""

    def __init__(self, iterable=[]):
        super().__init__(iterable)

    def print_sorted(self):
        tmp = []
        for item in self:
            tmp.append(item)
        tmp.sort()
        print(tmp)
        del tmp
