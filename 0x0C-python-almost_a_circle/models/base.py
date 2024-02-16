#!/usr/bin/python3


"""
This is the base class module
"""

class Base:
    """The base class

    Represents the base for the other classes.
    
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class

        Args:
            id(int): The id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
