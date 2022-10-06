#!/usr/bin/python3
"""
Function that returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    Returns json representation
    """
    json_rep = json.dumps(my_obj)
    return json_rep
