#!/usr/bin/python3
"""module that finds the nth smallest elemnet in an unsorted list"""


def find_kth_smallest(list_of_integers, k):
    """ find the kth smallest elemnet in the list:
        args:
            list_of_integers: unsorted list
            k: kth of elemnt to search for
    """
    if not list_of_integers:
        return None

    sorted_list = quick_sort(list_of_integers)
    print(sorted_list)

    return sorted_list[k - 1]


def quick_sort(array):
    """ using quick sort algorithm to sort the array"""
    if len(array) <= 1:
        return array

    mid_point = len(array) // 2

    left = []
    right = []
    mid_arr = []

    for i in array:
        if i < array[mid_point]:
            left.append(i)
        elif i == array[mid_point]:
            mid_arr.append(i)
        else:
            right.append(i)

    return (quick_sort(left) + mid_arr + quick_sort(right))


if __name__ == "__main__":
    print(find_kth_smallest([1, 2, 4, 6, 3], 3))  # Output: 3
    print(find_kth_smallest([4, 2, 1, 2, 3, 1], 2))  # Output: 1
    print(find_kth_smallest([2, 2, 2], 1))  # Output: 2
    print(find_kth_smallest([], 4))  # Output: None
    print(find_kth_smallest([-2, -4, 2, 1], 2))  # Output: -2
    print(find_kth_smallest([4, 2, 1, 2, 2, 2, 3, 1], 5))  # Output: 2
