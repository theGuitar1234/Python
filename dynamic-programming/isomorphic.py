def is_isomorphic_matrix(matrix1, matrix2):
    return matrix1 == matrix2

matrix1 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

matrix2 = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

print(is_isomorphic_matrix(matrix1, matrix2))
