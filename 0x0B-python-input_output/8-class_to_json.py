#!/usr/bin/python3
""" This module defines the function class_to_json."""


def class_to_json(obj):
    """ This class returns the dictionary description of object """
    return obj.__dict__
