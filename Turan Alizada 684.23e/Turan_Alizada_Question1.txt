def min_num_jumps(list):
    if len(list) <= 1:
        return 0
    if list[0] == 0:
        return -1
    
    maxReach = list[0] 
    steps = list[0]     
    jumps = 1          
    
    for i in range(1, len(list)):
        if i == len(list) - 1:
            return jumps
        maxReach = max(maxReach, i + list[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= maxReach:
                return -1
            steps = maxReach - i
            
    return -1

list = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_num_jumps(list))
