def minimum_spanning_tree(graph, nodes, node, queue, result, visited_nodes, weights):

    if node not in visited_nodes:
        result.append(node)
        visited_nodes.append(node)
        queue.append(node)

    for i in range(len(graph[nodes.index(node)])):
        if graph[nodes.index(node)][i] != 0 and nodes[i] not in visited_nodes:
            weights.append((graph[nodes.index(node)][i], nodes[i]))
            queue.append(nodes[i])

    print("Weights:", weights)
    print("Queue:", queue)

    min_weight_node = None
    min_weight = 999

    for i in weights:
        if i[1] not in visited_nodes and i[0] < min_weight:
            min_weight = i[0]
            min_weight_node = i[1]

    if min_weight_node and min_weight_node not in result:
        print("Selected Min Weight Node:", min_weight_node)
        result.append(min_weight_node)
        visited_nodes.append(min_weight_node)  

    queue.pop(0) 

    if len(queue) == 0:
        return result

    return minimum_spanning_tree(graph, nodes, queue[0], queue, result, visited_nodes, weights)


graph = [
    #  a  b  c  d  e
    [0, 4, 1, 3, 0],  # a
    [4, 0, 0, 2, 5],  # b
    [1, 0, 0, 6, 0],  # c
    [3, 2, 6, 0, 7],  # d
    [0, 5, 0, 7, 0]   # e
]

nodes = ["a", "b", "c", "d", "e"]
queue = []
result = []
visited_nodes = []
weights = []

print("Minimum Spanning Tree:", minimum_spanning_tree(graph, nodes, "a", queue, result, visited_nodes, weights))
