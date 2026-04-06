def longest_valid_bracket(s):
    stack = [-1] 
    max_len = 0
    n = len(s) 
    
    for i in range(n): 
        char = s[i]
        
        if char == '{':
            stack.append(i) 
        else:  
            stack.pop()
            
            if stack:
                max_len = max(max_len, i - stack[-1]) 
            else:
                stack.append(i)  
    
    return max_len

s = "(()()())"
print(longest_valid_bracket(s)) 
