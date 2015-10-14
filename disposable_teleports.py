''' Info on this particular solution can be found here https://www.checkio.org/mission/disposable-teleports/.'''


def find_neighbors(node, graph):
    ''' helper function to help initialize map. creates list of neighbors 
    based on all potential nodes available on map'''
    neighbors = []
    for prospect in graph:
        if prospect[0] == node[1] and prospect != node[::-1]:
            neighbors.append(prospect)
    return neighbors   
​
def startandgraph(string):
    ''' generates a possible starting point given the starting string, and 
    initializes a relational map of viable teleports 
    for each station (node) using a dict, 
    excluding the starting node and it's inverse'''
    connections = {}
    nodes1 = string.split(',')
    nodes2 = [st[::-1] for st in nodes1]
    all_nodes = nodes1 + nodes2
    starts = [st for st in all_nodes if '1' in st[0]] 
    for start in starts:
        for st in all_nodes:
            if st != start and (st != start[::-1]):
                connections[st] = find_neighbors(st, all_nodes)                
        yield start, connections
​
def checkio(string):
    ''' an implementation of solution using Breadth First Search, 
    based on some helpful info from the forums'''
    sg = startandgraph(string)
    visited_all = set('12345678')
    history = []
    for start, graph in sg:
        routes = [""]
        route = ""
        history.append(start)
        active_route = route + start
        queue = [(active_route, start)]
        while queue:
            if set(routes[-1]) == visited_all and routes[-1][-1] == '1':
                route = routes[-1]
                for digit in range(1,9):
                    route = route.replace(str(digit)*2, str(digit))
                return route
​
            active_route, current_node = queue[0]
            queue.remove(queue[0])
            forker = active_route # allows movement to branches possible when >1 neighbor
            used_nodes = [active_route[node_idx:node_idx + 2] 
                    for node_idx in range(0, len(active_route), 2)]
            used_nodes_inverse = [active_route[node_idx:node_idx + 2][::-1] 
                    for node_idx in range(0, len(active_route), 2)]
            if len(used_nodes) != len(set(used_nodes)):
                continue
            if current_node in set(used_nodes_inverse):
                continue                
​
            for neighbor_node in find_neighbors(current_node, graph):  
                active_route = forker                     
                history.append(neighbor_node)                 
                active_route = active_route + neighbor_node
                queue.append((active_route, neighbor_node))
                routes.append(active_route)
​
