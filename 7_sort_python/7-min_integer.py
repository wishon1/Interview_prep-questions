#!/usr/bin/python3
""" find the minimum element in a kist of unsorted array"""

def find_minimum(list_of_integers):
    """ find the minimum eleement"""
    if not list_of_integers:
        return None

    min_elem = list_of_integers[0]
    for i in list_of_integers:
        if i < min_elem:
            min_elem = list_of_integers[i]

    return min_elem


if __name__ == "__main__":
    print(find_minimum([1, 2, 4, 6, 3]))  # Output: 1
    print(find_minimum([4, 2, 1, 2, 3, 1]))  # Output: 1
    print(find_minimum([2, 2, 2]))  # Output: 2
    print(find_minimum([]))  # Output: None
    print(find_minimum([-2, -4, 2, 1]))  # Output: -4
    print(find_minimum([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 1
    
