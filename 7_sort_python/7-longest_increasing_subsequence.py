#!/usr/bin/python3
"""find the longest increasing sequence in unsorted array"""


def longest_increasing_subsequence(sequence):
    """lis"""
    sequence_length = len(sequence)
    # Get the length of the input sequence
    predecessors = [0] * sequence_length
    # Initialize an array to store the predecessors of each element
    increasing_subsequence_ends = [-1] * (sequence_length + 1)
    # Initialize an array to maintain the ending indices of increasing subsequences
    increasing_subsequence_ends[0] = -1
    # Set the initial value for the ending index of the empty subsequence

    longest_subsequence_length = 0
    # Initialize the length of the longest increasing subsequence found so far

    for i in range(sequence_length):
        # Iterate through each element in the sequence
        lo = 1
        hi = longest_subsequence_length + 1
        # Set the initial values for binary search
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            # Calculate the middle index for binary search
            if sequence[increasing_subsequence_ends[mid]] >= sequence[i]:
                hi = mid
            else:
                lo = mid + 1
            # Perform binary search to find the smallest positive l ≤ L such that X[M[l]] > X[i]

        new_length = lo
        # Determine the length of the new subsequence
        predecessors[i] = increasing_subsequence_ends[new_length - 1]
        # Store the predecessor of the current element
        increasing_subsequence_ends[new_length] = i
        # Update the ending index of the increasing subsequence

        if new_length > longest_subsequence_length:
            longest_subsequence_length = new_length
            # Update the length of the longest increasing subsequence

    longest_subsequence = [0] * longest_subsequence_length
    # Initialize an array to store the longest increasing subsequence
    index = increasing_subsequence_ends[longest_subsequence_length]
    # Get the index of the last element of the longest increasing subsequence
    for j in range(longest_subsequence_length - 1, -1, -1):
        # Iterate from the end of the longest subsequence to the beginning
        longest_subsequence[j] = sequence[index]
        # Populate the longest increasing subsequence array
        index = predecessors[index]
        # Update the index to the predecessor of the current element

    return longest_subsequence
    # Return the longest increasing subsequence


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
