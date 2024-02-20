#!/usr/bin/python3

def longest_increasing_subsequence(sequence):
    n = len(sequence)  # Get the length of the input sequence
    I = [-float('inf')] * (n + 1)  # Initialize array I to track increasing subsequences
    L = [0] * n  # Initialize array L to store lengths of increasing subsequences
    L[0] = 1  # Length of the first subsequence is 1
    I[1] = sequence[0]  # First element of the sequence is inserted at position 1 in I
    length = 1  # Initialize the length of the longest increasing subsequence

    # Iterate over the input sequence
    for i in range(1, n):
        low = 1  # Initialize lower bound for binary search
        high = length  # Initialize upper bound for binary search

        # Binary search to find the position to insert the current element
        while low <= high:
            mid = (low + high) // 2  # Calculate middle index
            if sequence[i] > I[mid]:  # If current element is greater than mid element in I
                low = mid + 1  # Update lower bound
            else:
                high = mid - 1  # Update upper bound

        L[i] = low  # Store the position where the current element is inserted in L
        I[low] = sequence[i]  # Insert the current element in the correct position in I
        if low > length:
            length = low  # Update the length of the longest increasing subsequence if needed

    return length  # Return the length of the longest increasing subsequence


if __name__ == "__main__":
    print(longest_increasing_subsequence(
        [10, 22, 9, 33, 21, 50, 41, 60, 80])
    )
    # Output: [10, 22, 33, 50, 60, 80]

    print(longest_increasing_subsequence([3, 10, 2, 1, 20]))
    # Output: [3, 10, 20]

    print(longest_increasing_subsequence([50, 3, 10, 7, 40, 80]))
    # Output: [3, 7, 40, 80]

    print(longest_increasing_subsequence([]))  # Output: []

    print(longest_increasing_subsequence([5, 4, 3, 2, 1]))
    # Output: [5]
