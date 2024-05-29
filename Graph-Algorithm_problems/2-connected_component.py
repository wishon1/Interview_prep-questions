#!/usr/bin/env python3
"""
Write a function, connected_component_count that takes in the adjacency
list of an undirected graph. The function should return the nimber of
connected component withon the graph
"""


def connected_component_count(graph):
    """
    This function returns the number of connected components within the graph.
    """
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True


if __name__ == "__main__":
    # Test the function with the provided graph
    graph1 = {
        '0': ['8', '1', '5'],
        '1': ['0'],
        '5': ['0', '8'],
        '8': ['0', '5'],
        '2': ['3', '4'],
        '3': ['2', '4'],
        '4': ['3', '2']
        }

    graph2 = {
        '0': ['1', '2', '3'],
        '1': ['0', '2'],
        '2': ['0', '1', '3'],
        '3': ['0', '2']
        }

    graph3 = {
        '0': [],
        '1': [],
        '2': [],
        '3': []
        }

    print(connected_component_count(graph1))  # Output should be 2

    print(connected_component_count(graph2))  # Output should be 1

    print(connected_component_count(graph3))  # Output should be 4
