def breadth_first_search(graph, nodes, node, queue, result, visited_nodes):
    if node not in visited_nodes:
        result.append(node)
        visited_nodes.append(node)
        queue.append(node)

    while len(queue) > 0: 
        current_node = queue.pop(0) 

        for i in range(len(graph[nodes.index(current_node)])):
            if graph[nodes.index(current_node)][i] == 1:  
                neighbor = nodes[i]
                if neighbor not in visited_nodes:  
                    result.append(neighbor)
                    visited_nodes.append(neighbor)
                    queue.append(neighbor)

    return result

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
