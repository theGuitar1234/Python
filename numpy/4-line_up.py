#!/usr/bin/env python3
"""Docstring for numpy.4-line_up."""


def add_arrays(arr1, arr2):
    """Docstring for add_arrays :param arr1: Description :param arr2: Description"""    
    if (len(arr1) != len(arr2)):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
print(add_arrays(arr1, arr2))
print(arr1)
print(arr2)
print(add_arrays(arr1, [1, 2, 3]))

# [6, 8, 10, 12]
# [1, 2, 3, 4]
# [5, 6, 7, 8]
# None