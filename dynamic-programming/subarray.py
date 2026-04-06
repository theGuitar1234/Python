def find_non_contiguous_subarrays(lst):
    subsequences = []

    def generate_subsequences(index, current):
        if index == len(lst):
            if current:
                subsequences.append(current)
            return
        
        generate_subsequences(index + 1, current + [lst[index]])
        
        generate_subsequences(index + 1, current)

    generate_subsequences(0, [])
    
    return subsequences

lst = [6, -3, -10, 0, 2]
result = find_non_contiguous_subarrays(lst)
print(result)

def find_non_contiguous_subarrays(lst):
    subsequences = []
    n = len(lst)
    
    for i in range(1, 1 << n):
        subsequence = []
        
        for j in range(n):
            if i & (1 << j): 
                subsequence.append(lst[j])
        
        subsequences.append(subsequence)
    
    return subsequences

lst = [6, -3, -10, 0, 2]
result = find_non_contiguous_subarrays(lst)
print(result)
