def isConnected(graph, nodes, node, queue, result, visited_nodes):
    if node not in visited_nodes :
        result.append(node)
        visited_nodes.append(node)
        queue.append(node)

    while len(queue) != 0 : 
        current = queue.pop(0)

        for i in range(len(graph[nodes.index(current)])):
            if graph[nodes.index(current)][i] == 1:
                if nodes[i] not in visited_nodes:
                    result.append(nodes[i])
                    queue.append(nodes[i])
                    visited_nodes.append(nodes[i])

    if len(result) == len(graph) :
        return True
    else :
        return False

def euler_path(graph, nodes) :
    queue = []
    result = []
    visited_nodes = []

    if not isConnected(graph, nodes, nodes[0], queue, result, visited_nodes):
        return "The Graph is not Connected"

    num_odd_degree = 0
    for i in range(len(graph)):
        degree = 0
        for j in graph[i] :
            if j == 1 :
                degree += 1
        if degree % 2 != 0:
            num_odd_degree += 1

    if num_odd_degree == 0:
        return f"Euler circuit exists for the graph"
    elif num_odd_degree == 2:
        return f"Euler path exists for the graph but with no circuits"
    else:
        return f"Euler path does not exist for the graph"

graph = [
    [0, 1, 1, 1, 0],  # a
    [1, 0, 0, 1, 1],  # b
    [1, 0, 0, 1, 0],  # c
    [1, 1, 1, 0, 1],  # d
    [0, 1, 0, 1, 0]   # e
]

nodes = ["a", "b", "c", "d", "e"]

print(euler_path(graph, nodes))
