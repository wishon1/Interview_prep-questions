#!/usr/bin/python3
"""
Write a function has_path that takes in an object representing the
adjacency list of a directed acyclic graph and two nodes (src, dst). The
function should return a boolean indicating whether or not there exists a
directed path between the source node and the destination node.
"""


def has_path(graph: dict, src: str, dst: str) -> bool:
    """
    The function should return a boolean indicating whether or not there
    exists a directed path between the source node and the destination node.

    Args:
        graph (dict): Dictionary representing the adjacency list of an acyclic
        graph.
        src (str): The source node.
        dst (str): The destination node.

    Returns:
        bool: Whether or not there exists a directed path from src to dst.
    """
    print("{}".format(src), end=', ')
    if src == dst:
        return True

    for neighbor in graph.get(src, []):
        if has_path(graph, neighbor, dst):
            return True
    return False

    # Algorim = depth first traversal.
    # BigO notation: time complexitive = O(e) - Where e is the number of edges
    # space complexity = O(n) - Where n is the number of node or vortex
