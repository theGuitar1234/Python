def is_subset(arr1, arr2) :
    arr1 = quick_sort(arr1)

    for i in arr2 :
        if not binary_search(arr1, i, 0, len(arr1)-1) :
            return False
    return True
    
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

def binary_search(s, target, pointer1, pointer2):
    if pointer1 > pointer2:
        return False
    
    mid = (pointer1 + pointer2) // 2
    
    if s[mid] == target:
        return True
    elif s[mid] < target:
        return binary_search(s, target, mid + 1, pointer2)  
    else:
        return binary_search(s, target, pointer1, mid - 1) 

arr1 = [4, 7, 1, 9, 3, 2]
arr2 = [3, 7, 2]

print(is_subset(arr1, arr2))

    