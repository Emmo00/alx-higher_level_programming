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
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """Area of square
        
        Args:
            no arguments
        Return:
            area of the square
        """
        return self.__size ** 2
