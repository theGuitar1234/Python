def shortest_path(graph, nodes, result, node):
    result[nodes.index(node)] = 0
    for i in range(len(graph[nodes.index(node)])):
        if graph[nodes.index(node)][i] != 0:
            result[i] = graph[nodes.index(node)][i]

    for k in range(len(graph)):
        for i in range(len(graph)):
            if result[i] != 999:
                for j in range(len(graph[i])): 
                    if graph[i][j] != 0:
                        if result[i] + graph[i][j] < result[j]:
                            result[j] = result[i] + graph[i][j]
                            
    return result


graph = [
    [0, 1, 4, 0],
    [1, 0, 2, 3],
    [4, 2, 0, 1],
    [0, 3, 1, 0]
]

nodes = ["a", "b", "c", "d"]
result = [999, 999, 999, 999] 

print(shortest_path(graph, nodes, result, "c"))
