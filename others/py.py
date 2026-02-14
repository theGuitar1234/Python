weights = [0, 10, 20, 30, 80]
values = [0, 60, 100, 120, 100]
dp = [[0, 0]]
capacity = 200
k = 0

for i in range(1, len(values)+1) :
    dp.append([])
    dp[i].append(k)
    k += 1

for i in range (len(weights)) :
    for j in range(i+1, len(weights)) :
        if weights[i]+weights[j] not in dp[0] and weights[i]+weights[j]<=capacity :
            dp[0].append(weights[i]+weights[j])
dp[0].sort()

for i in range(1, len(dp)) :
    for j in range(len(dp[0])-1) :
        dp[i].append(0)

max = 0
for i in range(1, len(values)) :
    for j in range(2, len(dp[0])) :
        w = dp[0][j]
        if weights[i] <= w :
            if w-weights[i] in weights :
                if values[i] + values[weights.index(w-weights[i])] > max :
                    max = values[i] + values[weights.index(w-weights[i])]
            dp[i+1][j] = max
        else :
            dp[i+1][j] = values[i]
       
                
for i in dp :
    print(i, end="\n")
print(max)


