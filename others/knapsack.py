def knapsack(capacity, weights, values) :
    dp = [[0]]
    k = 0
    if not weights or capacity == 0 :
        return 0
    
    for i in range(1, 5) :
        dp.append([])
        dp[i].append(k)
        k += 1

    for i in range (len(weights)) :
        for j in range(i+1, len(weights)) :
            if weights[i]+weights[j] not in dp[0] and weights[i]+weights[j]<=capacity :
                dp[0].append(weights[i]+weights[j])

    for i in range(1, len(dp)) :
        for j in range(len(dp[0])-1) :
            dp[i].append(0)
    for i in dp :
        print(i, end="\n")

weights = [0, 10, 20, 30]
values = [0, 60, 100, 120]
capacity = 50

print(knapsack(capacity, weights, values))