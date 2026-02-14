#!/usr/bin/env python3
"""Docstring for numpy.3-flip_me_over."""


def matrix_transpose(matrix):
    """Docstring for matrix_transpose: param matrix: Description."""
    result = []
    temp = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        result.append(temp)
        temp = []
    return result

mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))

# [[1, 2], [3, 4]]
# [[1, 3], [2, 4]]
# [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
# [[1, 6, 11, 16, 21, 26], [2, 7, 12, 17, 22, 27], [3, 8, 13, 18, 23, 28], [4, 9, 14, 19, 24, 29], [5, 10, 15, 20, 25, 30]]