#!/usr/bin/env python3
from typing import List
"""88 merge sort problem from LeetCode top 150 interview prep"""

class Solution:
    def __init__(self):
        """do nothing"""
        pass

    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 in-place.
        
        :param nums1: List[int], the first sorted array with extra space at the end
        :param m: int, number of elements in nums1 (excluding extra space)
        :param nums2: List[int], the second sorted array to be merged into nums1
        :param n: int, number of elements in nums2
        :return: None. Modify nums1 in-place instead.
        """
        # Step 1: Copy elements from nums2 to the end of nums1
        for j in range(n):
            nums1[m+j] = nums2[j]
        
        # Step 2: Sort the entire nums1 array using merge sort
        self.mergeSort(nums1, 0, m+n-1)

    def mergeSort(self, nums1, lhs, rhs):
        """
        Recursive merge sort function.
        
        :param nums1: List[int], the array to be sorted
        :param lhs: int, left index of the subarray
        :param rhs: int, right index of the subarray
        """
        if lhs < rhs:
            mid_point = (lhs + rhs) // 2
            self.mergeSort(nums1, lhs, mid_point)
            self.mergeSort(nums1, mid_point + 1, rhs)
            self.merge_arrays(nums1, lhs, mid_point, rhs)

    def merge_arrays(self, nums1, lhs, mid, rhs):
        """
        Merge two sorted subarrays of nums1.
        
        :param nums1: List[int], the array containing both subarrays
        :param lhs: int, start index of the first subarray
        :param mid: int, end index of the first subarray
        :param rhs: int, end index of the second subarray
        """
        left = nums1[lhs:mid+1]
        right = nums1[mid+1:rhs+1]
        
        i, j, k = 0, 0, lhs
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums1[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            nums1[k] = right[j]
            j += 1
            k += 1
    

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge nums2 into nums1 in-place.
        
        :param nums1: List[int], the first sorted array with extra space at the end
        :param m: int, number of elements in nums1 (excluding extra space)
        :param nums2: List[int], the second sorted array to be merged into nums1
        :param n: int, number of elements in nums2
        """
        # Start from the end of the arrays
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for placing elements

        # Merge arrays from back to front
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1


if __name__ == "__main__":
    """the example to check the class"""
    solution = Solution()


    num1 = [1, 2, 3, 0, 0, 0]
    m = 3
    n = 3
    num2 = [2, 5, 6]
    expected_output = [1, 2, 2, 3, 5, 6]
       
   
    solution.merge(num1, m, num2, n)
    print(f"Test Case 1 for Big O(n log n): {num1}")

    merge(num1, m, num2, n)
    print(f"Test Case 1 for O(m + n): {num1}")

    num1 = [0]
    m = 0
    num2 = [1]
    n = 1
    expected_output = [1]

    solution.merge(num1, m, num2, n)
    print(f"Test Case 2 for Big O(n log n): {num1}")

    merge(num1, m, num2, n)
    print(f"Test Case 2 for O(m + n): {num1}")




""""
solution.merge:
1. Best Case:
   Time Complexity: O(n log n)
   
   Even in the best case scenario (when the input array is already sorted), merge sort will still
   divide the array and merge it back together. The number of divisions is always log n, and each
   level of merging still requires n operations.

2. Average Case:
   Time Complexity: O(n log n)
   
   The average case performance is the same as the best case. Merge sort consistently performs the
   same number of comparisons and merges regardless of the initial order of the elements.

3. Worst Case:
   Time Complexity: O(n log n)
   
   The worst case is also O(n log n). Even with the most unordered input, merge sort will perform the
   same number of operations as in the best and average cases.

Explanation of O(n log n):
- The "log n" comes from the number of times the array is divided in half (in the mergeSort method).
- The "n" comes from the merging step (in the merge_arrays method), which processes n elements at each
level of recursion.

Space Complexity:
The space complexity is O(n) because:
- In your implementation, you're creating temporary arrays in the merge_arrays method.
- At any given time, these temporary arrays will hold at most n elements (when merging the two halves
of the full array).
"""

"""
merge():

Time Complexity: O(n + m)

1. The algorithm uses a single while loop that runs until all elements from nums2 have been
placed (p2 >= 0).
2. In each iteration, we place one element either from nums1 or nums2 into its final position.
3. The loop will run for a maximum of n + m iterations, where:
   - n is the number of elements in nums2
   - m is the number of elements originally in nums1
4. Each operation inside the loop (comparison, assignment, decrementing pointers) takes constant
time O(1).
5. Therefore, the total time complexity is O(n + m).

Detailed breakdown:
- Best case: O(n), when all elements in nums2 are larger than those in nums1. In this case, we only 
eed to copy n elements from nums2.
- Worst case: O(n + m), when we need to compare and move elements from both arrays.
- Average case: O(n + m), as we typically need to process elements from both arrays.

Space Complexity: O(1)

1. The algorithm uses a constant amount of extra space, regardless of the input size.
2. It only uses three integer variables as pointers (p1, p2, p):
   - p1: pointer for nums1
   - p2: pointer for nums2
   - p: pointer for the current position in nums1 where we're placing elements
3. No additional data structures are created.
4. The merging is done in-place within the existing nums1 array.

Detailed breakdown:
- The space used is constant and doesn't grow with the input size.
- We're not creating any new arrays or data structures.
- The original nums1 array is modified in-place.
- The extra space at the end of nums1 is utilized to store the merged result.

Additional notes:
1. This solution is more efficient than the previous merge sort approach, both in time and
space complexity.
2. It takes advantage of the fact that both input arrays are already sorted.
3. By merging from the end, it avoids the need for shifting elements, which would be necessary
if merging from the front.
4. This approach is optimal for the given problem, as it achieves the minimum possible time 
omplexity (we must examine each element at least once) and space complexity (in-place modification).

In summary, this solution provides an efficient O(n + m) time complexity with O(1) space complexity,
making it an optimal approach for merging two sorted arrays in-place.
"""
