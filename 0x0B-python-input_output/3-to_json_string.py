#!/usr/bin/python3
""" This module defines the function to_json_string. """
import json


def to_json_string(my_obj):
    """ This function returns an object turned into
    a json string. """
    return json.dumps(my_obj)
