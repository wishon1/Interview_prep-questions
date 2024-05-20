#!/usr/bin/python3
"""
Write a function undirected_path that takes an array of edges for an
undirected graph and two nodes (nodeA, nodeB). The function should return
a boolean indicating whether or not there exists a path between nodeA and nodeB.
"""

# First, convert the edge list into an adjacency list
def adjacent_graph(graph: list) -> dict:
    """Create an adjacency list from an edge list (graph)."""
    adjacent_list = {}

    for edge in graph:
        a, b = edge

        if a not in adjacent_list:
            adjacent_list[a] = []
        if b not in adjacent_list:
            adjacent_list[b] = []

        # a should be neighbor of b and b should be neighbor of a 
        adjacent_list[a].append(b)
        adjacent_list[b].append(a)

    print(f"This is the converted edge list to  a dict{adjacent_list}")

    return adjacent_list

def undirected_path(adjacent_list: dict, nodeA: str, nodeB: str,
                    visited: set) -> bool:
    """
    The function should return a boolean indicating whether or not there 
    exists a path between nodeA and nodeB.
    """
    if nodeA == nodeB:
        return True

    if nodeA in visited:
        return False

    visited.add(nodeA)

    for neighbor in adjacent_list.get(nodeA, []):
        if undirected_path(adjacent_list, neighbor, nodeB, visited):
            return True

    return False

if __name__ == "__main__":
    edges = [
        ('a', 'b'),
        ('b', 'c'),
        ('c', 'd'),
        ('d', 'e'),
        ('e', 'f')
    ]
    
    graph = adjacent_graph(edges)
    
    print("Using undirected_path function:")
    result = undirected_path(graph, 'a', 'f', set())

    # Should output True
    print(f"Result for path between 'a' and 'f': {result}")
    result = undirected_path(graph, 'a', 'g', set())

    # Should output False
    print(f"Result for path between 'a' and 'g': {result}")
