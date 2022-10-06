#!/usr/bin/python3
"""
Function that  returns an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Returns json representation
    """
    obj_rep = json.loads(my_str)
    return obj_rep
