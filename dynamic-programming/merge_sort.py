def merge_sort(s) :
    if len(s) > 1 :
        mid  = len(s)//2
        R = s[mid:]
        L = s[:mid]

        merge_sort(R)
        merge_sort(L)

        k = j = i = 0
        while j<len(R) and i<len(L) :
            if R[j]<L[i] :
                s[k] = R[j]
                j+=1
                k+=1
            else :
                s[k] = L[i]
                i+=1
                k+=1
        while j<len(R) :
            s[k] = R[j]
            j+=1
            k+=1
        while i<len(L) :
            s[k] = L[i]
            i+=1
            k+=1
z = [1,3,2]
merge_sort(z)
print(z)