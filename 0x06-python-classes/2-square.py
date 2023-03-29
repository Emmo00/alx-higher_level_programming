#!/usr/bin/python3
class Square():
    """A square class
    
    Args:
        size: (integer) size of the square
    Attributes:
        size: private
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        self.__size = size
