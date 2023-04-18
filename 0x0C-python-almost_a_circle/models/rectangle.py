#!/usr/bin/python3
"""Defines the Rectangle class
"""


Base = __import__('base').Base


class Rectangle(Base):
    """Rectangle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize Rectangle class
        """
        super().__init__(id)
        self.validate_integer("width", width)
        self.validate_integer("height", height)
        self.validate_integer("x", x)
        self.validate_integer("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.validate_integer("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validate_integer("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print('\n' * self.y, end="")
        for _ in range(self.__width):
            print("{}".format(" " * self.x), end="")
            for __ in range(self.__height):
                print("#", end="")
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self.__height)

    def update(self, *args, **kwargs):
        if len(args) > 0:
            if arg[0] is not None or type(args[0]) == int:
                self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ndict = dict()
        for key in self.__dict__:
            ndict[key.replace("_Rectangle__", "")] = self.__dict__[key]
        return ndict
