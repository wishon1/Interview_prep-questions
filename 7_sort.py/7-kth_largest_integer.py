#!/usr/bin/python3
'''finds the kth largest element in a list of unsorted array'''


def find_kth_largest(list_of_integers, k):
    """finds the kth largest element"""
    if not list_of_integers:
        return None

    sorted_list = quick_sort(list_of_integers)

    return sorted_list[-k]


def quick_sort(array):
    """sort the array using quick sort algirithm"""
    array_len = len(array)
    if array_len <= 1:
        return array

    pivot = array_len - 1
    mid_index = []
    left = []
    right = []

    for i in array:
        if i < array[pivot]:
            left.append(i)
        elif i > array[pivot]:
            right.append(i)
        else:
            mid_index.append(i)

    return (quick_sort(left) + (mid_index) + (quick_sort(right)))


if __name__ == "__main__":
    print(find_kth_largest([1, 2, 4, 6, 3], 3))  # Output: 3
    print(find_kth_largest([4, 2, 1, 2, 3, 1], 2))  # Output: 3
    print(find_kth_largest([2, 2, 2], 1))  # Output: 2
    print(find_kth_largest([], 4))  # Output: None
    print(find_kth_largest([-2, -4, 2, 1], 2))  # Output: 1
    print(find_kth_largest([4, 2, 1, 2, 2, 2, 3, 1], 5))  # Output: 1
