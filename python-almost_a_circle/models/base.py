#!/usr/bin/python3
"""
This program define a Base class for other classes
"""


class Base:
    """ 
    Base of the other shapes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
