#!/usr/bin/python3
''' This module defines the class Base '''


class Base():

    __nb_objects = 0

    def __init__(self, id=None):
        ''' This method takes id and assigns it to the id var
        if no id was passed, it will increment __nb_objects
        and assign that value to id '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
