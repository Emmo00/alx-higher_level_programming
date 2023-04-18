#!/usr/bin/python3
"""Defines the square class
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the Square Class
        calls Parent class (Rectangle)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square
        object
        """
        if len(args) >= 2:
            args = list(args)
            args.insert(1, args[1])
            args = tuple(args)
        super().update(*args, **kwargs)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id,
                self.x,
                self.y,
                self.width
                )

    def to_dictionary(self):
        """Return dictionary representation of
        the Square class
        """
        ndict = super().to_dictionary()
        ndict['size'] = ndict['width']
        del ndict['width']
        del ndict['height']
        return ndict
