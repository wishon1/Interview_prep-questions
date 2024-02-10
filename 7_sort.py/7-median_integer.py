#!/usr/bin/python3
""" find median element in the list of unsorted arrays"""

def find_median(list_of_integers):
    """ find median element"""
    if not list_of_integers:
        return None

    upper = len(list_of_integers)
    lower = 0

    sorted_list = quick_sort(list_of_integers, upper, lower)

    # calculate the median
    median = len(sorted_list) // 2
    return sorted_list[median]

# using quick_sort to first sort the algorithm before finding median
def quick_sort(list_of_integers, upper, lower):
    """Quick sort algorithm"""
    if upper <= lower:
        return
    lock = func_partition(list_of_integers, lower, upper)
    quick_sort(list_of_integers, lock - 1, lower)
    quick_sort(list_of_integers, upper, lock + 1)
    return list_of_integers

def func_partition(list_of_integers, lower, upper):
    """Partition the list"""
    pivot = list_of_integers[lower]
    start = lower + 1
    end = upper

    while True:
        while start <= end and list_of_integers[start] <= pivot:
            start += 1
        while start <= end and list_of_integers[end] > pivot:
            end -= 1
        if start > end:
            break
        list_of_integers[start], list_of_integers[end] = list_of_integers[end], list_of_integers[start]
        start += 1
        end -= 1

    # Swap pivot with the element at end
    list_of_integers[lower], list_of_integers[end] = list_of_integers[end], list_of_integers[lower]
    return end

if __name__ == "__main__":
    print(find_median([1, 2, 4, 6, 3]))  # Output: 3
    print(find_median([4, 2, 1, 2, 3, 1]))  # Output: 2
    print(find_median([2, 2, 2]))  # Output: 2
    print(find_median([]))  # Output: None
    print(find_median([-2, -4, 2, 1]))  # Output: -0.5
    print(find_median([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 2
