def transpoze(mat):
    result = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = mat[j][i]
    return result

if __name__ == "__main__":
    pass