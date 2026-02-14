def mul(mat1, mat2):
    if (len(mat1[0]) != len(mat2)):
        raise ValueError("Invalid Entries for multiplication")
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(result)):
        for j in range(len(result[i])):
            sum = 0
            for k in range(len(mat2)):
                sum += mat1[i][k]*mat2[k][j]
            result[i][j] = sum

    return result

mat1 = [
    [2, -2],
    [5, 3]
]

mat2 = [
    [-1, 4, 5],
    [7, -6, 5]
]

print(mul(mat1, mat2))