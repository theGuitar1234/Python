def mul(A, B):
    if not A or not B:
        raise ValueError("Empty matrix.")
    if any(len(row) != len(A[0]) for row in A):
        raise ValueError("Matrix A is not rectangular.")
    if any(len(row) != len(B[0]) for row in B):
        raise ValueError("Matrix B is not rectangular.")

    m, n = len(A), len(A[0])
    n2, p = len(B), len(B[0])

    if n != n2:
        raise ValueError(f"Incompatible shapes: A is {m}x{n}, B is {n2}x{p}")

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += A[i][k] * B[k][j]
            result[i][j] = total

    return result

if __name__ == "__main__":
    pass