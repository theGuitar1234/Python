def balanced_brackets(str) :
    brackets = { "[" : 0, "]" : 0, "{" : 0, "}" : 0, "(" : 0, ")" : 0 }

    for i in str :
        if i == "[" :
            brackets["["] += 1
        elif i == "]" :
            brackets["]"] += 1
        elif i == "(" :
            brackets["("] += 1
        elif i == ")" :
            brackets[")"] += 1
        elif i == "{" :
            brackets["{"] += 1
        elif i == "}" :
            brackets["}"] += 1
        else :
            raise ValueError("Unsupported Character")
    
    result = list(brackets.items())
    
    print("Brackets : " + str + "\nResult  : ", result)
    
    for i in range(0, len(result), 2) :
        if result[i][1] != result[i+1][1] :
            return f"{str} is not balanced"
    return f"{str} is balanced"


str = "[[[{}{}[[((()()()))]()]]{}{}]]"
print(balanced_brackets(str))

def balanced_brackets_stack(str):
    brackets = { "[" : "]", "{" : "}", "(" : ")" }
    stack = []
    for i in s :
        if i in "[({" :
            stack.append(i)
        elif i in "])}" :
            if len(stack) == 0 or brackets[stack[-1]] != i :
                return f"{str} is not balanced"
            stack.pop()

    if len(stack) == 0 :
        return f"{str} is balanced"
    else :
        return f"{str} is not balanced"

s = "[[[{}{}[[((()()()))]()]]{}{}]]{{}}"
print(balanced_brackets_stack(s))
