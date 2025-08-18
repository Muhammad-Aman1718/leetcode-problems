# Binary Search

# Given a sorted array arr[] and an integer k, find the position(0-based indexing) at which k is present in the array using binary search. If k doesn't exist in arr[] return -1.

# Note: If multiple occurrences are there, please return the smallest index.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 5], k = 4
# Output: 3
# Explanation: 4 appears at index 3.

# Input: arr[] = [11, 22, 33, 44, 55], k = 445
# Output: -1
# Explanation: 445 is not present.

# Input: arr[] = [1, 1, 1, 1, 2], k = 1
# Output: 0
# Explanation: 1 appears at index 0.


class Solution:
    def binarysearch(self, arr: list[int], k: int):
        # Code Here
        for i in range(len(arr)):
            if arr[i] == k:
                return i

        return -1


obj = Solution()
arr: list[int] = [1, 2, 3, 4, 5]
k = 45

print(obj.binarysearch(arr, k))
