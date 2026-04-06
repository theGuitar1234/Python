def smaller_integers_stack(arr) :
    stack = [] 
    result = []  

    for num in arr:
        while stack and stack[-1] >= num:
            stack.pop()

        if stack:
            result.append(stack[-1])
        else:
            result.append(None)  

        stack.append(num)

    return result

arr = [1, 6, 4, 10, 2, 5]
print(smaller_integers_stack(arr))