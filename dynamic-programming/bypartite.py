def is_bipartite(graph):
    color = [-1] * len(graph)

    def bfs(start):
        queue = [start]
        color[start] = 0
        
        while queue:
            node = queue.pop(0)
            
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True

    for i in range(len(graph)):
        if color[i] == -1:
            if not bfs(i):
                return False
    return True

graph = [
    [1, 3],
    [0, 2],
    [1, 3],
    [0, 2]
]

print(is_bipartite(graph))
