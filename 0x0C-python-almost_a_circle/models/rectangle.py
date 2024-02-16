#!/usr/bin/python3

"""Defines a sub-class 'Rectangle'."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base Class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes the Rectangle class.

        Args:
            width(int): Width of te rectangle.
            height(int): Height of the rectangle.
            x(int): The x coordinate of the rectangle.
            y(int): The y coordinate of the rectangle.
            id(int): The identity of the rectangle.

        Raises:
            TypeError: If width or geight is not an integer.
            TypeError: If x or y is not an integer.
            ValueError: If width or height is <= 0.
            ValueError: If x or y is < 0.  
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter and setter for Rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be > 0".format(width))
        self.__width = width

    @property
    def height(self):
        """height getter and setter for Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be > 0".format(height))
        self.__height = height

    @property
    def x(self):
        """x getter and setter for Rrectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("{} must be an integer".format(x))
        if x < 0:
            raise ValueError("{} must be >= 0".format(x))
        self.__x = x

    @property
    def y(self):
        """y getter and setter for Rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("{} must be an integer".format(y))
        if y < 0:
            raise ValueError("{} must be >= 0".format(y))
        self.__y = y

    def area(self):
        """Returns area value of Rectangle."""
        return self.width * self.height

    def display(self):
        """Function prints object with character #."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.heigt):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")


    def __str__(self):
        """Return the string representation of the rectangle."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)


    def update(self, *args, **kwargs):
        """Method assigns an argument to each attribute.

        Args:
            *args(ints): Instance attributes.
                - 1st argument represents id attr
                - 2nd argument represents width attr
                - 3rd argument represents height attr
                - 4th argument represents x attr
                - 4th argument represents y attr
            **kwargs(dictionary): Instance attributes in key/value pairs.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle."""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
