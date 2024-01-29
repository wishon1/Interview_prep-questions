
# Integer Operations

This repository contains Python functions to perform various operations on lists of unsorted integers, implemented with the lowest possible complexity.

## 1. Maximum Element

### Problem Statement
Write a function that finds the maximum element in a list of unsorted integers.

### Prototype
```python
def find_maximum(list_of_integers)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-max_integer.py`: Contains the function implementation.
- `7-max_integer.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(find_maximum([1, 2, 4, 6, 3]))  # Output: 6
print(find_maximum([4, 2, 1, 2, 3, 1]))  # Output: 4
print(find_maximum([2, 2, 2]))  # Output: 2
print(find_maximum([]))  # Output: None
print(find_maximum([-2, -4, 2, 1]))  # Output: 2
print(find_maximum([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 4
```

## 2. Minimum Element

### Problem Statement
Write a function that finds the minimum element in a list of unsorted integers.

### Prototype
```python
def find_minimum(list_of_integers)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-min_integer.py`: Contains the function implementation.
- `7-min_integer.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(find_minimum([1, 2, 4, 6, 3]))  # Output: 1
print(find_minimum([4, 2, 1, 2, 3, 1]))  # Output: 1
print(find_minimum([2, 2, 2]))  # Output: 2
print(find_minimum([]))  # Output: None
print(find_minimum([-2, -4, 2, 1]))  # Output: -4
print(find_minimum([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 1
```

## 3. Median Element

### Problem Statement
Write a function that finds the median element in a list of unsorted integers.

### Prototype
```python
def find_median(list_of_integers)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-median_integer.py`: Contains the function implementation.
- `7-median_integer.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(find_median([1, 2, 4, 6, 3]))  # Output: 3
print(find_median([4, 2, 1, 2, 3, 1]))  # Output: 2
print(find_median([2, 2, 2]))  # Output: 2
print(find_median([]))  # Output: None
print(find_median([-2, -4, 2, 1]))  # Output: -0.5
print(find_median([4, 2, 1, 2, 2, 2, 3, 1]))  # Output: 2
```

## 4. Kth Smallest Element

### Problem Statement
Write a function that finds the kth smallest element in a list of unsorted integers.

### Prototype
```python
def find_kth_smallest(list_of_integers, k)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-kth_smallest_integer.py`: Contains the function implementation.
- `7-kth_smallest_integer.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(find_kth_smallest([1, 2, 4, 6, 3], 3))  # Output: 3
print(find_kth_smallest([4, 2, 1, 2, 3, 1], 2))  # Output: 1
print(find_kth_smallest([2, 2, 2], 1))  # Output: 2
print(find_kth_smallest([], 4))  # Output: None
print(find_kth_smallest([-2, -4, 2, 1], 2))  # Output: -2
print(find_kth_smallest([4, 2, 1, 2, 2, 2, 3, 1], 5))  # Output: 2
```

## 5. Kth Largest Element

### Problem Statement
Write a function that finds the kth largest element in a list of unsorted integers.

### Prototype
```python
def find_kth_largest(list_of_integers, k)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-kth_largest_integer.py`: Contains the function implementation.
- `7-kth_largest_integer.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(find_kth_largest([1, 2, 4, 6, 3], 3))  # Output: 3
print(find_kth_largest([4, 2, 1, 2, 3, 1], 2))  # Output: 3
print(find_kth_largest([2, 2, 2], 1))  # Output: 2
print(find_kth_largest([], 4))  # Output: None
print(find_kth_largest([-2, -4, 2, 1], 2))  # Output: 1
print(find_kth_largest([4, 2, 1, 2, 2, 2, 3, 1], 5))  # Output: 1
```

Sure, let's continue with the README:

## 6. Longest Increasing Subsequence

### Problem Statement
Write a function that finds the longest increasing subsequence in a list of unsorted integers.

### Prototype
```python
def longest_increasing_subsequence(list_of_integers)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-longest_increasing_subsequence.py`: Contains the function implementation.
- `7-longest_increasing_subsequence.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))  # Output: [10, 22, 33, 50, 60, 80]
print(longest_increasing_subsequence([3, 10, 2, 1, 20]))  # Output: [3, 10, 20]
print(longest_increasing_subsequence([50, 3, 10, 7, 40, 80]))  # Output: [3, 7, 40, 80]
print(longest_increasing_subsequence([]))  # Output: []
print(longest_increasing_subsequence([5, 4, 3, 2, 1]))  # Output: [5]
```

## 7. Longest Common Subsequence

### Problem Statement
Write a function that finds the length of the longest common subsequence between two lists of unsorted integers.

### Prototype
```python
def longest_common_subsequence(list1, list2)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-longest_common_subsequence.py`: Contains the function implementation.
- `7-longest_common_subsequence.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(longest_common_subsequence([1, 2, 3, 4, 1], [3, 4, 1, 2, 1, 3]))  # Output: 3
print(longest_common_subsequence([5, 3, 2, 1], [3, 2, 1, 5, 7]))  # Output: 3
print(longest_common_subsequence([1, 2, 3], [4, 5, 6]))  # Output: 0
print(longest_common_subsequence([], [4, 5, 6]))  # Output: 0
print(longest_common_subsequence([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: 4
```

Of course! Let's continue:

## 8. Maximum Subarray Sum

### Problem Statement
Write a function that finds the maximum sum of a contiguous subarray within a list of unsorted integers.

### Prototype
```python
def max_subarray_sum(list_of_integers)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-max_subarray_sum.py`: Contains the function implementation.
- `7-max_subarray_sum.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(max_subarray_sum([1, 2, 3, -2, 5]))  # Output: 9
print(max_subarray_sum([]))  # Output: 0
print(max_subarray_sum([-2, -1, -3, -4, -1, -2, -1, -5, -4]))  # Output: -1
print(max_subarray_sum([1]))  # Output: 1
```

## 9. Minimum Number of Jumps to Reach End

### Problem Statement
Write a function that finds the minimum number of jumps needed to reach the end of a list of unsorted integers, where each element represents the maximum number of steps forward that can be taken from that position.

### Prototype
```python
def min_jumps_to_end(list_of_integers)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-min_jumps_to_end.py`: Contains the function implementation.
- `7-min_jumps_to_end.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(min_jumps_to_end([2, 3, 1, 1, 2, 4, 2, 0, 1, 1]))  # Output: 4
print(min_jumps_to_end([1, 3, 6, 1, 0, 9]))  # Output: 3
print(min_jumps_to_end([2, 3, 1, 1, 2, 4, 2, 0, 1, 1, 0]))  # Output: -1
print(min_jumps_to_end([]))  # Output: -1
print(min_jumps_to_end([1]))  # Output: 0
```

## 10. Longest Palindrome Substring

### Problem Statement
Write a function that finds the longest palindrome substring in a given string of unsorted characters.

### Prototype
```python
def longest_palindrome_substring(string)
```

### Constraints
- You are not allowed to import any module.
- The algorithm must have the lowest complexity.

### Files
- `7-longest_palindrome_substring.py`: Contains the function implementation.
- `7-longest_palindrome_substring.txt`: Contains the complexity of the algorithm (e.g., O(log(n)), O(n), O(nlog(n)), or O(n^2)).

### Example Usage
```python
print(longest_palindrome_substring("babad"))  # Output: "bab" or "aba"
print(longest_palindrome_substring("cbbd"))  # Output: "bb"
print(longest_palindrome_substring("a"))  # Output: "a"
print(longest_palindrome_substring(""))  # Output: ""
