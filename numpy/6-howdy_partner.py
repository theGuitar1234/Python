#!/usr/bin/env python3
"""Docstring for numpy.6-howdy_partner."""


def cat_arrays(arr1, arr2):
    """Docstring for cat_arrays."""
    return arr1 + arr2

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8]
print(cat_arrays(arr1, arr2))
print(arr1)
print(arr2)

# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5]
# [6, 7, 8]