#!/usr/bin/python3
""" Find the median element in a list of unsorted arrays"""

def find_median(list_of_integers):
    """ Find the median element"""
    if not list_of_integers:
        return None

    sorted_list = quick_sort(list_of_integers)

    # Calculate the median
    n = len(sorted_list)

    # if len of list is even
    if n % 2 == 0:
        median_index = (sorted_list[n // 2 - 1] + sorted_list[n // 2]) / 2
    else:
        # if the len of the listis odd
        median_index = sorted_list[n // 2]
    return median_index

def quick_sort(arr):
    """ Quick sort algorithm"""
    if len(arr) <= 1:
        return arr
    
    # i choose to use the element in the mid index as pivot
    pivot = arr[len(arr) // 2]
    
    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)

        if x == pivot:
            middle.append(x)

        if x > pivot:
            right.append(x)
   # left = [x for x in arr if x < pivot]
   # middle = [x for x in arr if x == pivot]
   # right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    print(find_median([1, 2, 4, 6, 3]))  # Output: 3
    print(find_median([4, 2, 1, 2, 3, 1]))  # Output: 2
    print(find_median([2, 2, 2]))  # Output: 2
    print(find_median([]))  # Output: None
    print(find_median([-2, -4, 2, 1]))  # Output: -0.5
    print(find_median([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 2
