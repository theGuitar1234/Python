def print_path(graph, vertices, v1, v2, visited=None):
    if visited is None:
        visited = set()
    
    if v1 == v2:
        return True
    
    visited.add(v1)
    print(v1)
    
    for i in range(len(graph[vertices.index(v1)])):
        if graph[vertices.index(v1)][i] == 1 and vertices[i] not in visited:
            if print_path(graph, vertices, vertices[i], v2, visited):
                return True
    
    return False

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

print(print_path(graph, vertices, "a", "e"))

