#A graph must be connected in order to have a euler path, I didn't check if the graph is connected or not.
#I added isConnected so check if the graph is connected or not and write True or False.

#There is no need to check for loops, their degree is 2 and won't change the sum to an odd number anyways, so I put None and they will be ignored

def euler_path(graph) :

    isConnected = True
    if isConnected :
        num_odd_degree = 0
        for i in range(len(graph)):
            degree = 0
            for j in graph[i] :
                if j == 1 :
                    degree += 1
            if degree % 2 != 0:
                num_odd_degree += 1

        if num_odd_degree == 0:
            return "Euler circuit exists for the graph"
        else:
            return "Euler circuit does not exist for the graph"
    else :
        return "The Graph is not connected"

graph = [
    [None, 1, 1, 1, 1],  
    [1, None, 1, 1, 1], 
    [1, 0, None, 1, 0],  
    [1, 1, 1, None, 1],  
    [0, 1, 0, 1, None]  
]

nodes = ["a", "b", "c", "d", "e"]

print(euler_path(graph))
