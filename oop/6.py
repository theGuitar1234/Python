#!/usr/bin/python3

"""
Docstring for 4-square.py
"""


class Square:

    """
    Docstring for Square
    """

    def __init__(self, size):
        __size = size
    
    @property
    def size(self):
        if not isinstance(size, int):
            raise Exception("")
        return self.__size