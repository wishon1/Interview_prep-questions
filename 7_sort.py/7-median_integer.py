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
    median = len(sorted_list) / 2
    return sorted_list[median]


    
    # using quick_sort to first sort the algorithm before finding median
    def quick_sort(list_of_integers, upper, lower):
        """ quick sort algorithm"""
        if (upper < lower):
            lock  = func_partution(list_of_integers, lower, upper)
            quick_sort(list_of_integers, lower, lock - 1)
            quik_sort(list_of_integers, lock + 1, upper)

        return list_of_integers

    def func_partition(list_of_integers, lower, upper):
        """ partition the list"""
        pivot = list_of_integers[lower]
        start = lower
        end = upper
            
        while (start < end )
            while (list_of_integers[start] <= pivot)
                   start++
            while (list_of_integers > pivot)
                    end--
                if (start < end )
                    
    def swap(list_of_integers[i], list
                    
                



if __name__ == "main"
    print(find_median([1, 2, 4, 6, 3]))  # Output: 3
    print(find_median([4, 2, 1, 2, 3, 1]))  # Output: 2
    print(find_median([2, 2, 2]))  # Output: 2
    print(find_median([]))  # Output: None
    print(find_median([-2, -4, 2, 1]))  # Output: -0.5
    print(find_median([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 2



