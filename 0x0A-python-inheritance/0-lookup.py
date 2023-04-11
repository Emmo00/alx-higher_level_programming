#!/usr/bin/python3
"""0-lookup module defines one function:
    lookup()
    """


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""

    meth_list = []
    for item in dir(obj):
        meth_list.append(item)
    return meth_list
