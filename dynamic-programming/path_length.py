def print_path(graph, vertices, v1, v2, visited):
    
    if v1 == v2:
        return [v1] 
    
    visited.append(v1)
    
    for i in range(len(graph[vertices.index(v1)])):
        if graph[vertices.index(v1)][i] == 1 and vertices[i] not in visited:
            path = print_path(graph, vertices, vertices[i], v2, visited)
            if path :
                return [v1] + path
    
    return []

graph = [
    # [a, b, c, d, e, f]
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0]
]

vertices = ["a", "b", "c", "d", "e", "f"]

lengths = []

for i in range(len(vertices)) :
    visited = []
    for j in range(i+1, len(vertices)) :
        lengths.append((len(print_path(graph, vertices, vertices[i], vertices[j], visited)), vertices[i], vertices[j]))

for i in lengths :
    print(i)

