#!/usr/bin/python3
""" This module defines the function from_json_string. """
import json


def from_json_string(my_str):
    """ This function returns an object represented
    by a json string. """
    return json.loads(my_str)
