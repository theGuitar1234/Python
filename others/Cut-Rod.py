def Cut_Rod(p, n) : 
    if n == 0 : 
        return 0
    q = -1
    for i in range(1, n) :
        q = max(q, p[i]+Cut_Rod(p, n-i))
    return q
print(Cut_Rod([1, 2, 3, 4], 4))