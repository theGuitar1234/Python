def quick_sort(list) : 
    left = []
    right = []
    middle = []
   
    if len(list) == 1 or len(list) == 0 :
        return list
    
    mid = len(list)//2
    pivot = list[mid]
    
    for i in range(len(list)) :
        if list[i]<pivot :
            left.append(list[i])
        elif list[i]>pivot :
            right.append(list[i])
        elif list[i]==pivot :
            middle.append(pivot)
    
    return quick_sort(left) + middle + quick_sort(right)
        
arr = [4, 2, 2, 1, 6, 6, 6, 5, 10, 11, 3, 999999999999]
print(quick_sort(arr))