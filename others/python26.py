def binary_search(s, target) :
    pointer1 = 0
    pointer2 = len(s) - 1
    mid = len(s)//2

    z = []

    while pointer1<=mid :
        if s[pointer1] == target :
            z.append("index : " + str(pointer1) + " number : " + str(target))
        
        pointer1 += 1
    
    while pointer2>mid :
        if s[pointer2] == target :
            z.append("index : " + str(pointer1) + " number : " + str(target))
        
        pointer2 -= 1
    
    return z
        
target = 23
s = [23, 5, 8, 23, 16, 23, 38, 45, 23, 91]
print(binary_search(s, target))

def binary_search1(list, x):
    n = len(list)
    a = 0
    b = n-1
    isValid = 0
    
    while a <= b:
        k = (a+b)//2
        
        if list[k] == x:
            isValid = 1
            return k
        
        if list[k] > x:
            b = k-1
            
        else:
            a = k+1
    
    if isValid == 0:
        return -1
            
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]

print(binary_search1(l, 5))
print(binary_search1(l, 10))
print(binary_search1(l, 1))