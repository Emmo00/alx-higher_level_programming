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

    def print_sorted(self):
        """ this method prints the list
        but sorted (ascending order)
        """
        tmp = self[:]
        tmp.sort()
        print(tmp)
        del tmp
