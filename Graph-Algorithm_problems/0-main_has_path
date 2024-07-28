#!/usr/bin/python3
"""Module for the hasPath problem"""
i_has_path = __import__('iterativeMethod_has_path').has_path
r_has_path = __import__('recursiveMth_has_path').has_path

if __name__ == "__main__":
    graph_01 = {
        'a': ['c', 'b'],
        'b': ['d'],
        'c': ['e'],
        'd': ['f'],
        'e': [],
        'f': []
    }

    graph_02 = {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }

    graph_03 = {
        'a': ['b'],
        'b': ['c'],
        'c': [],
        'd': ['e'],
        'e': []
    }

    print("Using iterative method:")
    print(f"Result for graph_01 is : {i_has_path(graph_01, 'a', 'f')}")
    print(f"Result for graph_02 is : {i_has_path(graph_02, 'f', 'k')}")
    print(f"Result for graph_03 is : {i_has_path(graph_03, 'a', 'e')}")
    
    print()
    print("Using recursive method:")
    print(f"Result for graph_01 is : {r_has_path(graph_01, 'a', 'f')}")
    print(f"Result for graph_02 is : {r_has_path(graph_02, 'f', 'k')}")
    print(f"Result for graph_03 is : {r_has_path(graph_03, 'a', 'e')}")
