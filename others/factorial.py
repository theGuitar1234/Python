def factorial(k):
    if (k == 0):
        return 1
    if (k == 1):
        return 1
    return k*factorial(k-1)
k = 5
print(factorial(5))