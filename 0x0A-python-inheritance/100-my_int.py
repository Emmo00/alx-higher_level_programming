#!/usr/bin/python3
"""Defines MyInt class - a subclass of the int class
Example:
    >>> my_int = MyInt()
    """


class MyInt(int):
    """MyList - a subclass of the list class
    class methods:
        print_sorted()
        """

    def __init__(self, number):
        """initialize the MyList class
        Uses init from base class `list`
        """
        super().__init__()

    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
