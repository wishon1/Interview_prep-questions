#!/usr/bin/python3
"""find the longest increasing sequence in unsorted array"""


#!/usr/bin/python3
"""Finds the longest increasing sequence in an unsorted array"""


def lis(seq):
    """Finds the longest increasing sequence"""
    n = len(seq)
    pred = [0] * n
    ends = [-1] * (n + 1)
    ends[0] = -1

    # Initialize the length of the longest increasing subsequence found so far
    max_len = 0

    for i in range(n):
        # Iterate through each element in the sequence
        lo = 1
        hi = max_len + 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if seq[ends[mid]] >= seq[i]:
                hi = mid
            else:
                lo = mid + 1

        new_len = lo
        pred[i] = ends[new_len - 1]
        ends[new_len] = i

        if new_len > max_len:
            max_len = new_len

    lis_seq = [0] * max_len
    index = ends[max_len]
    for j in range(max_len - 1, -1, -1):
        lis_seq[j] = seq[index]
        index = pred[index]

    return lis_seq


if __name__ == "__main__":
    print(lis([10, 22, 9, 33, 21, 50, 41, 60, 80]))
    # Output: [10, 22, 33, 50, 60, 80]

    print(lis([3, 10, 2, 1, 20]))
    # Output: [3, 10, 20]

    print(lis([50, 3, 10, 7, 40, 80]))
    # Output: [3, 7, 40, 80]

    print(lis([]))  # Output: []

    print(lis([5, 4, 3, 2, 1]))
    # Output: [5]
