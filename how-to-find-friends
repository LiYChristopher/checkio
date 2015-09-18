'''
We have an array of straight connections between drones. Each connection is represented as a 
string with two names of friends separated by hyphen. 
For example: "dr101-mr99" means what the dr101 and mr99 are friends. 
You should write a function that allow determine more complex connection between drones. 
You are given two names also. Try to determine if they are related through common bonds by any depth. 

For example: if two drones have a common friends or friends who have common friends and so on.

This concept will help you find not too obvious connections with the building of bond networks. 
And how to work social networks.
'''

def check_connection(network, first, second):
    '''
    Scans network for path between two nodes - first and
    second. By "walking" through the network via mutual friends:
        1. Node of interest is discovered (True)
        2. No path from first to second exists. (False)
    '''
    relationships = [pair.split('-') for pair in network]
    visited = [first]
    in_path = []
    # Finds neighbor relationships of initial node
    for conn in relationships:
        if first in conn:
            in_path.append(conn)
    # Search neighbors until second is located, or terminate.
    for pair in in_path:
        if second in pair:
            return True
        for conn in relationships:
            if any(node in conn for node in pair):
                in_path.append(conn)
                relationships.remove(conn)
    return False 
