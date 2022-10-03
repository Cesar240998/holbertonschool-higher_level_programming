#!/usr/bin/python3
"""inherits_from
"""


    def inherits_from(obj, a_class):
        """Returns True if obj is an instance of a_class, else False
        """
        return isinstance(obj, a_class) and type(obj) != a_class
