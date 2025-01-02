#!/usr/bin/python3
"""
Given an array of distinct integer values, count the number of pairs of integers that
have difference k. For example, given the array { 1, 7, 5, 9, 2, 12, 3} and the difference
k = 2,there are four pairs with difference2: (1, 3), (3, 5), (5, 7), (7, 9).
"""
def brut_force(array):
    if not arra or len(array) < 2:
        return []
 
    result = []
    for a in range(len(array)):
        for b in range(len(array)):
            if array[b] - array[a] == 2:
                result.append((array[a], array[b]))
    return result

def print_pairs_with_diff_k(array, k):
    """
    Prints all pairs of integers with difference k using a hash table approach.
    """
    if not array or len(array) < 2:
        return []

    # Convert array to hash set for O(1) lookups
    # Example: [1, 7, 5, 9, 2, 12, 3] becomes {1, 2, 3, 5, 7, 9, 12}
    num_set = set(array)

    # Initialize empty list to store our pairs
    pairs = []

    # Iterate through each number x in the array
    # Example: for x = 1, we'll check if 1 + 2 = 3 exists in set
    for x in array:
        # Check if the required pair number (x + k) exists in our set
        # Example: if x = 1 and k = 2, check if 3 exists in set
        if x + k in num_set:
            # If pair is found, add it to our results
            # Example: when x = 1, adds (1, 3) to pairs
            pairs.append((x, x + k))

    # Example: returns [(1, 3), (3, 5), (5, 7), (7, 9)]
    return pairs

if __name__ == "__main__":
    # Test array and difference value
    array = [1, 7, 5, 9, 2, 12, 3]
    k = 2

    result = brut_force(array)
    print(f'The result is: {result}')

    # Get and print all pairs
    pairs = print_pairs_with_diff_k(array, k)
    print(f"Pairs with difference {k}: {pairs}")

    # Verify that all pairs have the correct difference
    for x, y in pairs:
        assert y - x == k, f"Invalid pair: {x}, {y}"
    print("All pairs verified correctly")
