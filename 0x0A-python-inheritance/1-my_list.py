#!/usr/bin/python3
"""Defines MyList class - a subclass of the list class
Example:
    >>> my_list = MyList()
    """


class MyList(list):
    """MyList - a subclass of the list class
    class methods:
        print_sorted()
        """

    def __init__(self, iterable=[]):
        """initialize the MyList class
        Uses init from base class `list`
        """
        super().__init__(iterable)

    def print_sorted(self):
        """ this method prints the list
        but sorted (ascending order)
        """
        tmp = []
        for item in self:
            tmp.append(item)
        tmp.sort()
        print(tmp)
        del tmp
