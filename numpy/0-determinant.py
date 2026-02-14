#!/usr/bin/env python3
"""Docstring for numpy.0-determinant."""


def determinant(mat):
    """Docstring for determinant."""
    if (not isinstance(mat, list) or len(mat) == 0 or
            not all(isinstance(row, list) for row in mat)):
        print("matrix must be a list of lists")
        return
    if len(mat) == 1 and len(mat[0]) == 0:
        return 1
    n = len(mat)
    if any(len(row) != n for row in mat):
        print("matrix must be a square matrix")
        return
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

# # mat = [
# #     [1, 8], 
# #     [2, 4]
# # ]
# # print(determinant(mat))

# if __name__ == '__main__':

#     mat0 = [[]]
#     mat1 = [[5]]
#     mat2 = [
#         [1, 2], 
#         [3, 4]
#     ]
#     mat3 = [
#         [1, 1], [1, 1]
#     ]
#     mat4 = [
#         [5, 7, 9], 
#         [3, 1, 8], 
#         [6, 2, 4]
#     ]
#     mat5 = []
#     mat6 = [
#         [1, 2, 3], 
#         [4, 5, 6]
#     ]

#     print(determinant(mat0))
#     print(determinant(mat1))
#     print(determinant(mat2))
#     print(determinant(mat3))
#     print(determinant(mat4))
#     try:
#         determinant(mat5)
#     except Exception as e:
#         print(e)
#     try:
#         determinant(mat6)
#     except Exception as e:
#         print(e)

# # 1
# # 5
# # -2
# # 0
# # 192
# # matrix must be a list of lists
# # matrix must be a square matrix