#!/usr/bin/env python3
"""Docstring for 100-slice_like_a_ninja.py."""


import numpy as np


def np_slice(matrix, axes={}):
    """Docstring for np_slice."""
    result = []
    for key in axes.keys():
        for i in range(len(matrix)):
            s = axes[key]
            result.append(matrix[i][slice(*s)].tolist())
    return result

mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#np_slice(mat1, axes={1: (1, 3)})
print(np_slice(mat1, axes={1: (1, 3)}))
print(mat1)
mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                 [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
np_slice(mat2, axes={0: (2,), 2: (None, None, -2)})
print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
print(mat2)

# [[2 3]
#  [7 8]]
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
# [[[ 5  3  1]
#   [10  8  6]]

#  [[15 13 11]
#   [20 18 16]]]
# [[[ 1  2  3  4  5]
#   [ 6  7  8  9 10]]

#  [[11 12 13 14 15]
#   [16 17 18 19 20]]

#  [[21 22 23 24 25]
#   [26 27 28 29 30]]]