def fibo(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
        return memo[n]

n = 5
memo = [-1] * (n + 1)

print(fibo(n, memo))