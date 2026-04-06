def depth_first_search(graph, nodes, node, stack, result, visited_nodes):
    if node not in visited_nodes:
        result.append(node)
        visited_nodes.append(node)
        stack.append(node)

    while len(stack) > 0:
        current_node = stack.pop()

        for i in range(len(graph[nodes.index(current_node)])):
            if graph[nodes.index(current_node)][i] == 1: 
                neighbor = nodes[i]
                if neighbor not in visited_nodes:
                    result.append(neighbor)
                    visited_nodes.append(neighbor)
                    stack.append(neighbor)

    return result

graph = [
    # [a, b, c, d, e, f]
    [0, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0]
]

nodes = ["a", "b", "c", "d", "e", "f"]
stack = []
result = []
visited_nodes = []
print(depth_first_search(graph, nodes, "a", stack, result, visited_nodes))
