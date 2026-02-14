import sys
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    
    next = 1  
    prev = 0  

    for i in range(2, n + 1):  
        current = next + prev  
        prev = next 
        next = current  

    return next 
sys.set_int_max_str_digits(100000)
print(fibonacci(50000))
