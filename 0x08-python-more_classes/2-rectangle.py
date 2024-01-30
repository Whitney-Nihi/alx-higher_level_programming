#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width(int): The width of the Rectangle
            height(int): The height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the Rectangle"""
        return self.__width

    @property
    def height(self):
        """Get the height of the Rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (self.__height + self.__width) * 2
