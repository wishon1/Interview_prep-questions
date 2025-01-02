#!/usr/bin/python3
"""
using merge sort for the sort color question
"""
def sort_colors(num:list)->list:
    """using merge sort for the sort"""
    if len(num) <= 1:
        return num

    # find the midpoint
    mid_point = len(num) // 2
    left = sort_colors(num[:mid_point])
    right = sort_colors(num[mid_point:])

    return merge(left, right)

def merge(left:list, right:list)->list:
    """merge the left stack and the right stack"""
    output = []
    i=j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    
    # append the remaning lists
    output.extend(left[i:])
    output.extend(right[j:])

    return output


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(sort_colors(nums))
    # Expected output: [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    print(sort_colors(nums))
    # Expected output: [0, 1, 2]