#!/usr/bin/python3
"""
This module defines a function returns True if the object is an instance of,
 or if the objectis an instance of a class that inherited from the specified
  class; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """ This function returns True if obj is an instance of or if the obj
    is an instance of the class.
    """
    return isinstance(obj, a_class)
