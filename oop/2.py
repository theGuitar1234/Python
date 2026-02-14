#!/usr/bin/python3
"""
Docstring for 0-square.py
"""
class Square:
    """
    Docstring for Square
    """
    __size = None
    def __init__(self, size):
        self.__size = size


my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

print(Square.__doc__)
print(type(2))