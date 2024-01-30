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
            return (self.__height + self.__height) * 2

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
