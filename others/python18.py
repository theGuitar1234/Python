def grid(m, n) :
    if m or n == 1 :
        return 1
    else :
        return grid(m-1, n) + grid(m, n-1)
    
    