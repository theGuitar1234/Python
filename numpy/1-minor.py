#!/usr/bin/env python3
"""Docstring for numpy.1-minor."""


def minor(mat):
    """Docstring for minor."""
    if (
        not isinstance(mat, list)
        or not all(isinstance(row, list) for row in mat)
    ):
        print("matrix must be a list of lists")
        return
    if (
        len(mat) == 0
        or any(len(row) == 0 for row in mat)
        or any(len(row) != len(mat) for row in mat)
    ):
        print("matrix must be a non-empty square matrix")
        return
    result = []
    for p in range(len(mat)):
        for i in range(len(mat[p])):
            chunk = []
            for j in range(len(mat)):
                if (j != p):
                    temp = []
                    for k in range(len(mat[j])):
                        if (k != i):
                            temp.append(mat[j][k])
                    chunk.append(temp)
            result.append(chunk)
    minor = [[0 for _ in range(len(mat))] for _ in range(len(mat))]
    n = len(mat)
    if n == 1:
        return [[1]]
    for idx, sub in enumerate(result):
        r = idx // n
        c = idx % n
        minor[r][c] = determinant(sub)
    return minor

def determinant(mat):
    """Docstring for determinant."""
    if (not isinstance(mat, list) or len(mat) == 0 or
            not all(isinstance(row, list) for row in mat) or
            any(len(row) == 0 for row in mat)):
        raise TypeError("matrix must be a list of lists")
    n = len(mat)
    if any(len(row) != n for row in mat):
        raise TypeError("matrix must be a square matrix")
    if (len(mat) == 1):
        # print("reached the end : ", mat)
        return mat[0][0]
    result = []
    res = 0
    for i in range(len(mat[0])):
        chunk = []
        for j in range(1, len(mat)):
            temp = []
            for k in range(len(mat[j])):
                if (k != i):
                    temp.append(mat[j][k])
            chunk.append(temp)
        result.append(chunk)
        res += mat[0][i] * determinant(chunk) * (-1)**i
    return res

mat4 = [
    [5, 7, 9], 
    [3, 1, 8], 
    [6, 2, 4]
]
print(minor(mat4))

# if __name__ == '__main__':

#     mat1 = [[5]]
#     mat2 = [[1, 2], [3, 4]]
#     mat3 = [[1, 1], [1, 1]]
#     mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
#     mat5 = []
#     mat6 = [[1, 2, 3], [4, 5, 6]]

#     print(minor(mat1))
#     print(minor(mat2))
#     print(minor(mat3))
#     print(minor(mat4))
#     try:
#         minor(mat5)
#     except Exception as e:
#         print(e)
#     try:
#         minor(mat6)
#     except Exception as e:
#         print(e)


# [[1]]
# [[4, 3], [2, 1]]
# [[1, 1], [1, 1]]
# [[-12, -36, 0], [10, -34, -32], [47, 13, -16]]
# matrix must be a list of lists
# matrix must be a non-empty square matrix