def breadth_first_search(graph, nodes, node, queue, result, visited_nodes) :

    if node not in visited_nodes :
        result.append(node)
        visited_nodes.append(node)
        queue.append(node)

    for i in range(len(graph[nodes.index(node)])) :
        if graph[nodes.index(node)][i]==1 :
            if nodes[i] not in visited_nodes :
                result.append(nodes[i])
                queue.append(nodes[i])
                visited_nodes.append(nodes[i])
    
    queue = queue[1:]

    if len(queue) == 0:
        return result
    
    for i in queue :
        return breadth_first_search(graph, nodes, i, queue, result, visited_nodes)

graph = [
    #[a, b, c, d, e, f]
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0]
]

nodes = ["a", "b", "c", "d", "e", "f"]
queue = []
result = []
visited_nodes = []
print(breadth_first_search(graph, nodes, "f", queue, result, visited_nodes))