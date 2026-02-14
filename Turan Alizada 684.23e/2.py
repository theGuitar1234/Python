#!/usr/bin/python3
# 2-is_same_class.py

def is_same_class(obj, a_class):
    if isinstance(type(obj), a_class):
        return True
    elif type(obj) == a_class:
        return True
    else:
        return False

a = 1
print(is_same_class(a, int))