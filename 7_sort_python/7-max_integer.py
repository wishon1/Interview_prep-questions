#!/usr/bin/python3
""" module to find the maximum element in an unsorted list"""


def find_maximum(list_of_integers):
    """find the maximum element in a list of unsorted integers"""
    if not list_of_integers:
        return None

    max_elem = list_of_integers[0]
    for i in list_of_integers:
        if i > max_elem:
            max_elem = i

    return max_elem


if __name__ == "__main__":

    print(find_maximum([1, 2, 4, 6, 3]))  # Output: 6
    print(find_maximum([4, 2, 1, 2, 3, 1]))  # Output: 4
    print(find_maximum([2, 2, 2]))  # Output: 2
    print(find_maximum([]))  # Output: None
    print(find_maximum([-2, -4, 2, 1]))  # Output: 2
    print(find_maximum([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4

