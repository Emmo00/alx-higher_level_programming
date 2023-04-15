#!/usr/bin/python3
"""Defines the Rectangle class
"""


from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
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
        for _ in range(self.__width):
            for __ in range(self.__height):
                print("#", end="")
            print("")

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(
                self.__name__,
                self.id,
                self.__x,
                self.__y,
                self.__width,
                self._height)
