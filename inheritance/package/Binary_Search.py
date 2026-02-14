def binary_search(s, target, pointer1, pointer2):
    if pointer1 > pointer2:
        return f"{target} not found"
    
    mid = (pointer1 + pointer2) // 2
    print(s[:mid], s[mid:])
    
    if s[mid] == target:
        return f"index : {mid}, target : {target}"
    elif s[mid] < target:
        return binary_search(s, target, mid + 1, pointer2)  
    else:
        return binary_search(s, target, pointer1, mid - 1)  


